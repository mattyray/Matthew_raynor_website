from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserManagerTest(TestCase):
    def test_create_user_without_email_raises(self):
        with self.assertRaisesMessage(ValueError, "The Email field must be set"):
            User.objects.create_user(email="", password="pass123")

    def test_create_user_successful(self):
        user = User.objects.create_user(email="u@example.com", password="pass123")
        self.assertEqual(user.email, "u@example.com")
        self.assertTrue(user.check_password("pass123"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser_sets_flags(self):
        su = User.objects.create_superuser(email="su@example.com", password="pass123")
        self.assertTrue(su.is_staff)
        self.assertTrue(su.is_superuser)

class CustomUserModelTest(TestCase):
    def test_str_returns_email(self):
        user = User.objects.create_user(email="foo@bar.com", password="foo")
        self.assertEqual(str(user), "foo@bar.com")
