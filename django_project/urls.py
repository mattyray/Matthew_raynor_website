from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView, TemplateView
from accounts.views import DashboardView  # if not already imported


urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),  # ✅ Add this line
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path("blog/", include("blog.urls")),
    path("", include("pages.urls")),  # This must come first so "pages:home" is registered
    path("home/", RedirectView.as_view(url=reverse_lazy("pages:home"), permanent=False), name="home"),
    path("store/", include("store.urls")),
    path("portfolio/", include(("portfolio.urls", "portfolio"), namespace="portfolio")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("chat/", include("chat.urls", namespace="chat")),  # 👈 Add this line
    path("chatwidget/", include("chatwidget.urls")),
    path("test-chatwidget/", TemplateView.as_view(template_name="test_chatwidget.html")),




]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
