from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from openai import OpenAI
from django.conf import settings
from django.views import View
from django.http import JsonResponse
import json
from .utils import load_combined_context  # 👈 add this import


client = OpenAI(api_key=settings.OPENAI_API_KEY)


@csrf_exempt
class ChatAPIView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            message = data.get("message", "")
            full_context = load_combined_context()  # 👈 now uses both blog + KB

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
            return JsonResponse({"error": str(e)}, status=500)


class ChatInterfaceView(TemplateView):
    template_name = "chat/chat_interface.html"
