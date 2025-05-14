from django.urls import path
from .views import ChatInterfaceView, ChatAPIView
from django.views.decorators.csrf import csrf_exempt

app_name = "chat"

urlpatterns = [
    path("", ChatInterfaceView.as_view(), name="interface"),
    path("api/", csrf_exempt(ChatAPIView.as_view()), name="api"),  # ✅ FIXED HERE
]
