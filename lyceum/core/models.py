from django.db import models


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
