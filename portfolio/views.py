from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.utils.text import slugify

# Project data (you can expand later)
PROJECTS = [

    {
        "title": "EJ Art Moving App",
        "slug": "art-mover",
        "description": "A sleek logistics dashboard for scheduling art moves, managing clients, and tracking invoices.",
        "tech": ["Django", "FullCalendar", "Bootstrap", "Docker", "PostgreSQL"],
        "image": "/static/images/projects/art-mover.jpg",
        "live_url": "https://art-moving-buisness-0a734245a61f.herokuapp.com",
        "github_url": "https://github.com/mattyray/art_moving_buisness",
    },
    {
        "title": "Freedom Fundraiser Website",
        "slug": "fundraiser",
        "description": "A modern, heartfelt donation platform with blog, videos, and updates to support my transition to independent living.",
        "tech": ["Django", "Bootstrap", "YouTube Embed", "Heroku"],
        "image": "/static/images/projects/fundraiser.jpg",
        "live_url": "https://www.mattsfreedomfundraiser.com",
        "github_url": "https://github.com/mattyray/fundraiser-website",
    },
    {
        "title": "MatthewRaynor.com",
        "slug": "matthew-raynor",
        "description": "My personal brand site showcasing blog, store, press, and a portfolio of resilience, art, and development.",
        "tech": ["Django", "Allauth", "Bootstrap", "Docker", "Heroku"],
        "image": "/static/images/projects/matthewraynor.jpg",
        "live_url": "https://www.matthewraynor.com",
        "github_url": "https://github.com/mattyray/Matthew_raynor_website",
    },
    {
        "title": "Matt’s Bookstore API",
        "slug": "bookstore",
        "description": "A Django REST API bookstore with Google SSO, ratings, reviews, and Dockerized deployment.",
        "tech": ["Django", "DRF", "Docker", "PostgreSQL", "Heroku"],
        "image": "/static/images/projects/bookstore.jpg",
        "live_url": "https://mattsbookstore-c15521949514.herokuapp.com",
        "github_url": "https://github.com/mattyray/ch4-bookstore",
    },
]

class PortfolioView(TemplateView):
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = PROJECTS
        return context

class ProjectDetailView(TemplateView):
    template_name = "portfolio/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        project = get_object_or_404(PROJECTS, slug=slug)
        context["project"] = project
        return context
