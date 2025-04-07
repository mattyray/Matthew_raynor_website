from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

# Upgraded PROJECTS list with full build-out data
PROJECTS = [
    {
        "title": "EJ Art Moving App",
        "slug": "art-mover",
        "description": "A sleek logistics dashboard for scheduling art moves, managing clients, and tracking invoices.",
        "tech": ["Django", "FullCalendar", "Bootstrap", "Docker", "PostgreSQL"],
        "hero_image": "/static/images/projects/art-mover.jpg",
        "highlights": [
            "Custom client, work order, and invoice models",
            "Color-coded calendar with FullCalendar.js",
            "PDF invoice generation and status tracking",
            "Flatpickr + Select2 integration for date/time forms",
            "Dockerized setup with health checks and PostgreSQL"
        ],
        "problem": "The business needed a centralized, digital workflow to manage high-value art moves across locations and teams.",
        "solution": "I built a clean admin dashboard with calendar views, invoice logic, and real-time work order tracking.",
        "build_notes": """
            <p>Deployed via Docker and Heroku, this application uses Bootstrap 5 and Django Forms styled with Crispy Forms for the frontend. The backend supports full CRUD functionality for clients, work orders, and invoices, with PDF generation and status automation. A robust scheduling system integrates Flatpickr for dates and FullCalendar for visual management.</p>
        """,
        "live_url": "https://art-moving-buisness-0a734245a61f.herokuapp.com",
        "github_url": "https://github.com/mattyray/art_moving_buisness",
    },
    {
        "title": "Freedom Fundraiser Website",
        "slug": "fundraiser",
        "description": "A modern, heartfelt donation platform with blog, videos, and updates to support my transition to independent living.",
        "tech": ["Django", "Bootstrap", "YouTube Embed", "Heroku", "Docker", "PostgreSQL"],
        "hero_image": "/static/images/projects/fundraiser.jpg",
        "highlights": [
            "Embedded YouTube campaign video with autoplay",
            "Blog for motivational updates",
            "Bilingual CDPAP caregiver outreach section",
            "Donation CTA buttons styled with Bootstrap",
            "Contact form scaffolded with future CAPTCHA"
        ],
        "problem": "I needed a platform to tell my story and raise support as I transitioned out of the nursing home.",
        "solution": "I built this from scratch using Django and Docker, embedding videos, blog posts, and links to external fundraising tools.",
        "build_notes": """
            <h5 class="fw-bold mt-4">Technical Overview</h5>
            <ul>
              <li>Custom Django app architecture (pages, blog, accounts, store)</li>
              <li>Responsive UI built with Bootstrap 5 and Crispy Forms</li>
              <li>Static files served with Whitenoise in production</li>
              <li>Dockerized development and deployment via Heroku</li>
              <li>Secure environment management using django-environ</li>
            </ul>
            <h5 class="fw-bold mt-3">Future Additions</h5>
            <ul>
              <li>Stripe donations (custom checkout)</li>
              <li>AI assistant chatbot integration</li>
              <li>SEO and newsletter signup form</li>
            </ul>
        """,
        "live_url": "https://www.mattsfreedomfundraiser.com",
        "github_url": "https://github.com/mattyray/fundraiser-website",
    },
    {
        "title": "MatthewRaynor.com",
        "slug": "matthew-raynor",
        "description": "My personal brand site showcasing blog, store, press, and a portfolio of resilience, art, and development.",
        "tech": ["Django", "Allauth", "Bootstrap", "Docker", "Heroku"],
        "hero_image": "/static/images/projects/matthewraynor.jpg",
        "highlights": [
            "Integrated blog, e-commerce, press, and portfolio",
            "Deployed using Docker and Heroku container stack",
            "Secure custom user model with allauth login",
            "Full mobile support and accessibility styling",
            "AI chatbot scaffolded for site-wide assistance"
        ],
        "problem": "I needed a personal hub to unite my creative, technical, and motivational work under one platform.",
        "solution": "I fused my coding, writing, and photography into one polished brand identity, powered by Django and Docker.",
        "build_notes": """
            <p>This site brings together my full-stack skills and personal journey. It includes modular Django apps for blog posts, portfolio items, e-commerce products, and press content. Custom account handling with Google SSO, AI chatbot integration, and a clean responsive UI make this a powerful portfolio centerpiece.</p>
        """,
        "live_url": "https://www.matthewraynor.com",
        "github_url": "https://github.com/mattyray/Matthew_raynor_website",
    },
    {
        "title": "Matt’s Bookstore API",
        "slug": "bookstore",
        "description": "A Django REST API bookstore with Google SSO, ratings, reviews, and Dockerized deployment.",
        "tech": ["Django", "DRF", "Docker", "PostgreSQL", "Heroku"],
        "hero_image": "/static/images/projects/bookstore.jpg",
        "highlights": [
            "Custom user model with email login and Django Admin integration",
            "Books app with CRUD, slugs, UUID primary keys, and media uploads",
            "Authenticated reviews using DRF and permissions",
            "Full-text search with Q filtering across fields",
            "Docker + PostgreSQL with Heroku deployment"
        ],
        "problem": "I wanted to learn Django REST Framework by building a real-world bookstore API from scratch.",
        "solution": "I followed Django for Professionals and added Google SSO, DRF auth, and Docker deployment to cement my skills.",
        "build_notes": """
            <p>This API-focused bookstore project includes complete REST endpoints for listing, searching, reviewing, and managing books. It's deployed via Docker/Heroku with PostgreSQL, crispy form styling, and secure account login using django-allauth. I implemented review permission checks, search filters, and full admin control.</p>
        """,
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
