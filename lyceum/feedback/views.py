from django.shortcuts import render

__all__ = ['feedback']


def feedback(request):
    temlate = 'feedback/feedback.html'
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        print(name)
    return render(request=request, template_name=temlate, context=context)
