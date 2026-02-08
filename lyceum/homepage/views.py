import django.http


def home(request):
    return django.http.HttpResponse('<body>Главная</body>')


def coffee(request):
    return django.http.HttpResponse('<body>Я чайник</body>', status=418)
