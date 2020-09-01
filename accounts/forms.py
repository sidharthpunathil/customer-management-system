# from django.forms import  ModelForm
from .models import Order, Customer
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'John'}),
            'phone': forms.NumberInput(
                attrs={'placeholder': '+91 1234567890'}),
            'email': forms.TextInput(attrs={'placeholder': 'johndoe@mail.com'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
