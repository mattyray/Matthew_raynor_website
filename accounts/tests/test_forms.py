from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

class CustomUserCreationFormTest(TestCase):
    def test_form_requires_email_and_passwords(self):
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

    def test_form_creates_user(self):
        data = {
            'email': 'new@user.com',
            'password1': 'complexPass123',
            'password2': 'complexPass123'
        }
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)
        user = form.save()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.email, 'new@user.com')

class CustomUserChangeFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='change@user.com', password='abc123')

    def test_change_form_updates_email(self):
        form = CustomUserChangeForm(instance=self.user, data={'email': 'updated@user.com'})
        self.assertTrue(form.is_valid(), form.errors)
        user = form.save()
        self.assertEqual(user.email, 'updated@user.com')
