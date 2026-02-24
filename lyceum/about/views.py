from django.http import HttpResponse

__all__ = ['description']


def description(request):
    return HttpResponse(
        'О проекте',
        content_type='text/html; charset=utf-8',
    )