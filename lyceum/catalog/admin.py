from django.contrib import admin

from catalog.models import Category, Image, Item, MainImage, Tag

__all__ = []


class ItemImageInline(admin.TabularInline):
    model = Item.images.through
    verbose_name = 'дополнительное изображение'
    verbose_name_plural = 'дополнительные изображения'
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = (Category.is_published.field.name,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = (Tag.is_published.field.name,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (Image.id.field.name, Image.image_tmb)
    readonly_fields = (Image.image_tmb,)


@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = (
        MainImage.id.field.name,
        MainImage.image_tmb,
    )
    readonly_fields = (MainImage.image_tmb,)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = (ItemImageInline,)
    filter_horizontal = (Item.tags.field.name,)
    list_display = (
        Item.name.field.name,
        Item.is_published.field.name,
        Item.is_on_main.field.name,
        'main_image_tmb',
        Item.get_all_images_tmb,
    )
    list_editable = (Item.is_published.field.name,)
    list_display_links = (Item.name.field.name,)

    fieldsets = (
        (
            'Основная информация',
            {
                'fields': (
                    'name',
                    'text',
                    'category',
                    'tags',
                    'is_published',
                    'is_on_main',
                ),
            },
        ),
        (
            'Изображения',
            {
                'fields': (
                    'main_image',
                    'images',
                    'get_all_images_tmb',
                ),
            },
        ),
    )

    readonly_fields = ('get_all_images_tmb',)

    @admin.display(description='Главное изображение')
    def main_image_tmb(self, obj):
        if obj.main_image:
            return obj.main_image.image_tmb()

        return 'Нет изображения'

    @admin.display(description='Список изображений')
    def image_tmb(self, obj):
        if obj.image:
            return obj.image.image_tmb()

        return 'Нет изображения'

    @admin.display(description='Категория')
    def category_info(self, obj):
        return obj.category.name if obj.category else '-'
