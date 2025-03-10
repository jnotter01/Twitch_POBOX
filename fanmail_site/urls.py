from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),  # User authentication URLs
    path("fanmail/", include("fanmail.urls")),  # Fan mail app URLs
    path("", include("fanmail.urls")),  # Redirects home to fan mail
]
