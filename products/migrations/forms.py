from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, label='Your Email')
    message = forms.CharField(
        widget = forms.Textarea(attrs = {'row': 4}),
        required=True
        label="Your Message"
    )