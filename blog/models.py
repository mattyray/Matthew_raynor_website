from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField  # Import the embed video field

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    video = EmbedVideoField(blank=True, null=True)  # New field for video embeds (e.g., TikTok)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        if self.user:
            return f"Comment by {self.user} on {self.post}"
        return f"Comment by {self.name} on {self.post}"
