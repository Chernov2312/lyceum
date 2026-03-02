from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item
__all__ = ['home', 'coffee']


def home(request):
    template = 'homepage/main.html'
    items = Item.objects.filter(is_on_main=True)
    context = {'items': items}
    return render(request=request, template_name=template, context=context)


def coffee(request):
    return HttpResponse(
        'Я чайник',
        content_type='text/html; charset=utf-8',
        status=HTTPStatus.IM_A_TEAPOT,
    )
