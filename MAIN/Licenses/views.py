from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from Licenses.models import Licenses
from django.shortcuts import render
from requirements_analysis import requirements_analyser

licenses_serializer = {
    'license_name': {'required': True, 'read only': False},
    'guarantee': {'required': False, 'read only': False},
    'DFSG_compatible': {'required': True, 'read only': False},
    'FSF_approved': {'required': True, 'read only': False},
    'OSI_approved': {'required': True, 'read only': False},
    'GPL_compatible': {'required': True, 'read only': False},
    'copyleft': {'required': True, 'read only': False},
    'different_license': {'required': False, 'read only': False},
    'active': {'required': False, 'read only': True}
}


def serialize(license_serialize, data_dict, data_id):
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

    # from pprint import pprint
    # pprint(data, indent=4)

    end_list = dictionary_processing(data)
    return render(request, 'licenses.html',
                  context={'licenses_data': end_list})


def dictionary_processing(list_of_dictionaries):
    end_list = []
    for i in list_of_dictionaries:
        list_dot = []
        for key in i:
            end_dict = {'name': key, 'value': i[key]}
            list_dot.append(end_dict)
        end_list.append(list_dot)
    return end_list


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
    return render(request, 'license_info.html',
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
    # license_id.delete()
    license_id.active = False
    license_id.save()
    return HttpResponse('DEL')


def create_licenses(request):
    if request.method == 'POST':
        try:
            data = dict(request.POST)
            a = serialize(licenses_serializer, data, None)
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
        return get_license(request, data_id)
    elif request.method == 'POST':
        return update_license(request, data_id)
    elif request.method == 'DELETE':
        return delete_license(request, data_id)
    else:
        return HttpResponse('Error')


def license_comparison(request):
    json_list = requirements_analyser('/home/clifford/PycharmProjects/License Manager/requirements.txt')
    data = [model_to_dict(obj) for obj in Licenses.objects.all()]
    final_licenses_list = []
    not_in_db = []
    for license_dict in json_list:
        for license_data in data:
            if license_dict['License'] in license_data['license_name']:
                final_licenses_list.append(license_dict['License'])
                if license_dict['License'] in not_in_db:
                    not_in_db.remove(license_dict['License'])
                break
            elif license_dict['License'] not in final_licenses_list and license_dict['License'] not in not_in_db:
                not_in_db.append(license_dict['License'])
            else:
                print('Nope')

    return HttpResponse(f'{final_licenses_list=}\n{not_in_db=}')
