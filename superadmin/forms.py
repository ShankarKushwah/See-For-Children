from django import forms
from NGO.models import NGO, Events, Children


class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['name', 'code', 'email', 'established', 'city', 'area', 'director',
                  'no_of_children', 'no_of_staff', 'state', 'zip_code', 'image']
