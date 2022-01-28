from django.db import models


class Licenses(models.Model):
    license_name = models.CharField(max_length=30)
    copyright_holder = models.CharField(max_length=100)
    # product_name = models.CharField(max_length=30, help_text='Specify which software product is covered by the license.')
    guarantees = models.BooleanField(help_text='Is the license guaranteed?')
    DFSG_compatible = models.BooleanField(help_text='The Debian Free Software Guidelines (DFSG) is a set of guidelines that the Debian Project uses to determine whether a software license is a free software license, which in turn is used to determine whether a piece of software can be included in Debian.')
    FSF_approved = models.BooleanField(help_text='Free software is computer software distributed under terms that allow users to run the software for any purpose as well as to study, change, and distribute it and any adapted versions.')
    OSI_approved = models.BooleanField(help_text='Is the OSI license approved?')
    GPL_approved = models.BooleanField(help_text='Is it compatible with GPL?')
    copyleft = models.BooleanField(help_text='Is Copyleft a license?')
    linking_from_different_license = models.BooleanField(help_text='Allows linking with code under a different license.')

    class Meta:
        ordering = ['license_name']
