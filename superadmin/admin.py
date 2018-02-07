from django.contrib import admin
from .models import Invoice, Donor


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'select_ngo']


admin.site.register(Invoice, InvoiceAdmin)


class DonorAdmin(admin.ModelAdmin):
    list_display = ['donor_id', 'donor_name']
    search_fields = ['donor_name']


admin.site.register(Donor, DonorAdmin)
