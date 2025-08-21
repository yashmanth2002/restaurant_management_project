from django import forms
from .models import Subscriber
from django import forms
from .models import NewsletterSubscription

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'email-input'
            })
        }

class NewsletterForm(forms.ModelForm):
    model = NewsletterSubscription
    fields = ['emai']
    widgets = forms.EmailInput(attrs={ 
        'placeholder': 'Enter your Email',
        'class': 'form-control'
    }),
    