from django.views.generic import TemplateView
import openai
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def chat_api_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI assistant for MatthewRaynor.com. Help visitors understand who Matthew is, his journey, how to contact him, what services he offers (web development, drone photography), and how to donate or support his mission to leave the nursing home."},
                    {"role": "user", "content": user_message},
                ],
                temperature=0.7,
                max_tokens=300,
            )

            reply = response["choices"][0]["message"]["content"]
            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


class ChatInterfaceView(TemplateView):
    template_name = "chat/chat_interface.html"
