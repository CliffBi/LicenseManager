from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from Licenses.models import Licenses
from rest_framework import generics, viewsets
from Licenses.serializer import LicenseSerializer, LicenseSerializerV2


class CreateLicense(generics.ListCreateAPIView):
    queryset = Licenses.objects.all()
    serializer_class = LicenseSerializer


# class GetLicense(generics.RetrieveAPIView):
#     queryset = Licenses.objects.all()
#     serializer_class = LicenseSerializer

class GetUpdateDeleteLicense(generics.RetrieveUpdateDestroyAPIView):
    queryset = Licenses.objects.all()
    serializer_class = LicenseSerializer


class LicenseView(viewsets.ViewSet):

    def list(self, request):
        queryset = Licenses.objects.all()
        serializer_class = LicenseSerializerV2(queryset)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = Licenses.objects.all()
        license_pk = get_object_or_404(queryset, pk=pk)
        serializer = LicenseSerializerV2(license_pk)
        return Response(serializer.data)


class LicenseViewSet(viewsets.ModelViewSet):

    serializer_class = LicenseSerializerV2
    queryset = Licenses.objects.all()
