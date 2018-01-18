from django import forms
from .models import Events, Children
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'date', 'place', 'description', 'organizer', 'time', 'type']


class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = ['name', 'dob', 'gender', 'place_found', 'image', 'description', 'education', 'school','hobby','adoption_date']


class EditChildrenForm(UserChangeForm):
    class Meta:
        model = Children
        fields = ['name', 'dob', 'gender', 'place_found', 'image', 'description', 'education', 'school','hobby','adoption_date']
