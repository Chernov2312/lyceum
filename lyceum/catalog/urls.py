from django.urls import path, re_path, register_converter

from .converters import PositiveIntegerConverter
from .views import (
    get_int_item_detail,
    item_list,
)

register_converter(PositiveIntegerConverter, 'positive_int')
urlpatterns = [
    path('', item_list),
    path('<int:item_id>/', get_int_item_detail),
    re_path(r're/(?P<item_id>[0-9]*[1-9][0-9]*)/', get_int_item_detail),
    path('converter/<positive_int:item_id>/', get_int_item_detail),
]
