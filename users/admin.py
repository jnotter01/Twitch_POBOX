from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Register UserProfile with Django's built-in UserAdmin
admin.site.register(UserProfile, UserAdmin)
