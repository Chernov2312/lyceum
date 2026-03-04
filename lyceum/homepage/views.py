from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render

import catalog.models

__all__ = ['home', 'coffee']


def home(request):
    template = 'homepage/main.html'
    context = {
        'items': catalog.models.Item.objects.on_main(),
    }
    return render(request=request, template_name=template, context=context)


def coffee(request):
    return HttpResponse(
        'Я чайник',
        content_type='text/html; charset=utf-8',
        status=HTTPStatus.IM_A_TEAPOT,
    )
