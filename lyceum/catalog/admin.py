from django.conf import settings
from django.contrib import admin

from catalog.models import Category, Item, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = settings.LIST_FILTER_CATEGORY
    list_per_page = settings.LIST_PER_PAGE


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = settings.LIST_FILTER_TAG
    list_per_page = settings.LIST_PER_PAGE


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = settings.LIST_DISPLAY_ITEM
    list_editable = settings.LIST_ADIBLE_ITEM
    list_display_links = settings.LIST_DISPLAY_LINKS_ITEM
    list_filter = settings.LIST_FILTER_ITEM
    filter_horizontal = settings.LIST_HORIZONTAL_ITEM
    list_per_page = settings.LIST_PER_PAGE

    @admin.display(description='Категория')
    def category_info(self, obj):
        return obj.category.name if obj.category else '-'
