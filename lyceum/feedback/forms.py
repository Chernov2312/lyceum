import django.forms

from feedback.models import Feedback

__all__ = ['FeedbackForm']


class FeedbackForm(django.forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'mail', 'text']
        widgets = {
            'text': django.forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'name': 'Ваше имя',
            'mail': 'Email для ответа',
            'text': 'Сообщение',
        }
        help_texts = {
            'name': 'Введите ваше имя',
            'mail': 'Укажите действующий email',
            'text': 'Напишите ваше сообщение',
        }
