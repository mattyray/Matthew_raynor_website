from django.views.generic import TemplateView
from openai import OpenAI
from django.conf import settings
from django.views import View
from django.http import JsonResponse
import json

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class ChatAPIView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            message = data.get("message", "")

            # Add context
            system_prompt = (
                "You are a helpful assistant on MatthewRaynor.com. "
                "Matthew Raynor is a quadriplegic artist, developer, and author. "
                "He lives in a nursing home and is working toward independence. "
                "He offers web development services, custom drone photography, and motivational content. "
                "People can support him by donating or sharing his story. "
                "If someone asks about his injury, needs, projects, or how to help, explain warmly and clearly."
            )

            chat_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ]
            )
            reply = chat_response.choices[0].message.content.strip()
            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class ChatInterfaceView(TemplateView):
    template_name = "chat/chat_interface.html"
