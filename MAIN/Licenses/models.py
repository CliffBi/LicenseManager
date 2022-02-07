from django.db import models


class Licenses(models.Model):
    license_name = models.CharField(max_length=30)
    # copyright_holder = models.CharField(max_length=100)
    guarantee = models.BooleanField(help_text='Is the license guaranteed?', blank=True, null=True)
    DFSG_compatible = models.BooleanField(help_text='')
    FSF_approved = models.BooleanField(help_text='')
    OSI_approved = models.BooleanField(help_text='Is the OSI license approved?')
    GPL_compatible = models.BooleanField(help_text='Is it compatible with GPL?')
    copyleft = models.BooleanField(help_text='Is Copyleft a license?', default=True)
    different_license = models.BooleanField(help_text='Allows linking with code under a different license.')
    active = models.BooleanField(help_text='Check', default=True)

    class Meta:
        ordering = ['license_name']

    # def get_absolute_url(self):
    #     return reverse('Licence-detail', args=[str(self.id)])

    def __str__(self):
        return self.license_name
