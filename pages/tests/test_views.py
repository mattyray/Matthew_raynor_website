from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch
from django.contrib.messages.storage.fallback import FallbackStorage
from pages.views import contact_view, HomePageView
from blog.models import Post
from django.contrib.auth import get_user_model


class ContactViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("pages.views.ContactForm")
    @patch("pages.views.send_mail")
    def test_valid_contact_form_sends_email(self, mock_send_mail, mock_form_class):
        mock_form = mock_form_class.return_value
        mock_form.is_valid.return_value = True
        mock_form.cleaned_data = {
            "name": "Test User",
            "email": "test@example.com",
            "message": "Hello!"
        }

        request = self.factory.post(reverse("pages:contact"), data={})
        
        # ✅ Set up the message framework
        setattr(request, "session", self.client.session)
        request._messages = FallbackStorage(request)

        response = contact_view(request)

        mock_send_mail.assert_called_once()
        self.assertEqual(response.status_code, 302)  # Should redirect


class HomePageViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email="author@test.com",
            password="testpass"
        )

    def test_homepage_context_includes_recent_posts(self):
        Post.objects.create(
            title="Test Post",
            slug="test-post",
            content="Test content",
            is_published=True,
            author=self.user
        )

        request = self.factory.get(reverse("pages:home"))
        request.user = self.user

        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("recent_posts", response.context_data)
        self.assertEqual(len(response.context_data["recent_posts"]), 1)
