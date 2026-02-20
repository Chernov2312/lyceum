from django.conf import settings
from django.contrib import admin

from catalog.models import Category, Item, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('is_published',)
    list_per_page = settings.ADMIN_LIST_PER_PAGE


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ('is_published',)
    list_per_page = settings.ADMIN_LIST_PER_PAGE


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'category_info')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    list_filter = ('is_published', 'category', 'name')
    filter_horizontal = ('tags',)
    list_per_page = settings.ADMIN_LIST_PER_PAGE

    @admin.display(description='Категория')
    def category_info(self, obj):
        return obj.category.name if obj.category else '-'