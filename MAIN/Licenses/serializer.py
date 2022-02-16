from rest_framework import serializers
from Licenses.models import Licenses


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenses
        fields = '__all__'


class LicenseSerializerV2(serializers.Serializer):
    license_name = serializers.CharField(max_length=120)
    guarantee = serializers.BooleanField()
    DFSG_compatible = serializers.BooleanField()
    FSF_approved = serializers.BooleanField()
    OSI_approved = serializers.BooleanField()
    GPL_compatible = serializers.BooleanField()
    copyleft = serializers.BooleanField()
    different_license = serializers.BooleanField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Licenses.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.license_name = validated_data.get('license_name', instance.license_name)
        instance.guarantee = validated_data.get('guarantee', instance.guarantee)
        instance.DFSG_compatible = validated_data.get('DFSG_compatible', instance.DFSG_compatible)
        instance.FSF_approved = validated_data.get('FSF_approved', instance.FSF_approved)
        instance.OSI_approved = validated_data.get('OSI_approved', instance.OSI_approved)
        instance.GPL_compatible = validated_data.get('GPL_compatible', instance.GPL_compatible)
        instance.copyleft = validated_data.get('copyleft', instance.copyleft)
        instance.different_license = validated_data.get('different_license', instance.different_license)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    class Meta:
        model = Licenses
        fields = '__all__'
