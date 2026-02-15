from core.validators import (
    validate_name,
    validate_slug,
)

from django.db import models


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
    )

    class Meta:
        abstract = True


class NamedBaseModel(models.Model):
    name = models.CharField(
        max_length=150, validators=[validate_name], verbose_name='Название',
    )

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.CharField(
        max_length=200,
        unique=True,
        validators=[validate_slug],
        verbose_name='Слаг',
        help_text='Только латиница, цифры, дефис и подчеркивание',
    )

    class Meta:
        abstract = True
