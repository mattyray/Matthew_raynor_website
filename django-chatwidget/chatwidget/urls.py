# chatwidget/urls.py

from django.urls import path
from .views import ChatAPIView

app_name = "chatwidget"

urlpatterns = [
    path("api/", ChatAPIView.as_view(), name="api"),
]
