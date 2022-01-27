from django.db import models


class Licenses(models.Model):
    license_name = models.CharField(max_length=30, help_text='Enter License name')
    copyright_holder = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)
    guarantees = models.CharField(max_length=30)

    class Meta:
        ordering = ['license_name']

    def __str__(self):
        return self.field_names


