from django.urls import path
from .views import ChatInterfaceView, ChatAPIView

app_name = "chat"

urlpatterns = [
    path("", ChatInterfaceView.as_view(), name="interface"),
    path("api/", ChatAPIView.as_view(), name="api"),
]
