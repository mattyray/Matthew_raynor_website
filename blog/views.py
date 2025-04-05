from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Post, Comment
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("post_detail", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = self.object.comments.filter(approved=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        if self.request.user.is_authenticated:
            comment.user = self.request.user
        comment.approved = True  # Automatically approve for now
        comment.save()
        return super().form_valid(form)
