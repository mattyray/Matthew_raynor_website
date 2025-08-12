# pages/forms.py - Just add the honeypot field
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    # Honeypot field - bots will fill this, humans won't see it
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'display:none;',
            'tabindex': '-1',
            'autocomplete': 'off'
        })
    )
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean_website(self):
        """If honeypot field is filled, it's a bot"""
        website = self.cleaned_data.get('website')
        if website:
            raise ValidationError("Bot detected")
        return website