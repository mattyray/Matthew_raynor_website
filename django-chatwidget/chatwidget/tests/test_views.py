from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
import json


class ChatWidgetTests(TestCase):
    @patch("chatwidget.views.get_openai_response", return_value="Hello from mock!")
    def test_api_returns_200(self, mock_get_openai_response):
        response = self.client.post(
            reverse("chatwidget:api"),
            data=json.dumps({"message": "Hello"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["reply"], "Hello from mock!")
