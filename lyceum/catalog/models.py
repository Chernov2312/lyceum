from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Prefetch
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field

from catalog.validators import ValidateMustContain
from core.models import BaseImageModel, NamedBaseModel, PublishedBaseModel
from core.unic_field import Normalise

__all__ = ['Tag', 'Category', 'Item', 'Image', 'MainImage']


def get_image_upload_path(instance, filename):
    if hasattr(instance, 'items') and instance.items.exists():
        item = instance.items.first()
        return f'uploads/item_{item.id}/{filename}'
    return f'uploads/temp/{filename}'


def get_main_image_upload_path(instance, filename):
    if hasattr(instance, 'main_item') and instance.main_item.exists():
        item = instance.main_item.first()
        return f'main/item_{item.id}/{filename}'
    return f'main/temp/{filename}'


class ItemManager(models.Manager):
    def published_items(self):
        return (
            self.get_queryset()
            .select_related(
                'category',
                'main_image',
            )
            .prefetch_related(
                Prefetch('tags', queryset=Tag.objects.only('name')),
                Prefetch(
                    'images',
                    queryset=Image.objects.only('image'),
                ),
            )
            .order_by('category__name', 'name')
            .only('name', 'text', 'main_image__main_image', 'category__name')
            .filter(
                is_published=True,
                category__is_published=True,
            )
        )

    def main_items(self):
        return (
            self.get_queryset()
            .select_related(
                'category',
                'main_image',
            )
            .prefetch_related(
                Prefetch('tags', queryset=Tag.objects.only('name')),
            )
            .only('name', 'text', 'main_image__main_image', 'category__name')
            .order_by('name')
            .filter(is_on_main=True)
        )

    def get_object_or_404(self, item_id):
        return (
            self.get_queryset()
            .select_related(
                'main_image',
                'category',
            )
            .prefetch_related(
                Prefetch('tags', queryset=Tag.objects.only('name')),
                Prefetch(
                    'images',
                    queryset=Image.objects.only('image'),
                ),
            )
            .only('name', 'text', 'main_image__main_image', 'category__name')
            .filter(
                is_published=True,
                category__is_published=True,
            )
            .filter(id=item_id)
            .first()
        )


class Tag(NamedBaseModel, PublishedBaseModel):
    slug = models.SlugField(
        verbose_name='слаг',
        max_length=200,
        unique=True,
        help_text='Только латиница, цифры, дефис и подчеркивание',
    )
    normalised_name = models.CharField(
        max_length=150,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name='нормализованное название',
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self):
        self.normalised_name = Normalise.normalise(self.name)

    def save(self, *args, **kwargs):
        self.normalised_name = Normalise.normalise(self.name)
        self.full_clean()
        super().save(*args, **kwargs)

    def _save_table(self, *args, **kwargs):
        self.normalised_name = Normalise.normalise(self.name)
        return super()._save_table(*args, **kwargs)


class Category(PublishedBaseModel, NamedBaseModel):
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
    normalised_name = models.CharField(
        max_length=150,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name='нормализованное название',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['weight', 'name']

    def __str__(self):
        return self.name

    def clean(self):
        self.normalised_name = Normalise.normalise(self.name)

    def save(self, *args, **kwargs):
        self.normalised_name = Normalise.normalise(self.name)
        self.full_clean()
        super().save(*args, **kwargs)

    def _save_table(self, *args, **kwargs):
        self.normalised_name = Normalise.normalise(self.name)
        return super()._save_table(*args, **kwargs)


class Image(BaseImageModel):
    image = models.ImageField(
        upload_to=get_image_upload_path,
        verbose_name='изображение',
    )

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return f'Изображение #{self.id}'


class MainImage(BaseImageModel):
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

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']

    def get_all_images_tmb(self):
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

    get_all_images_tmb.short_description = 'Галерея'

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
