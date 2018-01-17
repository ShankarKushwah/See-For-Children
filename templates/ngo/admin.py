from django.contrib import admin
from .models import NGO, Events, Children, Staff, Certification, Donor, Photos


class NGOAdmin(admin.ModelAdmin):
    list_display = ['id', 'ngo_name', 'ngo_email', 'ngo_director', 'ngo_city']


admin.site.register(NGO, NGOAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_place', 'event_date']


admin.site.register(Events, EventAdmin)


class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['c_name', 'c_gender', 'c_place_found']


admin.site.register(Children, ChildrenAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_work', 's_address']


admin.site.register(Staff, StaffAdmin)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['ngo_name', 'donor_name']


admin.site.register(Certification, CertificateAdmin)
admin.site.register(Donor)
admin.site.register(Photos)
