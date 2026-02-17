from django.db import models

from core.unic_field import Normalise


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
    normalized_name = models.CharField(
        max_length=150,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name='нормализованное название',
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.normalized_name = Normalise.normalize_name(self.name)
        super().save(*args, **kwargs)
