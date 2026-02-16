from django.db import models

from core.validators import (
    validate_slug,
)


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='опубликовано',
    )

    class Meta:
        abstract = True


class NamedBaseModel(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='название',
        db_index=True,
        help_text='Название до 150 символов',
    )

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.CharField(
        max_length=200,
        unique=True,
        validators=[validate_slug],
        verbose_name='слаг',
        help_text='Только латиница, цифры, дефис и подчеркивание',
    )

    class Meta:
        abstract = True
