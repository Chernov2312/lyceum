from django.urls import path

from download.views import download

app_name = 'download'
urlpatterns = [
    path('<str:file_path>/', download, name='download'),
]
