from django.urls import path

from .views import item_detail, item_list

urlpatterns = [path('<int:item>/', item_detail), path('', item_list)]
