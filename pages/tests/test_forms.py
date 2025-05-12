# pages/tests/test_forms.py
from django.test import TestCase
from unittest.mock import patch
from pages.forms import ContactForm

class ContactFormTest(TestCase):
    @patch('pages.forms.ReCaptchaField.clean')
    def test_contact_form_valid_data(self, mock_clean):
        mock_clean.return_value = True  # Pretend captcha is valid
        form = ContactForm(data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello there!',
            'g-recaptcha-response': 'PASSED'
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_missing_fields(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)
