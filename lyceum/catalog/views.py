from http import HTTPStatus
import os

from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render

import catalog.models
__all__ = ['item_list', 'get_int_item_detail']


def item_list(request):
    template = 'catalog/item_list.html'
    context = {
        'items': catalog.models.Item.objects.published(),
    }
    return render(request=request, template_name=template, context=context)


def get_int_item_detail(request, item_id):
    template = 'catalog/item.html'
    context = {
        'item': catalog.models.Item.objects.get_object_or_404(item_id),
    }
    if context['item'] is None:
        return render(
            request=request,
            template_name=template,
            context=context,
            status=HTTPStatus.NOT_FOUND,
        )
    return render(request=request, template_name=template, context=context)


def new(request):
    template = 'catalog/item_list.html'
    context = {
        'items': catalog.models.Item.objects.new(),
    }
    return render(request=request, template_name=template, context=context)


def friday(request):
    template = 'catalog/item_list.html'
    context = {
        'items': catalog.models.Item.objects.friday(),
    }
    return render(request=request, template_name=template, context=context)


def unverified(request):
    template = 'catalog/item_list.html'
    context = {
        'items': catalog.models.Item.objects.unverified(),
    }
    return render(request=request, template_name=template, context=context)


def download(request, file_path):
    base_dir = settings.MEDIA_ROOT
    full_path = os.path.join(base_dir, file_path)
    if not os.path.exists(full_path):
        raise Http404('Файл не найден')
    return FileResponse(
        open(full_path, 'rb'),
        as_attachment=True,
        filename=os.path.basename(file_path),
    )
