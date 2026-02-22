import django.http


def item_list(request):
    return django.http.HttpResponse(
        'Список элементов',
        content_type='text/plain; charset=utf-8',
    )


def get_int_item_detail(request, item_id: int):
    return django.http.HttpResponse(
        f'Подробно элемент {item_id}',
        content_type='text/plain; charset=utf-8',
    )
