from http import HTTPStatus

from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render

import catalog.models

__all__ = ['home', 'coffee']


def home(request):
    template = 'homepage/main.html'
    context = {
        'items': catalog.models.Item.objects.select_related(
            'category',
            'main_image',
        )
        .prefetch_related(
            Prefetch('tags', queryset=catalog.models.Tag.objects.only('name')),
        )
        .only('name', 'text', 'main_image__main_image', 'category__name')
        .order_by('name')
        .filter(is_on_main=True),
    }
    return render(request=request, template_name=template, context=context)


def coffee(request):
    return HttpResponse(
        'Я чайник',
        content_type='text/html; charset=utf-8',
        status=HTTPStatus.IM_A_TEAPOT,
    )
