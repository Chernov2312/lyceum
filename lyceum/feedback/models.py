from django.db import models

from core.models import NamedBaseModel

__all__ = ['Feedback']


class Feedback(NamedBaseModel):
    text = models.TextField()
    mail = models.EmailField(verbose_name='маил')
    created_on = models.TimeField(
        auto_now_add=True,
        verbose_name='дата создания',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_on']
