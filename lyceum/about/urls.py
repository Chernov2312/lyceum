from django.urls import path

from about.views import description

app_name = 'about'
urlpatterns = [
    path('', description),
]
