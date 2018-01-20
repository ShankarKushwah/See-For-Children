from django import forms
from NGO.models import NGO
from superadmin.models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['select_ngo', 'child_code', 'donor_id', 'donation_month', 'invoice', 'date', 'paid']

