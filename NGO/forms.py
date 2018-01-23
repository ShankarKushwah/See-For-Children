from django import forms
from .models import Events, Children, Certificate
from django.contrib.auth.forms import UserChangeForm


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'date', 'place', 'description', 'organizer', 'time', 'type', 'image']


class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = ['name', 'dob', 'gender', 'place_found', 'image', 'description', 'education', 'school','hobby','adoption_date']


class EditChildrenForm(UserChangeForm):
    class Meta:
        model = Children
        fields = ['name', 'dob', 'gender', 'place_found', 'image', 'description', 'education', 'school','hobby','adoption_date']


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['donor_name', 'donation_amount', 'sponsored_child_code', 'sponsored_child_name', 'month', 'certificate_issue_date']
