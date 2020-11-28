from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=64)
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32,
                                       widget=forms.PasswordInput
                                       )
