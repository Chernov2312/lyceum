from http import HTTPStatus

import django.http
from django.http import HttpResponse


def home(request):
    return django.http.HttpResponse(
        'Главная', content_type='text/plain; charset=utf-8'
    )


def coffee(request):
    from lyceum.settings import ALLOW_REVERSE
    if ALLOW_REVERSE:
        return HttpResponse(
            'Я чайник Я кинйач',
            content_type='text/plain; charset=utf-8',
            status=HTTPStatus.IM_A_TEAPOT,
        )
    return HttpResponse(
        'Я чайник',
        content_type='text/plain; charset=utf-8',
        status=HTTPStatus.IM_A_TEAPOT,
    )
