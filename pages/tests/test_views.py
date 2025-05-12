# pages/tests/test_views.py

from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch
from pages.views import contact_view
from blog.models import Post


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
        request._messages = self.client.session  # necessary for `messages.success`
        response = contact_view(request)

        self.assertEqual(response.status_code, 302)
        mock_send_mail.assert_called_once()

    def test_get_contact_form_renders_template(self):
        response = self.client.get(reverse("pages:contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")


class HomePageViewTest(TestCase):
    def test_homepage_view_uses_correct_template(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_context_includes_recent_posts(self):
        Post.objects.create(title="Test Post", slug="test-post", is_published=True)
        response = self.client.get(reverse("pages:home"))
        self.assertIn("recent_posts", response.context)


class PressPageViewTest(TestCase):
    def test_press_page_renders(self):
        response = self.client.get(reverse("pages:press"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/press.html")
        self.assertIn("press_articles", response.context)


class StoryPageViewTest(TestCase):
    def test_story_page_renders(self):
        response = self.client.get(reverse("pages:story"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/story.html")
