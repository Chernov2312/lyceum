from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from catalog.validators import ValidateMustContain
from core.models import NamedBaseModel, PublishedBaseModel
from core.unic_field import Normalise


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

    def save(self, *args, **kwargs):
        self.normalised_name = Normalise.normalise(self.name)
        self.full_clean()
        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        self.normalised_name = Normalise.normalise(self.name)
        self.full_clean()
        super().save(*args, **kwargs)


class Image(models.Model):
    image = models.ImageField(
        upload_to='uploads/',
        verbose_name='изображение',
    )

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return f'Изображение #{self.id}'

    def get_image_x1280(self):
        return get_thumbnail(self.image, '1280', quality=51)

    def get_image_300x300(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="50" height="50"'
                'style="object-fit: cover;">',
            )
        return 'Нет изображения'

    image_tmb.short_description = 'Превью'
    image_tmb.allow_tags = True


class MainImage(models.Model):
    main_image = models.ImageField(upload_to='main/')

    class Meta:
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'

    def __str__(self):
        return f'Изображение #{self.id}'

    def image_tmb(self):
        if self.main_image:
            return mark_safe(
                f'<img src="{self.main_image.url}" width="50" height="50"'
                'style="object-fit: cover;">',
            )
        return 'Нет изображения'


class Item(PublishedBaseModel, NamedBaseModel):
    text = models.TextField(
        verbose_name='текст',
        validators=[ValidateMustContain('роскошно', 'превосходно')],
        help_text='Обязательно должно содержать слова'
        '"превосходно" или "роскошно"',
    )
    category = models.ForeignKey(
        Category,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='категория',
        db_index=True,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='items',
        verbose_name='теги',
        blank=True,
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

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_main_image_tmb(self):
        if self.main_image:
            return self.main_image.image_tmb()
        return 'Нет главного изображения'

    get_main_image_tmb.short_description = 'Главное изображение'

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
