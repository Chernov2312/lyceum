from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models

from catalog.validators import ValidateMustContain
from core.models import NamedBaseModel, PublishedBaseModel, SluggedBaseModel


class Tag(NamedBaseModel, PublishedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
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
        verbose_name='вес',
        help_text='Вес категории от 1 до 32767',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['weight', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Item(PublishedBaseModel, NamedBaseModel):
    text = models.TextField(
        verbose_name='текст',
        validators=[ValidateMustContain(['роскошно', 'превосходно'])],
        help_text='Обязательно должно содержать слова "превосходно"'
        'или "роскошно"',
    )
    category = models.ForeignKey(
        Category,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='items',
        verbose_name='Теги',
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
