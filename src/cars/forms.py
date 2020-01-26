from django import forms
from .models import CarDetail


class CreateForm(forms.ModelForm):
    class Meta:
        model = CarDetail
        fields = ('make', 'brand', 'year', 'price', 'mileage', 'transmission', 'fuel_type', 'feature', 'body_type', 'drivetrain', 'ext_color', 'image1', 'image2', 'display', 'exclusive')


class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Full name',
        'class': 'form-control'
        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'Placeholder': 'Email address',
        'class': 'form-control'
    }))
    phone = forms.IntegerField(required=False, widget=forms.TextInput(attrs={
        'Placeholder': 'Phone Number',
        'class': 'form-control'
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'class': 'form-control',
        'rows': '5'
        }))
