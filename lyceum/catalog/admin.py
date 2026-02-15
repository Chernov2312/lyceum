from django.contrib import admin

from catalog.models import Category, Item, Tag

LIST_PER_PAGE = 20
LIST_FILTER_CATEGORY = ['is_published']
LIST_FILTER_TAG = ['is_published']
LIST_FILTER_ITEM = ['is_published', 'category']
LIST_DISPLAY_ITEM = ('name', 'is_published', 'category_info')
LIST_ADIBLE_ITEM = ('is_published',)
LIST_FILTER_ITEM = ('name',)
LIST_DISPLAY_LINKS_ITEM = ('name',)
LIST_HORIZONTAL_ITEM = ('tags',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = LIST_FILTER_CATEGORY
    list_per_page = LIST_PER_PAGE


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = LIST_FILTER_TAG
    list_per_page = LIST_PER_PAGE


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_ITEM
    list_editable = LIST_ADIBLE_ITEM
    list_display_links = LIST_DISPLAY_LINKS_ITEM
    list_filter = LIST_FILTER_ITEM
    filter_horizontal = LIST_HORIZONTAL_ITEM
    list_per_page = LIST_PER_PAGE

    @admin.display(description='Категория')
    def category_info(self, obj):
        return obj.category.name if obj.category else '-'
