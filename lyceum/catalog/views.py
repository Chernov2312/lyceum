from http import HTTPStatus

from django.db.models import Prefetch
from django.shortcuts import render

import catalog.models

__all__ = ['item_list', 'get_int_item_detail']


def item_list(request):
    template = 'catalog/item_list.html'
    context = {
        'items': catalog.models.Item.objects.select_related(
            'category',
            'main_image',
        )
        .prefetch_related(
            Prefetch('tags', queryset=catalog.models.Tag.objects.only('name')),
            Prefetch(
                'images',
                queryset=catalog.models.Image.objects.only('image'),
            ),
        )
        .order_by('name')
        .only('name', 'text', 'main_image__main_image', 'category__name')
        .filter(
            is_published=True,
            category__is_published=True,
        ),
    }
    return render(request=request, template_name=template, context=context)


def get_int_item_detail(request, item_id):
    template = 'catalog/item.html'
    context = {
        'item': catalog.models.Item.objects.select_related(
            'main_image',
            'category',
        )
        .prefetch_related(
            Prefetch('tags', queryset=catalog.models.Tag.objects.only('name')),
            Prefetch(
                'images',
                queryset=catalog.models.Image.objects.only('image'),
            ),
        )
        .only('name', 'text', 'main_image__main_image', 'category__name')
        .filter(
            is_published=True,
            category__is_published=True,
        )
        .filter(id=item_id)
        .first(),
    }
    if context['item'] is None:
        return render(
            request=request,
            template_name=template,
            context=context,
            status=HTTPStatus.NOT_FOUND,
        )
    return render(request=request, template_name=template, context=context)
