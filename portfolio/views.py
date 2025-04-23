from django.views.generic import TemplateView
from django.http import Http404
# 

PROJECTS = [
    {
        "title": "EJ Art Moving App",
        "slug": "art-mover",
        "hero_image": "images/projects/art-mover.jpg",
        "description": "A sleek logistics dashboard for managing clients, work orders, and invoices.",
        "overview": "A production-grade business dashboard for an art moving company, complete with scheduling, PDF invoicing, and a dynamic calendar.",
        "tech_stack": {
            "backend": ["Django 5.1.6", "Python 3.10", "PostgreSQL", "Docker"],
            "frontend": ["Bootstrap 5", "Crispy Forms", "FullCalendar", "Flatpickr", "Select2"],
            "deployment": ["Docker Compose", "Heroku", "Whitenoise"],
            "tools": ["django-environ", "django-import-export"]
        },
        "problem": "The client was managing logistics, invoicing, and scheduling manually via email and spreadsheets, which caused delays and errors.",
        "solution": "I created a centralized system that tracks jobs, clients, and invoices using relational models, AJAX-enhanced forms, and a real-time calendar for scheduling.",
        "special_features": [
            "Dynamic AJAX invoice creation from client work orders",
            "PDF invoice generation and calendar event syncing",
            "Inline formsets and lazy model references to avoid circular imports"
        ],
        "problems_solved": [
            "Digitized manual scheduling and invoicing",
            "Visual overview of work orders via FullCalendar",
            "Centralized client, job, and invoice management"
        ],
        "improvements": [
            "Integrate Stripe or QuickBooks for real payment processing",
            "Add search and filters for completed jobs and past invoices"
        ],
        "proud_of": [
            "Overcame circular model dependencies",
            "Built a real-time calendar with interactive event links"
        ],
        "build_notes": "<p>Containerized with Docker, deployed using Heroku's container stack. PostgreSQL health checks ensure app doesn’t launch before DB is ready.</p>",
        "github_url": "https://github.com/mattyray/art_moving_buisness",
        "live_url": "https://art-moving-buisness-0a734245a61f.herokuapp.com"
    },
    {
        "title": "Matt’s Freedom Fundraiser",
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
        "problem": "I needed a way to raise funds for housing and medical needs while also telling my story and engaging my community.",
        "solution": "I built a multi-page fundraising site that includes a blog, press coverage, embedded video, and contact outreach tools.",
        "special_features": [
            "Embedded YouTube campaign video with autoplay",
            "Integrated blog with post editor and dynamic list/detail views"
        ],
        "problems_solved": [
            "Unified storytelling, fundraising, and updates in one hub",
            "Raised awareness and caregiver interest via CDPAP outreach"
        ],
        "improvements": [
            "Integrate Stripe or PayPal for donations",
            "Add comment moderation and CAPTCHA"
        ],
        "proud_of": [
            "Deployed solo with Docker and Heroku",
            "Bilingual outreach increased community engagement"
        ],
        "build_notes": "<p>Uses Django Pages app with static press data. Campaign blog and store are modular and reusable across other projects.</p>",
        "github_url": "https://github.com/mattyray/fundraiser-website",
        "live_url": "https://www.mattfreedomfundraiser.com"
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
        "problem": "I needed a single platform to unify my professional work, writing, art, and personal journey to help others and represent myself to the world.",
        "solution": "I built a full-featured Django site with custom user login, store, blog, portfolio, and press coverage hub.",
        "special_features": [
            "Custom user model + Allauth integration",
            "Press hub, blog, store, and modular portfolio detail pages",
            "AI chatbot scaffold and accessible frontend"
        ],
        "problems_solved": [
            "Needed one site to host my store, blog, portfolio, and press",
            "Reduced reliance on platforms like Shopify or Medium"
        ],
        "improvements": [
            "Add Stripe cart/checkout system",
            "Enable newsletter signup and global search"
        ],
        "proud_of": [
            "Built a fully modular, multi-app Django system",
            "Reflects my resilience and technical versatility"
        ],
        "build_notes": "<p>Every page is component-driven with a global base template. Portfolio is hardcoded for now, but database-driven expansion is planned.</p>",
        "github_url": "https://github.com/mattyray/Matthew_raynor_website",
        "live_url": "https://www.matthewraynor.com"
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
        "problem": "I wanted to learn Django REST Framework by building an API-first bookstore that could handle real CRUD operations and secure logins.",
        "solution": "Created a REST-ready bookstore with user authentication, image uploads, reviews, and Heroku-based deployment using Docker.",
        "special_features": [
            "UUID and slug-based URLs",
            "Secure reviews via permission classes",
            "Search filtering using Django Q objects"
        ],
        "problems_solved": [
            "Learned DRF by building real API endpoints",
            "Handled book reviews, search, and secure login"
        ],
        "improvements": [
            "Add frontend search bar and filters",
            "Convert to SPA with Vue or React"
        ],
        "proud_of": [
            "Handled Docker + DRF + PostgreSQL integration solo",
            "Built full book management pipeline"
        ],
        "build_notes": "<p>Heroku container stack deployment using `heroku.yml` and `.env` management. Includes future-ready DRF endpoints for mobile or SPA frontend.</p>",
        "github_url": "https://github.com/mattyray/ch4-bookstore",
        "live_url": ""  # Currently broken, noted in portfolio
    },
    {
    "title": "AI Motivational Chatbot",
    "slug": "motivational-chatbot",
    "hero_image": "images/projects/motivational-chatbot.jpg",
    "description": "An AI-powered real-time chat interface built to uplift, motivate, and support users through guided messages and mindfulness prompts.",
    "overview": "This web app features a real-time motivational chatbot using Django Channels and OpenAI's GPT-4 API. Designed with accessibility and emotional support in mind, it offers inspiring guidance with markdown-to-HTML formatting and secure WebSocket messaging.",
    "tech_stack": {
        "backend": ["Django 5.1.6", "Python 3.12", "PostgreSQL", "Docker"],
        "frontend": ["Bootstrap 5", "Crispy Forms", "JavaScript WebSocket API"],
        "deployment": ["Docker Compose", "Heroku", "Whitenoise"],
        "tools": ["Channels", "OpenAI SDK (>=1.0.0)", "django-environ", "markdown"]
    },
    "problem": "Users lacked an uplifting, real-time interface to ask spiritual, emotional, or motivational questions and receive formatted responses that felt supportive.",
    "solution": "Built a guided AI chatbot interface that handles live input, streams OpenAI GPT-4 responses, and uses markdown formatting for expressive feedback.",
    "special_features": [
        "Live WebSocket chat powered by Django Channels",
        "OpenAI GPT-4 Turbo integration with markdown-to-HTML formatting",
        "Responsive layout with accessibility-focused design choices"
    ],
    "problems_solved": [
        "Enabled real-time motivational chat for users seeking support",
        "Removed latency by using async communication and markdown rendering",
        "Created a safe space for users to engage with uplifting messages"
    ],
    "improvements": [
        "Add user accounts and saved conversation history",
        "Integrate voice recognition and text-to-speech for accessibility",
        "Implement streaming response instead of chunked delivery"
    ],
    "proud_of": [
        "Successfully implemented real-time async chat with OpenAI GPT-4",
        "Handled migration to OpenAI SDK 1.0+ and updated markdown rendering",
        "Built with performance and spiritual value in mind"
    ],
    "build_notes": "<p>Chat interface built with Django Channels, using Redis for pub/sub communication. WebSocket connection gracefully handles disconnects and errors, and the OpenAI SDK 1.0+ interface ensures future-proof API usage.</p>",
    "github_url": "https://github.com/mattyray/ai_motivator_chatbot",
    "live_url": "https://ai-motivator-chatbot.herokuapp.com"
}

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
