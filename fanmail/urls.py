from django.urls import path
from . import views  # Import views from the fanmail app

urlpatterns = [
    path("", views.fanmail_list, name="fanmail_list"),  # View all fan mail
    path("new/", views.fanmail_create, name="fanmail_create"),  # Create new fan mail
    path("<int:pk>/edit/", views.fanmail_update, name="fanmail_update"),  # Edit fan mail
    path("<int:pk>/delete/", views.fanmail_delete, name="fanmail_delete"),  # Delete fan mail
]
