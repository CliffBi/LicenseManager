from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from Licenses.models import Licenses
from django.core import serializers


# licenses_serialize = ('license_name', 'guarantee', 'DFSG_compatible',
#                           'FSF_approved', 'OSI_approved', 'GPL_compatible', 'copyleft',
#                           'different_license', 'active')
licenses_serializer = {
    'license_name': 'name_license',
    'guarantee': False,
    'DFSG_compatible': False,
    'FSF_approved': False,
    'OSI_approved': False,
    'GPL_compatible': False,
    'copyleft': False,
    'different_license': False,
    'active': True
}


def serialize(license_serialize, data_dict, data_id):
    output_dict = dict()
    for name in license_serialize:
        if name not in data_dict:
            if data_id is None:          # for create_license
                output_dict[name] = license_serialize[name]
            else:                        # for update_license
                license_object = Licenses.objects.get(id=data_id)
                data = model_to_dict(license_object)
                output_dict[name] = data[name]
        else:
            output_dict[name] = data_dict[name][0]
    # if 'active' in data_dict:
    #     output_dict['active'] = data_dict['active'][0]
    print(output_dict)
    return output_dict


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


def get_license(request, data_id):
    try:
        license_object = Licenses.objects.get(id=data_id)
    except Licenses.DoesNotExist as e:
        print(type(e))
        return HttpResponse('No Data', status=204)

    data = model_to_dict(license_object)
    return JsonResponse(data, safe=False)


def update_license(request, data_id):
    try:
        # license_id = Licenses.objects.get(id=data_id)
        data = dict(request.POST)
        a = serialize(licenses_serializer, data, data_id)
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
    license_id.delete()
    return HttpResponse('DEL')


@csrf_exempt
def create_licenses(request):
    if request.method == 'POST':
        try:
            data = dict(request.POST)
            a = serialize(licenses_serializer, data, None)
        except KeyError as e:
            print(type(e))
            return HttpResponse('No Data', status=204)
        # Licenses.objects.create(**a)
        return HttpResponse('ok')


@csrf_exempt
def get_update_delete_license(request, data_id):
    if request.method == 'GET':
        return get_license(request, data_id)
    elif request.method == 'POST':
        return update_license(request, data_id)
    elif request.method == 'DELETE':
        return delete_license(request, data_id)
    else:
        return HttpResponse('Error')
