from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),  # User authentication URLs
    path("fanmail/", include("fanmail.urls")),  # Fan mail app URLs
    path("", include("fanmail.urls")),  # Redirects home to fan mail
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
