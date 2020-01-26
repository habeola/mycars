from django.shortcuts import render
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Make, Brand, CarDetail, Contact, BodyType, Transmission, FUEL_CHOICES
from .forms import CreateForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


def is_valid_queryparam(param):
    return param != '' and param is not None


def sidebar(request):
    post = Brand.objects.all()
    maker = Make.objects.all()
    transmis = Transmission.objects.all()
    car_types = CarDetail.objects.all()
    fuel_choices = FUEL_CHOICES
    bodies = BodyType.objects.all()
    brand = request.GET.get('brand')
    trans = request.GET.get('trans')
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')
    body = request.GET.get('body')
    fuel = request.GET.get('fuel')
    print(fuel)

    

    if is_valid_queryparam(brand):
        car_types = CarDetail.objects.filter(brand__name=brand)

    
    if is_valid_queryparam(body):
        car_types = CarDetail.objects.filter(body_type__name=body)


    if is_valid_queryparam(trans):
        car_types = CarDetail.objects.filter(transmission__name=trans)


    if is_valid_queryparam(fuel):
        car_types = CarDetail.objects.filter(fuel_type=fuel)

    

    if is_valid_queryparam(min_year) and min_year != 'From':
        car_types = CarDetail.objects.filter(year__gte=min_year)

    
    if is_valid_queryparam(max_year) and max_year != 'To':
        car_types = CarDetail.objects.filter(year__lte=max_year)



    context = {
        'post': post,
        'car_types': car_types,
        'maker': maker,
        'bodies': bodies,
        'transmis': transmis,
        'fuel_choices': fuel_choices
    }
    return render(request, 'filterandsearch.html', context)


def sidebar_detail(request, id):
    car_detail = get_object_or_404(CarDetail, id=id)
    context = {
       'car_detail': car_detail
    }
    return render(request, 'single-product.html', context)



def search(request):
    post = Brand.objects.all()
    car_type = CarDetail.objects.all()
    query = request.GET.get('q')
    # To do absolute url
    print(query)
    if query:
        car_type = car_type.filter(
            Q(make__name__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(body_type__name__icontains=query)
        ).distinct()

    context = {
        'car_type': car_type,
        'post': post
    }

    return render(request, 'search.html', context)



def  index(request):
    car_type = CarDetail.objects.filter(exclusive=True)
    maker = Make.objects.all()
    bodies = BodyType.objects.all()
    context = {
        'car_type': car_type,
        'maker': maker,
        'bodies': bodies
    }
    return render(request, 'index.html', context)


def category_shop(request):
    post = Brand.objects.all()
    maker = Make.objects.all()
    bodies = BodyType.objects.all()
    fuel_choices = FUEL_CHOICES
    transmis = Transmission.objects.all()
    car_type = CarDetail.objects.order_by('-timestamp')
    paginator = Paginator(car_type, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    # To do absolute url

    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)

    context = {
        'car_type': car_type,
        'paginated_qs': paginated_qs,
        'page_request_var': page_request_var,
        'post': post,
        'maker': maker,
        'bodies': bodies,
        'transmis': transmis,
        'fuel_choices': fuel_choices
    }
    return render(request, 'category.html', context)


def carlist_page(request, make):
    post = Brand.objects.all()
    bodies = BodyType.objects.all()
    transmis = Transmission.objects.all()
    car_type = get_object_or_404(Make, name=make)
    car_list = Make.objects.get(name=make).makes.all()
    paginator = Paginator(car_list, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    

    try:
        car_make = paginator.page(page)
    except PageNotAnInteger:
        car_make = paginator.page(1)
    except EmptyPage:
        car_make = paginator.page(paginator.num_pages)
    

    context = {
        'car_type':car_type,
        'page_request_var': page_request_var,
        'car_make':car_make,
        'post':post,
        'bodies':bodies,
        'transmis': transmis
    }
    return render(request, 'listbycarmake.html', context)


def viewcar_detail(request, make, id):
    car_type = get_object_or_404(Make, name=make)
    car_detail = get_object_or_404(CarDetail, id=id)

    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("The form is valid")
            return redirect("category")

    context = {
       'car_type': car_type,
       'car_detail': car_detail,
       'form': form
    }
    return render(request, 'single-product.html', context)


def viewcar_detail2(request, id):
    car_detail = get_object_or_404(CarDetail, id=id)
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone') 
            message = form.cleaned_data.get('message')
            contact_info = Contact(
                user=request.user,
                full_name=full_name,
                email=email,
                phone=phone,
                message=message
            )
            contact_info.save()

            return redirect("category")
            messages.info(self.request, "Your information has been submited")
    context = {
       'car_detail': car_detail,
       'form': form
    }
    return render(request, 'single-product.html', context)


def filter_page(request):
    return render(request, 'sidebar.html')

@login_required
def createview(request):
    title = 'Create'
    form = CreateForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("category")

    context = { 
        'form': form,
        'title': title
    }
    return render(request, 'create.html', context)
    
@staff_member_required
def updateview(request, id):
    title = 'Update'
    car_detail = get_object_or_404(CarDetail, id=id)
    form = CreateForm(request.POST or None, request.FILES or None, instance=car_detail)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("category")

    context = { 
        'form': form,
        'title': title
    }
    return render(request, 'create.html', context)


@staff_member_required
def deleteview(request, id):
    car_detail = get_object_or_404(CarDetail, id=id)
    if request.method == "POST":
        car_detail.delete()
        return redirect("category")
    context = {
        'car_detail': car_detail
    }
    return render(request, 'delete.html', context)


#class ContactView(request):
   # def get(self, *args, **kwargs):
        #form = ContactForm(request.POST or None)
       # if request.method == "POST":
        #return render(self.request, "")

