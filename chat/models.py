from django.db import models


class ChatMessage(models.Model):
    session_key = models.CharField(max_length=64, blank=True, default="")
    page_url = models.URLField(max_length=500, blank=True, default="")
    user_message = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.created_at:%Y-%m-%d %H:%M} — {self.user_message[:80]}"
