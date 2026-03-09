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
