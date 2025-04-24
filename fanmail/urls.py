from django.urls import path
from . import views  

urlpatterns = [
    path("", views.fanmail_list, name="fanmail_list"),  # View all fan mail
    path("new/", views.fanmail_create, name="fanmail_create"),  # Create new fan mail
    path("<int:pk>/edit/", views.fanmail_update, name="fanmail_update"),  # Edit fan mail
    path("<int:pk>/delete/", views.fanmail_delete, name="fanmail_delete"),  # Delete fan mail
    path("gallery/", views.fanmail_gallery, name="fanmail_gallery"), #View fan mail gallery
    path("package_notify/", views.package_notify, name="package_notify"), #package notification system
    path("my_packages/", views.my_packages, name="my_packages"), #View package submissions
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
