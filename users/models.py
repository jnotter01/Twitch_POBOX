from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):  # Extends Django's default User model
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
