from django.urls import path, re_path, register_converter

from .convertors import PositiveIntegerConverter
from .views import (
    get_int_converter_endpoint,
    get_int_endpoint,
    item_detail,
    item_list
)

register_converter(PositiveIntegerConverter, 'intpositive')
urlpatterns = [
    path('<int:item>/', item_detail),
    path('', item_list),
    re_path(r're/(?P<id>[0-9]*[1-9][0-9]*)/', get_int_endpoint),
    path('converter/<intpositive:id>/', get_int_converter_endpoint),
]
