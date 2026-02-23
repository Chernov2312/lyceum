from django.shortcuts import render


__all__ = ['item_list', 'get_int_item_detail']


def item_list(request):
    template = 'catalog/item_list.html'
    context = {}
    return render(request=request, template_name=template, context=context)


def get_int_item_detail(request, item_id):
    template = 'catalog/item.html'
    context = {}
    return render(request=request, template_name=template, context=context)
