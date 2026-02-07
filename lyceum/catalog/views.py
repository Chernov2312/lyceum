import django.http


def item_list(request):
    return django.http.HttpResponse('Список элементов')


def item_detail(request, item):
    return django.http.HttpResponse('Подробно элемент')
