from django.urls import path

from homepage.views import coffee, echo, echo_submit, home

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('coffee/', coffee, name='coffee'),
    path('echo/', echo, name='echo'),
    path('echo/submit', echo_submit, name='echo_submit'),
]
