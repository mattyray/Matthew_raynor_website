# chatwidget/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from django.conf import settings
import json

class ChatWidgetTests(TestCase):
    def test_api_returns_200(self):
        response = self.client.post(
            reverse("chatwidget:api"),
            data=json.dumps({"message": "Hello"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("reply", response.json())
