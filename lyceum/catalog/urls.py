from django.urls import path, re_path

from catalog.views import (
    friday,
    get_int_item_detail,
    item_list,
    new,
    unverified,
)

app_name = 'catalog'
urlpatterns = [
    path('', item_list, name='item_list'),
    path('new/', new, name='new'),
    path('friday/', friday, name='friday'),
    path('unverified/', unverified, name='unverified'),
    path('<int:item_id>/', get_int_item_detail, name='item_detail'),
    re_path(
        r're/(?P<item_id>[0-9]*[1-9][0-9]*)/',
        get_int_item_detail,
        name='re_item_detail',
    ),
]
