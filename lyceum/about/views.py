import django.http


def description():
    return django.http.HttpResponse('<body>О проекте</body>')