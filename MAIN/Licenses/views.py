from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from Licenses.models import Licenses
from django.core import serializers
from django.db import models


def index(request):
    num_books=serializers.serialize("json", Licenses.objects.all())

    return HttpResponse(num_books, content_type='application/json')


def get_list_licenses(request):
    # data = list(Licenses.objects.values())
    # data = []
    # for obj in Licenses.objects.all():
    #     data.append(model_to_dict(obj))

    data = [model_to_dict(obj) for obj in Licenses.objects.all()]
    return JsonResponse(data, safe=False)


@csrf_exempt
def check_lic(request, id):
    if request.method == 'GET':
        try:
            lic_obj = Licenses.objects.get(id=id)
        except Licenses.DoesNotExist as e:
            print(type(e))
            return HttpResponse('No Data', status=204)

        data = model_to_dict(lic_obj)
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data1 = Licenses.objects.get(id=2)
        return HttpResponse(data1)


