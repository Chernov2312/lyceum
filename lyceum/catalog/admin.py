from django.contrib import admin

from catalog.models import Category, Item, Tag, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = (Category.is_published.field.name,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = (Tag.is_published.field.name,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = (Image.image.field.name,)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = (Item.tags.field.name,)
    list_display = (
        Item.name.field.name,
        Item.is_published.field.name,
        Item.main_image.field.name,
    )
    list_editable = (Item.is_published.field.name,)
    list_display_links = (Item.name.field.name,)
    filter_horizontal = (Item.tags.field.name,)

    @admin.display(description='Категория')
    def category_info(self, obj):
        return obj.category.name if obj.category else '-'

    @admin.display(description='Картинка')
    def category_info(self, obj):
        return obj.image.get_image_300x300() if obj.image else '-'
