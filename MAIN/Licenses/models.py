from django.db import models


class Licenses(models.Model):
    license_name =      models.CharField(max_length=30)
    # copyright_holder = models.CharField(max_length=100)
    guarantee =         models.BooleanField(blank=True, null=True, help_text='Is the license guaranteed?')
    DFSG_compatible =   models.BooleanField(blank=True, null=True, help_text='')
    FSF_approved =      models.BooleanField(blank=True, null=True, help_text='')
    OSI_approved =      models.BooleanField(blank=True, null=True, help_text='Is the OSI license approved?')
    GPL_compatible =    models.BooleanField(blank=True, null=True, help_text='Is it compatible with GPL?')
    copyleft =          models.BooleanField(blank=True, null=True, default=True, help_text='Is Copyleft a license?')
    different_license = models.BooleanField(blank=True, null=True, help_text='Allows linking with code under a different license.')
    active =            models.BooleanField(default=True, help_text='Check')

    class Meta:
        ordering = ['license_name']

    # def get_absolute_url(self):
    #     return reverse('Licence-detail', args=[str(self.id)])

    def __str__(self):
        return self.license_name
