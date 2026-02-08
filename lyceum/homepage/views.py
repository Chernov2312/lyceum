import django.http
from django.http import HttpResponse


def home(request):
    return django.http.HttpResponse('Главная', content_type='text/plain')


def coffee(request):
    return HttpResponse('Я чайник', content_type='text/plain', status=418)
