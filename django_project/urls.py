from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),         # Custom signup and logout routes
    path("accounts/", include("allauth.urls")),            # Django-allauth handles login, signup, etc.
    path("blog/", include("blog.urls")),                   # Blog URLs
    path("", include("pages.urls")),                       
    path("store/", include("store.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
