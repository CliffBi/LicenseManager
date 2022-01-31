from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Licenses.models import Licenses
from django.views import View
from django.forms.models import model_to_dict
import json

def index(request):
    num_books=Licenses.objects.all()

    return HttpResponse(json.dumps(num_books), content_type = "application/json")


def health_check(request):
    return HttpResponse('ok')

