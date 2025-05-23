#chat/tests/test_views.py
from django.test import TestCase
from django.urls import reverse

class ChatInterfaceViewTest(TestCase):
    def test_chat_interface_loads(self):
        response = self.client.get(reverse("chat:interface"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AI Assistant")
