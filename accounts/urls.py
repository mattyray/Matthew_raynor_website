from django.urls import path
from .views import DashboardView, SignupPageView, custom_logout

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("logout/", custom_logout, name="logout"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
