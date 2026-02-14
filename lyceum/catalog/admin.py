import catalog.models
from django.contrib import admin


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = 'is_published'
    list_display_links = 'name'
