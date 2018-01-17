from django import forms
from NGO.models import NGO
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['name', 'email', 'established', 'city', 'area', 'director',
                  'no_of_children', 'no_of_staff', 'state', 'zip_code', 'image']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
