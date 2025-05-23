# chatwidget/urls.py

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import ChatAPIView

app_name = "chatwidget"

urlpatterns = [
    path("api/", csrf_exempt(ChatAPIView.as_view()), name="api"),  # ✅ CSRF exempted
]
 