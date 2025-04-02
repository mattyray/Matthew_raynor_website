from django.urls import path, include
from .views import SignupPageView, DashboardView, custom_logout, ProfileEditView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('login/', include('allauth.urls')),  # or your custom login view
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('logout/', custom_logout, name='logout'),
]
