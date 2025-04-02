from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import SignupPageView, DashboardView, custom_logout, ProfileEditView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('login/', include('allauth.urls')),  # or your custom login view
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('logout/', custom_logout, name='logout'),
        path(
        'password/change/',
        auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
        name='password_change'
    ),
    path(
        'password/change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
        name='password_change_done'
    ),
]
