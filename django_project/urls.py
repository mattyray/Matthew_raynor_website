from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("", include("pages.urls")),  # This must come first so "pages:home" is registered
    path("home/", RedirectView.as_view(url=reverse_lazy("pages:home"), permanent=False), name="home"),
    path("store/", RedirectView.as_view(url="https://store.matthewraynor.com", permanent=False), name="store_redirect"),
    path("portfolio/", include(("portfolio.urls", "portfolio"), namespace="portfolio")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("chat/", include("chat.urls", namespace="chat")),
    path("search/", include("search.urls", namespace="search")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)