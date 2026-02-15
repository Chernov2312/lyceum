from django.contrib import admin

from catalog.models import Category, Item, Tag

LIST_PER_PAGE = 20
SEARCH_FIELDS_CATEGORY = ['name', 'slug']
SEARCH_FIELDS_TAG = ['name', 'slug']
SEARCH_FIELDS_ITEM = ['name', 'text']
LIST_FILTER_CATEGORY = ['is_published']
LIST_FILTER_TAG = ['is_published']
LIST_FILTER_ITEM = ['is_published', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'weight',
        'is_published',
        'get_items_count',
    )
    list_editable = ('weight', 'is_published')
    list_display_links = ('name',)
    list_filter = LIST_FILTER_CATEGORY
    search_fields = SEARCH_FIELDS_CATEGORY
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = LIST_PER_PAGE

    @admin.display(description='Количество товаров')
    def get_items_count(self, obj):
        return obj.items.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'is_published',
        'get_items_count',
    )
    list_editable = ('is_published',)
    list_display_links = ('name',)
    list_filter = LIST_FILTER_TAG
    search_fields = SEARCH_FIELDS_TAG
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = LIST_PER_PAGE

    @admin.display(description='Количество товаров')
    def get_items_count(self, obj):
        return obj.items.count()


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'category_info')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    list_filter = LIST_FILTER_ITEM
    search_fields = SEARCH_FIELDS_ITEM
    filter_horizontal = ('tags',)
    list_per_page = LIST_PER_PAGE

    fieldsets = (
        (
            'Основная информация',
            {
                'fields': ('name', 'text', 'is_published'),
            },
        ),
        (
            'Связи',
            {
                'fields': ('category', 'tags'),
                'description': 'Выберите категорию и теги для товара',
            },
        ),
    )

    @admin.display(description='Категория', ordering='category__name')
    def category_info(self, obj):
        if obj.category:
            return f'{obj.category.name} (вес: {obj.category.weight})'
        return 'Не указана'

    @admin.display(description='Количество тегов')
    def get_tags_count(self, obj):
        return obj.tags.count()
