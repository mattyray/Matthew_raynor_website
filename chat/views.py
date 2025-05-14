from django.views.generic import TemplateView
import openai
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

@method_decorator(csrf_exempt, name='dispatch')
class ChatAPIView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user_input = data.get("message", "").strip()

            if not user_input:
                return JsonResponse({"error": "No input provided."}, status=400)

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant trained on Matthew Raynor's story, web development, photography, and recovery journey."},
                    {"role": "user", "content": user_input},
                ],
            )

            reply = response.choices[0].message.content.strip()
            return JsonResponse({"reply": reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)



class ChatInterfaceView(TemplateView):
    template_name = "chat/chat_interface.html"
