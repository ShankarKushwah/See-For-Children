from django import forms
from superadmin.models import Invoice


class DateInput(forms.DateInput):
    input_type = 'date'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['select_ngo', 'child_name', 'child_code', 'donor_id', 'donation_month', 'date', 'paid']
        widgets = {'date': DateInput(), }

