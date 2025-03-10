from django import forms
from .models import FanMail

class FanMailForm(forms.ModelForm):
    class Meta:
        model = FanMail
        fields = ['message', 'image']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your fan mail here...'}),
        }
