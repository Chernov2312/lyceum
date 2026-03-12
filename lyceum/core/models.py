from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from core.unic_field import Normalise

__all__ = [
    'PublishedBaseModel',
    'NamedBaseModel',
    'ImageBaseModel',
    'NormiliseBaseModel',
]


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
        unique=True,
        blank=False,
        help_text='Название до 150 символов',
    )

    class Meta:
        abstract = True


class ImageBaseModel(models.Model):
    class Meta:
        abstract = True

    def get_image_x1280(self):
        thumbnail = self.get_thumbnail('1280', quality=85)
        return thumbnail.url if thumbnail else None

    def get_image_300x300(self):
        thumbnail = self.get_thumbnail('300x300', crop='center', quality=85)
        return thumbnail.url if thumbnail else None

    def get_image_800x600(self):
        thumbnail = self.get_thumbnail('800x600', quality=85)
        return thumbnail.url if thumbnail else None

    def get_image_tmb(self, width=50, height=50):
        if not self.get_thumbnail:
            return 'Нет изображения'

        try:
            thumbnail = self.get_thumbnail(f'{width}x{height}', crop='center')
            return mark_safe(
                f'<img src="{thumbnail.url}" width="{width}"'
                f' height="{height}" '
                f'style="object-fit: cover;">',
            )
        except Exception:
            return 'Ошибка загрузки'

    def image_tmb(self):
        return self.get_image_tmb()

    def get_thumbnail(self, geometry_string, **options):
        if hasattr(self, 'image') and self.image:
            return get_thumbnail(self.image, geometry_string, **options)
        if hasattr(self, 'main_image') and self.main_image:
            return get_thumbnail(self.main_image, geometry_string, **options)
        return None


class NormiliseBaseModel(models.Model):
    normalised_name = models.CharField(
        max_length=150,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name='нормализованное название',
    )

    def clean(self):
        self.normalised_name = Normalise.normalise(self.name)

    def save(self, *args, **kwargs):
        self.normalised_name = Normalise.normalise(self.name)
        self.full_clean()
        super().save(*args, **kwargs)

    def _save_table(self, *args, **kwargs):
        self.normalised_name = Normalise.normalise(self.name)
        return super()._save_table(*args, **kwargs)

    class Meta:
        abstract = True
