import django.http


def item_list(request):
    return django.http.HttpResponse('<body>Список элементов</body>')


def item_detail(request, item):
    return django.http.HttpResponse('<body>Подробно элемент</body>')


def get_int_endpoint(request, id):
    return django.http.HttpResponse(f'<body>{id}</body>')

