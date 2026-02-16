import json
import logging

from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from openai import OpenAI

from .utils import load_combined_context

logger = logging.getLogger(__name__)

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class ChatAPIView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            message = data.get("message", "")
            if not message or len(message) > 2000:
                return JsonResponse({"error": "Invalid message."}, status=400)

            full_context = load_combined_context()

            chat_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": full_context},
                    {"role": "user", "content": message}
                ]
            )
            reply = chat_response.choices[0].message.content.strip()
            return JsonResponse({"reply": reply})
        except Exception as e:
            logger.exception("Chat API error")
            return JsonResponse({"error": "Something went wrong. Please try again."}, status=500)


class ChatInterfaceView(TemplateView):
    template_name = "chat/chat_interface.html"
