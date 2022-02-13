from rest_framework import serializers
from Licenses.models import Licenses


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenses
        fields = '__all__'
