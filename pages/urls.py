from django.urls import path
from .views import HomePageView, PressPageView, contact_view
from . import views
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),  # Ensure this exists!
    path("press/", PressPageView.as_view(), name="press"),
    path("contact/", contact_view, name="contact"),
    path('story/', views.StoryPageView.as_view(), name='story'),

    
    
    
]
