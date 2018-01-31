from django import forms
from .models import Events, Children, Certificate, NGO, Photo
from django.contrib.auth.forms import UserChangeForm


class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'date', 'place', 'description', 'organizer', 'type', 'image']
        widgets = {'date': DateInput()}


class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = ['name', 'dob', 'gender', 'place_found', 'image', 'description', 'education', 'school', 'hobby',
                  'adoption_date', 'video_link']
        widgets = {'dob': DateInput(), 'adoption_date': DateInput()}


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['donor_name', 'donation_amount', 'sponsored_child_code', 'sponsored_child_name', 'month',
                  'certificate_issue_date']
        widgets = {'certificate_issue_date': DateInput(), }


class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['name', 'email', 'state', 'city', 'zip_code', 'director', 'no_of_children', 'no_of_staff',
                  'established', 'area', 'image']
        widgets = {'established': DateInput(), }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['file', ]
