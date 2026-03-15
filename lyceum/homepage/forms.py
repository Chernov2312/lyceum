from django import forms

__all__ = ['EchoForm']


class EchoForm(forms.Form):
    text = forms.CharField(
        label='Введите текст',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Напишите что-нибудь',
            },
        ),
    )
