from django.shortcuts import render
from django.http import HttpResponse


def testpip(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('Привет!')

