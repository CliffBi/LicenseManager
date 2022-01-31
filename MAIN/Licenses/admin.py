from django.contrib import admin
from .models import Licenses


#admin.site.register(Licenses)

class ManagerLicense(admin.ModelAdmin):
    list_display = ('license_name', 'guarantees', 'copyleft', 'different_license')
    list_filter = ('DFSG_compatible', 'FSF_approved', 'OSI_approved', 'GPL_compatible')
    fields = [
        'license_name',
        'copyright_holder',
        ('guarantees', 'DFSG_compatible', 'FSF_approved', 'OSI_approved', 'GPL_compatible'),
        ('copyleft', 'different_license'),
    ]


admin.site.register(Licenses, ManagerLicense)

