from django.db import models
from django.conf import settings

class FanMail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to="fanmail_images/", blank=True, null=True)  # 👈 Image field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fan Mail from {self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"
