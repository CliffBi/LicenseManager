from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Licenses.models import Licenses
from django.core import serializers
from django.db import models


def index(request):
    num_books=serializers.serialize("json", Licenses.objects.all())

    return HttpResponse(num_books, content_type='application/json')


def health_check(request):
    data = list(Licenses.objects.values())
    return JsonResponse(data, safe=False)


@csrf_exempt
def check_lic(request):
    if request.method == 'GET':
        data = list(Licenses.objects.values())
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        return HttpResponse('POST1')
