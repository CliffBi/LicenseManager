from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from Licenses.models import Licenses
from django.core import serializers
from rest_framework import generics, viewsets
from rest_framework.response import Response
from Licenses.serializer import LicenseSerializer
from django.shortcuts import render


class GetCreateUpdateDelete:
    licenses_serializer = {
        'license_name':         {'required': True, 'read only': False},
        'guarantee':            {'required': False, 'read only': False},
        'DFSG_compatible':      {'required': True, 'read only': False},
        'FSF_approved':         {'required': True, 'read only': False},
        'OSI_approved':         {'required': True, 'read only': False},
        'GPL_compatible':       {'required': True, 'read only': False},
        'copyleft':             {'required': True, 'read only': False},
        'different_license':    {'required': False, 'read only': False},
        'active':               {'required': False, 'read only': True}
    }

    def serialize(self, license_serialize, data_dict, data_id):
        output_dict = dict()
        for name in license_serialize:
            if name not in data_dict:
                if (not data_id) and license_serialize[name]['required']:  # for create_license
                    raise Exception(f'No field {name=}')
                else:  # for update_license
                    pass
            elif license_serialize[name]['read only']:
                continue
            else:
                output_dict[name] = data_dict[name][0]
        print(output_dict)
        return output_dict

    def index(request):
        # num_books = serializers.serialize("json", Licenses.objects.all())
        # a = HttpResponse(num_books, content_type='application/json')
        #
        data = [model_to_dict(obj) for obj in Licenses.objects.all()]
        # return JsonResponse(data, safe=False)
        return render (request, 'index.html',
                       context={'id':data[0]['id'],
                                'license_name':data[0]['license_name'],
                                'guarantee':data[0]['guarantee'],
                                'DFSG_compatible':data[0]['DFSG_compatible'],
                                'FSF_approved':data[0]['FSF_approved'],
                                'OSI_approved':data[0]['OSI_approved'],
                                'GPL_compatible':data[0]['GPL_compatible'],
                                'copyleft':data[0]['copyleft'],
                                'different_license':data[0]['different_license'],
                                'active':data[0]['active'],
                                })

    def get_list_licenses(request):
        # data = list(Licenses.objects.values())
        # data = []
        # for obj in Licenses.objects.all():
        #     data.append(model_to_dict(obj))

        data = [model_to_dict(obj) for obj in Licenses.objects.all()]
        return JsonResponse(data, safe=False)

    def get_license(request, data_id):
        try:
            license_object = Licenses.objects.get(id=data_id)
        except Licenses.DoesNotExist as e:
            print(type(e))
            return HttpResponse('No Data', status=204)

        data = model_to_dict(license_object)
        # return JsonResponse(data, safe=False)
        return render(request, 'get_license.html',
                      context={'id': data['id'],
                               'license_name': data['license_name'],
                               'guarantee': data['guarantee'],
                               'DFSG_compatible': data['DFSG_compatible'],
                               'FSF_approved': data['FSF_approved'],
                               'OSI_approved': data['OSI_approved'],
                               'GPL_compatible': data['GPL_compatible'],
                               'copyleft': data['copyleft'],
                               'different_license': data['different_license'],
                               'active': data['active'],
                               })

    def update_license(request, data_id, self=None):
        try:
            # license_id = Licenses.objects.get(id=data_id)
            data = dict(request.POST)
            a = GetCreateUpdateDelete.serialize(self, GetCreateUpdateDelete.licenses_serializer, data, data_id)
        except Licenses.DoesNotExist as e:
            print(type(e))
            return HttpResponse('No Data', status=204)
        Licenses.objects.filter(id=data_id).update(**a)
        # request_data = request.POST['license_name']
        # license_id.license_name = request_data
        # license_id.save()
        return HttpResponse('ok')

    def delete_license(request, data_id):
        try:
            license_id = Licenses.objects.get(id=data_id)
        except Licenses.DoesNotExist as e:
            print(type(e))
            return HttpResponse('No Data', status=204)
        # license_id.delete()
        license_id.active = False
        license_id.save()
        return HttpResponse('DEL')

    def create_licenses(request, self=None):
        if request.method == 'POST':
            try:
                data = dict(request.POST)
                a = GetCreateUpdateDelete.serialize(self, GetCreateUpdateDelete.licenses_serializer, data, None)
            except KeyError as e:
                print(type(e))
                return HttpResponse('No Data', status=204)
            if a is None:
                return HttpResponse('More info')
            else:
                # Licenses.objects.create(**a)
                return HttpResponse('ok')

    def get_update_delete_license(request, data_id):
        if request.method == 'GET':
            return GetCreateUpdateDelete.get_license(request, data_id)
        elif request.method == 'POST':
            return GetCreateUpdateDelete.update_license(request, data_id)
        elif request.method == 'DELETE':
            return GetCreateUpdateDelete.delete_license(request, data_id)
        else:
            return HttpResponse('Error')


class DrfGetUpdateCreateDelete:
    class CreateLicense(generics.ListCreateAPIView):
        queryset = Licenses.objects.all()
        serializer_class = LicenseSerializer

    # class GetLicense(generics.RetrieveAPIView):
    #     queryset = Licenses.objects.all()
    #     serializer_class = LicenseSerializer

    class GetUpdateDeleteLicense(generics.RetrieveUpdateDestroyAPIView):
        queryset = Licenses.objects.all()
        serializer_class = LicenseSerializer
