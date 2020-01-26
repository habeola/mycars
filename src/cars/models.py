from django.db import models
from django.urls import reverse
from django.conf import settings


User = settings.AUTH_USER_MODEL

FUEL_CHOICES = (
    ('Diesel', 'Diesel'),
    ('Petrol', 'Petrol'),
    ('Petroleum Gas', 'Petroleum Gas')
)

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Make(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BodyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Transmission(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        

class Drivetrain(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarDetail(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    make = models.ForeignKey(Make, related_name='makes', on_delete=models.CASCADE)
    year = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    mileage = models.IntegerField()
    price = models.IntegerField()
    transmission = models.ForeignKey(Transmission, on_delete=models.SET_NULL, blank=True, null=True)
    fuel_type = models.CharField(choices=FUEL_CHOICES, max_length=15)
    feature = models.ManyToManyField(Feature)
    body_type = models.ForeignKey(BodyType, related_name='bodytypes', on_delete=models.SET_NULL, blank=True, null=True)
    ext_color = models.CharField(max_length=100)
    drivetrain = models.ForeignKey(Drivetrain, on_delete=models.SET_NULL, blank=True, null=True)
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    display = models.BooleanField()
    exclusive = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return f"{self.id}"



    def detail_url(self):
        return reverse('viewcar_detail2', kwargs={
            'id': self.id
        })


    def update_url(self):
        return reverse('update', kwargs={
            'id':self.id
        })

    def delete_url(self):
        return reverse('delete', kwargs={
            'id':self.id
        })


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(blank=True, null=False)
    message = models.TextField()

    def __str__(self):
        self.user.username










