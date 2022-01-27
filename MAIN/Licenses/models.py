from django.db import models


class Licenses(models.Model):
    license_name = models.CharField(max_length=30)
    copyright_holder = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)
    guarantees = models.CharField(max_length=30)

