from http import HTTPStatus

import django.http


def item_list(request):
    return django.http.HttpResponse(
        'Список элементов', content_type='text/plain; charset=utf-8'
    )


def item_detail(request, item):
    return django.http.HttpResponse(
        'Подробно элемент', content_type='text/plain; charset=utf-8'
    )


def get_int_endpoint(request, id):
    return django.http.HttpResponse(f'{id}', content_type='text/plain; charset=utf-8')


def get_int_converter_endpoint(request, id):
    if id > 0:
        return django.http.HttpResponse(f'{id}', content_type='text/plain; charset=utf-8')
    return django.http.HttpResponse(status=HTTPStatus.NOT_FOUND)
