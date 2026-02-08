from http import HTTPStatus

import django.http
from django.http import HttpResponse


def home(request):
    return django.http.HttpResponse(
        'Главная', content_type='text/plain; charset=utf-8'
    )


def coffee(request):
    return HttpResponse(
        'Я чайник',
        content_type='text/plain; charset=utf-8',
        status=HTTPStatus.IM_A_TEAPOT,
    )
