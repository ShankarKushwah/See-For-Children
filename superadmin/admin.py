from django.contrib import admin
from .models import Invoice, Donor


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['select_ngo']


admin.site.register(Invoice, InvoiceAdmin)


class DonorAdmin(admin.ModelAdmin):
    list_display = ['donor_id', 'donor_name']


admin.site.register(Donor, DonorAdmin)
