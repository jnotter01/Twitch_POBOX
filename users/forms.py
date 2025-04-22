from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile  # Your custom user model

class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ("username",)  
