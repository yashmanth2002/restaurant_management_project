from django import forms
from .models import Subscriber
from django import forms
from django import forms
from .models import ContactMessage
from django import forms
from .models import RestaurantReview
from django import forms
from .models import Reservation
from django import forms
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
    name = forms.CharField(  
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'})
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'})
    )

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'adte', 'time', 'guests']

class RestaurantReview(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ["rating", "comment"]

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

class ContactForm(forms/ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]

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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)