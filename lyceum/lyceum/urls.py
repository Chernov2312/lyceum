from django.contrib import admin
from django.urls import include, path

from lyceum.settings import DEBUG

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('catalog/', include('catalog.urls')),
]


if DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
