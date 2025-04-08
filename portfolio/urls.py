# portfolio/urls.py

from django.urls import path
from .views import PortfolioView, ProjectDetailView

app_name = "portfolio"

urlpatterns = [
    path("", PortfolioView.as_view(), name="index"),
    path("<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
]
