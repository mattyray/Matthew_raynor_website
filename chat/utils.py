# chat/utils.py

from blog.models import Post
from .knowledge_base import KNOWLEDGE_BASE

def load_combined_context():
    posts = Post.objects.filter(is_published=True).order_by("-updated_date")[:5]
    blog_snippets = "\n\n".join(
        f"Title: {post.title}\n{post.content[:500]}..." for post in posts
    )
    return KNOWLEDGE_BASE + "\n\nRecent Blog Posts:\n" + blog_snippets
