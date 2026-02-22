import django.http


def description(request):
    return django.http.HttpResponse(
        'О проекте',
        content_type='text/text; charset=utf-8',
    )
