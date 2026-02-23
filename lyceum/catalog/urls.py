from django.urls import path, re_path

from catalog.views import (
    get_int_item_detail,
    item_list,
)

urlpatterns = [
    path('', item_list, name='catalog'),
    path('<int:item_id>/', get_int_item_detail, name='item_detail'),
    re_path(
        r're/(?P<item_id>[0-9]*[1-9][0-9]*)/',
        get_int_item_detail,
        name='item_detail',
    ),
]
