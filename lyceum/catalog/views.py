import django.http


def item_list(request):
    return django.http.HttpResponse(
        'Список элементов', content_type='text/plain'
    )


def item_detail(request, item):
    return django.http.HttpResponse(
        'Подробно элемент', content_type='text/plain'
    )


def get_int_endpoint(request, id):
    return django.http.HttpResponse(f'{id}', content_type='text/plain')
