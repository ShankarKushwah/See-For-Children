from django.contrib import admin
from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['select_ngo']


admin.site.register(Invoice, InvoiceAdmin)
