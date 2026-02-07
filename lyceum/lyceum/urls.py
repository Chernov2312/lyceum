from about.views import description

from catalog.views import item_list, item_detail

from django.contrib import admin
from django.urls import path

from homepage.views import home
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('about/', description),
    path('catalog/', item_list),
    path('catalog/<int:item>', item_detail)
]
