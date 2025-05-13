from django.views.generic import TemplateView

class ChatInterfaceView(TemplateView):
    template_name = "chat/chat_interface.html"
