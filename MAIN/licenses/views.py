from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from licenses.models import Licenses
from django.core import serializers
from django.db import models


def index(request):
    num_books=serializers.serialize("json", Licenses.objects.all())

    return HttpResponse(num_books, content_type='application/json')


def health_check(request):
    data = list(Licenses.objects.values())
    return JsonResponse(data, safe=False)
