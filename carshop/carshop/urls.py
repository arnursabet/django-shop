
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', include('shop.urls', namespace="shop")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    #urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
