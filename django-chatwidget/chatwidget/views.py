import json
import logging
from django.http import JsonResponse
from django.views import View
from .openai_utils import get_openai_response

logger = logging.getLogger(__name__)

class ChatAPIView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            reply = get_openai_response(user_message)
            return JsonResponse({"reply": reply})
        except Exception as e:
            logger.exception("💥 ChatWidget API error")
            return JsonResponse({"error": str(e)}, status=500)
