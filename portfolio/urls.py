from django.urls import path
from .views import PortfolioView, ProjectDetailView

urlpatterns = [
    path("", PortfolioView.as_view(), name="portfolio"),
    path("<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
]
