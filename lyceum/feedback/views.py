from django.shortcuts import render

__all__ = ['feedback']


def feedback(request):
    temlate = 'feedback/feedback.html'
    context = {}
    return render(request=request, template_name=temlate, context=context)
