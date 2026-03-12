from datetime import timedelta

from django.db import models
from django.db.models import Prefetch
from django.utils import timezone

from catalog.models import Image, Tag


__all__ = ['ItemManager']


class ItemManager(models.Manager):
    def _base_queryset(self, include_images=True):
        queryset = (
            self.get_queryset()
            .select_related('category', 'main_image')
            .only('name', 'text', 'main_image__main_image', 'category__name')
        )

        prefetch_tags = Prefetch('tags', queryset=Tag.objects.only('name'))
        prefetch_list = [prefetch_tags]

        if include_images:
            prefetch_list.append(
                Prefetch('images', queryset=Image.objects.only('image')),
            )

        return queryset.prefetch_related(*prefetch_list)

    def _published_base(self, include_images=True):
        return self._base_queryset(include_images=include_images).filter(
            is_published=True,
            category__is_published=True,
        )

    def published(self):
        return self._published_base(include_images=True).order_by('name')

    def on_main(self):
        return (
            self._base_queryset(include_images=False)
            .order_by('name')
            .filter(is_on_main=True)
        )

    def new(self):
        week_ago = timezone.now() - timedelta(days=7)
        return (
            self._published_base(include_images=True)
            .filter(created_at__gte=week_ago)
            .order_by('?')[:5]
        )

    def friday(self):
        return (
            self._published_base(include_images=True)
            .filter(updated_at__week_day=6)
            .order_by('updated_at')[:5]
        )

    def unverified(self):
        delta = timedelta(minutes=1)
        return (
            self._published_base(include_images=True)
            .filter(created_at__gte=models.F('updated_at') - delta)
            .order_by('name')
        )

    def get_object_or_404(self, item_id):
        return (
            self._published_base(include_images=True)
            .filter(id=item_id)
            .first()
        )
