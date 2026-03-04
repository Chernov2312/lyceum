from http import HTTPStatus

from django.shortcuts import render

import catalog.models

__all__ = ['item_list', 'get_int_item_detail']


def item_list(request):
    template = 'catalog/item_list.html'
    context = {
        'items': catalog.models.Item.objects.published_items(),
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
