from django.views.generic import TemplateView
from django.http import Http404

PROJECTS = [
    {
        "title": "EJ Art Moving App",
        "slug": "art-mover",
        "hero_image": "images/projects/art-mover.jpg",
        "description": "A sleek logistics dashboard for managing clients, work orders, and invoices.",
        "overview": "A production-grade business dashboard for an art moving company, complete with scheduling, PDF invoicing, and a dynamic calendar.",
        "tech_stack": {
            "backend": ["Django 5", "Python 3.10", "PostgreSQL", "Docker"],
            "frontend": ["Bootstrap 5", "Crispy Forms", "FullCalendar", "Flatpickr", "Select2"],
            "deployment": ["Docker Compose", "Heroku", "Whitenoise"],
            "tools": ["django-environ", "django-import-export"]
        },
        "problems_solved": [
            "Digitized manual scheduling and invoicing",
            "Visual overview of work orders via FullCalendar",
            "Centralized client, job, and invoice management"
        ],
        "special_features": [
            "Dynamic AJAX invoice creation from client work orders",
            "PDF invoice generation and calendar event syncing",
            "Inline formsets and lazy model references to avoid circular imports"
        ],
        "improvements": [
            "Integrate Stripe or QuickBooks for real payment processing",
            "Add search and filters for completed jobs and past invoices"
        ],
        "proud_of": [
            "Overcame circular model dependencies",
            "Built a real-time calendar with interactive event links"
        ],
        "showcase": "An advanced business app built solo, handling real-world logistics, billing, and scheduling."
    },
    {
        "title": "Freedom Fundraiser Website",
        "slug": "fundraiser",
        "hero_image": "images/projects/fundraiser.jpg",
        "description": "A donation-based campaign platform with embedded video, blog, and outreach.",
        "overview": "Created to support my move out of a nursing home, this campaign site includes a motivational blog, caregiver outreach, and donation CTAs.",
        "tech_stack": {
            "backend": ["Django", "Python", "PostgreSQL"],
            "frontend": ["Bootstrap 5", "Crispy Forms"],
            "deployment": ["Docker", "Heroku", "Whitenoise"],
            "tools": ["django-environ", "YouTube Embed", "Mailchimp (planned)"]
        },
        "problems_solved": [
            "Unified storytelling, fundraising, and updates in one hub",
            "Raised awareness and caregiver interest via CDPAP outreach"
        ],
        "special_features": [
            "Embedded YouTube campaign video with autoplay",
            "Integrated blog from the fundraiser app with admin post editor"
        ],
        "improvements": [
            "Integrate real payment gateway (Stripe or PayPal)",
            "Add comment moderation and CAPTCHA"
        ],
        "proud_of": [
            "Deployed the entire project using Docker and Heroku",
            "Bilingual outreach increased community engagement"
        ],
        "showcase": "Represents personal growth, storytelling, and full-stack deployment."
    },
    {
        "title": "MatthewRaynor.com",
        "slug": "matthew-raynor",
        "hero_image": "images/projects/matthewraynor.jpg",
        "description": "My flagship website combining my story, blog, art store, and technical portfolio.",
        "overview": "A personal brand site where all my passions intersect — tech, writing, art, and accessibility.",
        "tech_stack": {
            "backend": ["Django 5.1.6", "Python 3.10", "PostgreSQL"],
            "frontend": ["Bootstrap 5", "SCSS", "Flatpickr", "FullCalendar"],
            "deployment": ["Docker", "Heroku (Container Stack)", "Whitenoise"],
            "tools": ["Allauth", "Crispy Forms", "django-environ"]
        },
        "problems_solved": [
            "Needed one site to host my store, blog, portfolio, and press",
            "Reduced reliance on platforms like Shopify or Medium"
        ],
        "special_features": [
            "Custom user model + Allauth integration",
            "Chatbot scaffold, press hub, gallery section, blog, and store"
        ],
        "improvements": [
            "Add cart, checkout, and testimonial display",
            "Enable global search and newsletter signup"
        ],
        "proud_of": [
            "Built a fully modular, multi-app Django system",
            "Reflects my resilience and technical versatility"
        ],
        "showcase": "The foundation of my brand and proof of my end-to-end web dev skills."
    },
    {
        "title": "Matt’s Bookstore API",
        "slug": "bookstore",
        "hero_image": "images/projects/bookstore.jpg",
        "description": "A Django REST API bookstore project with Google SSO, reviews, and deployment.",
        "overview": "An API-first bookstore web app with full CRUD for books, ratings, search, and Docker-based deployment.",
        "tech_stack": {
            "backend": ["Django", "DRF", "Python 3.12"],
            "frontend": ["Bootstrap 5", "Crispy Forms"],
            "deployment": ["Docker", "Heroku", "Whitenoise"],
            "tools": ["Allauth", "django-environ"]
        },
        "problems_solved": [
            "Learned DRF by building real API endpoints",
            "Handled book reviews, search, and secure login"
        ],
        "special_features": [
            "UUID and slug-based URLs",
            "Secure reviews via permission classes",
            "Search filtering using Django Q objects"
        ],
        "improvements": [
            "Add frontend search bar and filters",
            "Convert to SPA with Vue or React"
        ],
        "proud_of": [
            "Handled Docker + DRF + PostgreSQL integration solo",
            "Built full book management pipeline"
        ],
        "showcase": "A clean, REST-based bookstore for testing API design and secure auth."
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
        project = next((p for p in PROJECTS if p["slug"] == slug), None)
        if not project:
            raise Http404("Project not found")
        context["project"] = project
        return context
