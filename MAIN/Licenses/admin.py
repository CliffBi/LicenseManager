from django.contrib import admin
from .models import Licenses


class ManagerLicense(admin.ModelAdmin):
    list_display = ('license_name', 'guarantee', 'copyleft', 'different_license', 'active')
    list_filter = ('DFSG_compatible', 'FSF_approved', 'OSI_approved', 'GPL_compatible')
    fields = (
        'license_name',
        ('guarantee', 'DFSG_compatible', 'FSF_approved', 'OSI_approved', 'GPL_compatible'),
        ('copyleft', 'different_license', 'active'),
    )


admin.site.register(Licenses, ManagerLicense)
