from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from lyceum.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('catalog/', include('catalog.urls')),
    path('download/', include('download.urls')),
    path('feedback/', include('feedback.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]


if DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
