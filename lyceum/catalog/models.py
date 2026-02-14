from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    ValidationError,
    validate_unicode_slug,
)
from django.db import models

from .validators import validate_words_in_text


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField(default=True, name='Опубликовано')

    class Meta:
        abstract = True


class Tag(PublishedBaseModel):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, verbose_name='id'
    )
    name = models.CharField(max_length=150, name='Название')
    slug = models.CharField(
        max_length=200,
        unique=True,
        validators=[validate_unicode_slug],
        name='Слаг',
    )
    
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    def __str__(self):
        return self.name
    def clean(self):
        if self.pk and self.pk <= 0:
            raise ValidationError({'id': 'id должен быть больше нуля'})


class Category(PublishedBaseModel):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, verbose_name='id'
    )
    name = models.CharField(max_length=150, name='Название')
    slug = models.CharField(
        max_length=200,
        unique=True,
        validators=[validate_unicode_slug],
        name='Слаг',
    )
    weight = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(32767)],
        default=100,
        name='Вес',
    )
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

    def clean(self):
        if self.pk and self.pk <= 0:
            raise ValidationError({'id': 'id должен быть больше нуля'})


class Item(PublishedBaseModel):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, verbose_name='id'
    )
    name = models.CharField(max_length=150, name='Название')
    text = models.TextField(name='Текст', validators=[validate_words_in_text])
    category = models.OneToOneField(
        Category, related_name='category', on_delete=models.CASCADE
    )
    tags = models.ForeignKey(
        Tag, on_delete=models.SET_NULL, related_name='tag'
    )
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return self.name

    def clean(self):
        if self.pk and self.pk <= 0:
            raise ValidationError({'id': 'id должен быть больше нуля'})
