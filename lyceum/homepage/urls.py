from django.urls import path

from homepage.views import coffee, home, echo

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('coffee/', coffee, name='coffee'),
    path('echo/', echo, name='echo'),
]
