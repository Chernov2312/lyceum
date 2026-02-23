from django.contrib import admin

from catalog.models import Category, Image, Item, MainImage, Tag


class ItemImageInline(admin.TabularInline):
    model = Item.images.through
    verbose_name = 'дополнительное изображение'
    verbose_name_plural = 'дополнительные изображения'
    extra = 1


class ItemMainImageInline(admin.StackedInline):
    model = MainImage
    verbose_name = 'главное изображение'
    verbose_name_plural = 'главные изображения'
    extra = 0
    max_num = 1
    fields = (MainImage.main_image, MainImage.image_tmb)
    readonly_fields = (MainImage.image_tmb,)

    def image_tmb(self, obj):
        return obj.image_tmb() if obj.pk else 'Будет доступно после сохранения'

    image_tmb.short_description = 'Превью'


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

    def image_tmb(self, obj):
        return obj.image_tmb()

    image_tmb.short_description = 'Превью'


@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = (Image.id.field.name, Image.image_tmb,)
    readonly_fields = (Image.image_tmb,)

    def image_tmb(self, obj):
        return obj.image_tmb()

    image_tmb.short_description = 'Превью'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = (Item.tags.field.name,)
    list_display = (
        Item.name.field.name,
        Item.is_published.field.name,
        'get_main_image_tmb',
        'get_all_images_tmb',
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
                ),
            },
        ),
        (
            'Изображения',
            {
                'fields': (
                    'main_image',
                    'images',
                    'get_main_image_tmb',
                    'get_all_images_tmb',
                ),
            },
        ),
    )

    readonly_fields = ('get_main_image_tmb', 'get_all_images_tmb')

    @admin.display(description='Категория')
    def category_info(self, obj):
        return obj.category.name if obj.category else '-'
