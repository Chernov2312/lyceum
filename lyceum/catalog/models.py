from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field

from catalog.manager import ItemManager
from catalog.utils import get_image_upload_path, get_main_image_upload_path
from catalog.validators import ValidateMustContain
from core.models import (
    ImageBaseModel,
    NamedBaseModel,
    NormiliseBaseModel,
    PublishedBaseModel,
)

__all__ = ['Tag', 'Category', 'Item', 'Image', 'MainImage']


class Tag(NamedBaseModel, PublishedBaseModel, NormiliseBaseModel):
    slug = models.SlugField(
        verbose_name='слаг',
        max_length=200,
        unique=True,
        help_text='Только латиница, цифры, дефис и подчеркивание',
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(PublishedBaseModel, NamedBaseModel, NormiliseBaseModel):
    slug = models.SlugField(
        verbose_name='слаг',
        max_length=200,
        unique=True,
        help_text='Только латиница, цифры, дефис и подчеркивание',
    )
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


class Image(ImageBaseModel):
    image = models.ImageField(
        upload_to=get_image_upload_path,
        verbose_name='изображение',
    )

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return f'Изображение #{self.id}'


class MainImage(ImageBaseModel):
    main_image = models.ImageField(
        upload_to=get_main_image_upload_path,
        verbose_name='главное изображение',
    )

    class Meta:
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'

    def __str__(self):
        return f'Изображение #{self.id}'


class Item(PublishedBaseModel, NamedBaseModel):
    objects = ItemManager()
    text = CKEditor5Field(
        verbose_name='текст',
        validators=[ValidateMustContain('роскошно', 'превосходно')],
        config_name='default',
        help_text='Обязательно должно содержать слова'
        '"превосходно" или "роскошно"',
    )
    is_on_main = models.BooleanField(
        verbose_name='на главной',
        default=False,
    )
    category = models.ForeignKey(
        Category,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='категория',
        db_index=True,
        related_query_name='item',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='items',
        verbose_name='теги',
        blank=True,
        related_query_name='item',
    )
    main_image = models.ForeignKey(
        MainImage,
        related_name='main_item',
        on_delete=models.SET_NULL,
        verbose_name='главное изображение',
        null=True,
        blank=True,
        help_text='Выберите главное изображение товара',
    )
    images = models.ManyToManyField(
        Image,
        related_name='items',
        verbose_name='дополнительные изображения',
        blank=True,
        help_text='Выберите дополнительные изображения для галереи',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания',
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='дата обновления',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']

    def get_all_images_tmb(
        self,
    ):  # код для вывода доп картинок в каталоге конфликтует с тестами лмс
        # которые требуют простого вызова all а не функции
        # он тут так же как get_image_tmb в методе core
        # только он вызывается только для item
        images = self.images.all()
        if images:
            html = '<div style="display: flex; flex-wrap: wrap; gap: 5px;">'
            for img in images[:5]:
                html += f'<img src="{img.image.url}" width="40" height="40">'
            if images.count() > 5:
                html += (
                    f'<span style="padding: 8px;">+{images.count() - 5}</span>'
                )
            html += '</div>'
            return mark_safe(html)
        return 'Нет дополнительных изображений'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __repr__(self):
        return (
            f'Item(name={self.name}, '
            f'category={self.category}, '
            f'tags={self.tags}, '
            f'main_image={self.main_image})'
        )
