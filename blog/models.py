from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField  # ✅ for rich text
from cloudinary_storage.storage import MediaCloudinaryStorage  # ✅ for Cloudinary upload
from django.contrib.postgres.search import SearchVectorField  # ADD THIS
from django.contrib.postgres.indexes import GinIndex  # ADD THIS

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    
    # ✅ Rich text content field
    content = RichTextUploadingField()

    # ✅ Optional YouTube/TikTok embed
    video = EmbedVideoField(blank=True, null=True)

    # ✅ Optional fallback image
    image = models.ImageField(
        upload_to='blog_images/',
        storage=MediaCloudinaryStorage(),
        null=True,
        blank=True
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    # here!!
    search_vector = SearchVectorField(null=True, blank=True)

    class Meta:
        ordering = ['-published_date']
        # And hurrr!!!
        indexes = [
            GinIndex(fields=['search_vector']),
        ]

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