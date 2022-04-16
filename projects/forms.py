from django import forms
from django.contrib.auth.models import User
from .models import Profile,Neighborhood,Business,Post,Service
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']