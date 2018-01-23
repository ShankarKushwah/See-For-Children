from django.contrib import admin
from .models import NGO, Events, Children, Staff, Donor, Certificate


class NGOAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'email', 'city']


admin.site.register(NGO, NGOAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'place', 'date']


admin.site.register(Events, EventAdmin)


class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'ngo', 'dob', 'gender', 'adoption_date']


admin.site.register(Children, ChildrenAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'work', 'address']


admin.site.register(Staff, StaffAdmin)


class DonorAdmin(admin.ModelAdmin):
    list_display = ['name', 'child_code', 'city']


admin.site.register(Donor, DonorAdmin)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['ngo', 'donor_name']


admin.site.register(Certificate, CertificateAdmin)
