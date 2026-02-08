from django.urls import path, re_path

from .views import get_int_endpoint, item_detail, item_list

urlpatterns = [
    path('<int:item>/', item_detail),
    path('', item_list),
    re_path(r're/(?P<id>[1-9]+)/', get_int_endpoint),
    path('converter/<int:id>/', get_int_endpoint),
]
