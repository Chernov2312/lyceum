from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from catalog.validators import ValidateMustContain
from core.models import NamedBaseModel, PublishedBaseModel, SluggedBaseModel


class Tag(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = _('тег')
        verbose_name_plural = _('теги')
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Category(PublishedBaseModel, NamedBaseModel, SluggedBaseModel):
    weight = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(32767)],
        default=100,
        verbose_name=_('вес'),
        help_text=_('Вес категории от 1 до 32767'),
    )

    class Meta:
        verbose_name = _('категория')
        verbose_name_plural = _('категории')
        ordering = ['weight', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Item(PublishedBaseModel, NamedBaseModel):
    text = models.TextField(
        verbose_name=_('текст'),
        validators=[ValidateMustContain(['роскошно', 'превосходно'])],
        help_text=_(
            'Обязательно должно содержать слова "превосходно" или "роскошно"',
        ),
    )
    category = models.ForeignKey(
        Category,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name=_('Категория'),
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='items',
        verbose_name=_('Теги'),
    )

    class Meta:
        verbose_name = _('товар')
        verbose_name_plural = _('товары')
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
