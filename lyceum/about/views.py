import django.http


def description(request):
    return django.http.HttpResponse(
        'О проекте',
        content_type='text/plain; charset=utf-8',
    )
