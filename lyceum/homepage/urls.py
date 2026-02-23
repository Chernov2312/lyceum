from django.urls import path

from homepage.views import coffee, home

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('coffee/', coffee, name='coffee'),
]
