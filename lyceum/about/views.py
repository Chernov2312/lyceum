from django.shortcuts import render


def description(request):
    template = 'about/about.html'
    context = {}
    return render(request=request, template_name=template, context=context)
