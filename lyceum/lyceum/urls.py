import django
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('catalog/', include('catalog.urls')),
    path('catalog/', include('about.urls')),
]

if django.conf.settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
