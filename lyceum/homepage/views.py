import django.http


def home(request):
    return django.http.HttpResponse('Главная')
