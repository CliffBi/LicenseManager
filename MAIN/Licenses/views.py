from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from Licenses.models import Licenses
from django.core import serializers
from rest_framework.decorators import api_view


def index(request):
    num_books = serializers.serialize("json", Licenses.objects.all())

    return HttpResponse(num_books, content_type='application/json')


def get_list_licenses(request):
    # data = list(Licenses.objects.values())
    # data = []
    # for obj in Licenses.objects.all():
    #     data.append(model_to_dict(obj))

    data = [model_to_dict(obj) for obj in Licenses.objects.all()]
    return JsonResponse(data, safe=False)


@csrf_exempt
def check_lic(request, data_id):
    if request.method == 'GET':
        try:
            lic_obj = Licenses.objects.get(id=data_id)
        except Licenses.DoesNotExist as e:
            print(type(e))
            return HttpResponse('No Data', status=204)

        data = model_to_dict(lic_obj)
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data1 = Licenses.objects.get(id=2)
        return HttpResponse(data1)


@api_view(['POST'])
@csrf_exempt
def data_updater(request, data_id):
    if request.method == 'POST':
        try:
            license_id = Licenses.objects.get(id=data_id)
        except Licenses.DoesNotExist as e:
            print(type(e))
            return HttpResponse('No Data', status=204)
        request_data = request.data['license_name']
        license_id.license_name = request_data
        license_id.save()
        return HttpResponse('ok')


def serialize(names_list, data_dict):
    output_dict = dict()
    for name in names_list:
        output_dict[name] = data_dict[name][0]
    print(output_dict)
    return output_dict


@csrf_exempt
def data_create(request):
    if request.method == 'POST':
        try:
            data = dict(request.POST)
            names_list = ('license_name', 'guarantee', 'DFSG_compatible',
                          'FSF_approved', 'OSI_approved', 'GPL_compatible', 'copyleft',
                          'different_license', 'active')
            a = serialize(names_list, data)
        except KeyError as e:
            print(type(e))
            return HttpResponse('No Data', status=204)
        # Licenses.objects.create(**a)
        return HttpResponse('ok')


@csrf_exempt
def data_delete(request, data_id):
    if request.method == 'DELETE':
        try:
            license_id = Licenses.objects.get(id=data_id)
            license_id.delete()
        except Licenses.DoesNotExist as e:
            print(type(e))
            return HttpResponse('No Data', status=204)
        return HttpResponse('DEL')

