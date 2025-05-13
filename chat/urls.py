from django.urls import path
from .views import ChatInterfaceView, chat_api_view

app_name = "chat"

urlpatterns = [
    path("", ChatInterfaceView.as_view(), name="interface"),
    path("api/", chat_api_view, name="chat_api"),  # ← backend route

]
