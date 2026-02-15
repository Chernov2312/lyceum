from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models

from catalog.validators import validate_words_in_text
from core.models import NamedBaseModel, PublishedBaseModel, SluggedBaseModel


class Tag(PublishedBaseModel, NamedBaseModel, SluggedBaseModel):
    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='id',
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(PublishedBaseModel, NamedBaseModel, SluggedBaseModel):
    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='id',
    )
    weight = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(32767)],
        default=100,
        verbose_name='Вес',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['weight', 'name']

    def __str__(self):
        return self.name


class Item(PublishedBaseModel, NamedBaseModel):
    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='id',
    )
    text = models.TextField(
        verbose_name='Текст',
        validators=[validate_words_in_text],
        help_text='Обязательно должно содержать'
        'слова "превосходно" или "роскошно"',
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
        verbose_name='Тэг',
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']

    def __str__(self):
        return self.name
