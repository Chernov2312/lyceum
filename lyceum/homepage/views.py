from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import catalog.models
from homepage.forms import EchoForm

__all__ = ['home', 'coffee', 'echo', 'echo_submit']


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


def echo(request):
    temlate = 'homepage/echo.html'
    context = {'form': EchoForm()}
    return render(request=request, template_name=temlate, context=context)


@require_POST
@csrf_exempt
def echo_submit(request):
    return HttpResponse(
        request.POST.get('text', ''),
        content_type='text/plain; charset=utf-8',
        status=HTTPStatus.OK,
    )
