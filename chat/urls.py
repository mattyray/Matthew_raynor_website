from django.urls import path
from .views import ChatInterfaceView

app_name = "chat"

urlpatterns = [
    path("", ChatInterfaceView.as_view(), name="interface"),
]
