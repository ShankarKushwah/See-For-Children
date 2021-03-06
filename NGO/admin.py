from django.contrib import admin
from .models import NGO, Events, Children, Donor, Certificate, Photo


class NGOAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'email', 'city']


admin.site.register(NGO, NGOAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'place', 'date']


admin.site.register(Events, EventAdmin)


class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'ngo', 'dob', 'gender', 'adoption_date']


admin.site.register(Children, ChildrenAdmin)


class DonorAdmin(admin.ModelAdmin):
    list_display = ['name', 'child_code', 'city']


admin.site.register(Donor, DonorAdmin)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['ngo', 'donor_name']


admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Photo)
