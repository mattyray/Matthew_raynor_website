from django.views.generic import TemplateView
from blog.models import Post  # 👈 Import the Post model

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add 3 most recently updated published posts
        context["recent_posts"] = Post.objects.filter(is_published=True).order_by('-updated_date')[:3]
        return context
