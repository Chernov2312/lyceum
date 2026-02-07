from catalog import item_list

from django.contrib import admin
from django.urls import path

from homepage import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('catalog/', item_list),
]
