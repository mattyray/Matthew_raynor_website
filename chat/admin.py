from django.contrib import admin

from .models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ["created_at", "short_message", "session_key", "page_url"]
    list_filter = ["created_at"]
    search_fields = ["user_message", "ai_response"]
    readonly_fields = ["session_key", "page_url", "user_message", "ai_response", "created_at"]
    date_hierarchy = "created_at"

    def short_message(self, obj):
        return obj.user_message[:100]
    short_message.short_description = "User Message"
