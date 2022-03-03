from .models import Mail
from django.forms import ModelForm, EmailInput

class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = ['mail']
        
        widgets = {
            'mail': EmailInput(attrs={
                "class": 'form-control',
                "placeholder": "name@example.com",
                "style": 'width: 300px'
            })
        }