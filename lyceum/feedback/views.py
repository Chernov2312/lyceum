from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from feedback.forms import FeedbackForm

__all__ = ['feedback']


def feedback(request):
    temlate = 'feedback/feedback.html'
    context = {'form': FeedbackForm()}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['name'],
                form.cleaned_data['text'],
                'Django@example.com',
                [form.cleaned_data['mail']],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('feedback:feedback'))
    return render(request=request, template_name=temlate, context=context)
