from django import forms
from .models import FanMail
from .models import PackageNotification

class FanMailForm(forms.ModelForm):
    class Meta:
        model = FanMail
        fields = ['message', 'image']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your fan mail here...'}),
        }

class PackageNotificationForm(forms.ModelForm):
    class Meta:
        model = PackageNotification
        fields = ['message', 'sent_date']