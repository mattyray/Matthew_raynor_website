from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout, get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.http import Http404

# Updated PROJECTS with Enhanced Fundraiser Entry
PROJECTS = [
    {
        "title": "HistoryFace AI - Face Swap SaaS",
        "slug": "historyface-ai",
        "hero_video": "https://youtu.be/rpkIL5FZbpA",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173587/motivational-chatbot_b2e8qv.jpg",
        "description": "An AI-powered SaaS app that transforms your face into historical figures using facial recognition and HuggingFace AI models.",
        "overview": "HistoryFace is a production-grade SaaS application that uses advanced facial recognition to match users with historical figures, then applies AI face-swapping technology to create realistic transformations. Built with a complete freemium business model, external AI integrations, and smart cost management.",
        "tech_stack": {
            "backend": ["Django 5.1.6", "Django REST Framework", "PostgreSQL", "Redis", "Celery"],
            "frontend": ["React 18", "TypeScript", "Tailwind CSS", "Axios"],
            "ai_integration": ["HuggingFace Spaces", "FaceFusion Model", "dlib", "face-recognition", "OpenCV"],
            "deployment": ["Docker", "Fly.io", "Netlify", "Cloudinary"],
            "business": ["Stripe API", "Google OAuth", "Session Tracking", "Usage Limits"]
        },
        "problem": "Creating a viral AI face-swapping app requires complex facial recognition, expensive GPU processing, smart cost management, and a sustainable monetization strategy - all while maintaining fast user experience.",
        "solution": "Built a complete SaaS architecture integrating HuggingFace AI models with custom facial recognition, implemented freemium usage tracking, automated cost controls, and real-time API processing for seamless user experience.",
        "special_features": [
            "Advanced facial recognition using dlib and cosine similarity matching",
            "Real-time API integration with HuggingFace Spaces GPU infrastructure", 
            "Smart freemium model with session-based usage tracking",
            "Automated Cloudinary storage cleanup to control costs",
            "Google OAuth authentication with unlimited access for registered users",
            "Responsive React frontend with live processing updates",
            "Stripe payment integration for subscription monetization"
        ],
        "problems_solved": [
            "Cost-effective AI model integration without running own GPU infrastructure",
            "Real-time face swapping with 25-30 second processing pipeline",
            "Sustainable business model balancing free trials with paid conversions",
            "Scalable architecture ready for thousands of concurrent users",
            "Automated resource cleanup preventing runaway cloud costs"
        ],
        "improvements": [
            "Implement background job processing with Celery for better scaling",
            "Add more historical figure options and categories",
            "Create mobile app version with React Native",
            "Integrate additional AI models for different transformation styles",
            "Add social sharing features and user galleries"
        ],
        "proud_of": [
            "Successfully integrated complex AI services with minimal latency",
            "Built complete SaaS business model from freemium to paid subscriptions", 
            "Overcame accessibility challenges to create production-grade AI application",
            "Designed smart cost management preventing expensive surprises",
            "Created viral-ready app architecture that can scale instantly"
        ],
        "build_notes": "<p>This project demonstrates advanced AI integration, business model implementation, and cost-conscious cloud architecture. The facial recognition pipeline uses mathematical comparison of facial features, while the HuggingFace integration required custom API client development. Built with accessibility in mind using voice commands and adaptive technologies.</p>",
        "github_url": "https://github.com/mattyray/ai-convert",
        "video_url": "https://youtu.be/rpkIL5FZbpA"
    },
    {
        "title": "EJ Art Moving App",
        "slug": "art-mover",
        "hero_video": "https://youtu.be/xWtrO4F0In4",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173585/art-mover_tlvsny.jpg",
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
        "build_notes": "<p>Containerized with Docker, deployed using Heroku's container stack. PostgreSQL health checks ensure app doesn't launch before DB is ready.</p>",
        "github_url": "https://github.com/mattyray/art_moving_buisness",
    },
    {
        "title": "MatthewRaynor.com",
        "slug": "matthew-raynor",
        "hero_video": "https://youtu.be/pWuW1AasRGY",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173587/matthewraynor_rjiinl.jpg",
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
        "title": "Matt's Freedom Fundraiser - When GoFundMe Almost Stole $26K",
        "slug": "fundraiser",
        "hero_video": "https://youtu.be/ZumlW-noN6E",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173586/fundraiser_gsbo4o.jpg",
        "description": "After GoFundMe nearly blocked my $26K withdrawal with terrible policies, I built my own donation platform with zero platform fees.",
        "overview": "When I needed funds to escape the nursing home, I initially used GoFundMe. Big mistake. They made it nearly impossible to withdraw money, took percentage cuts, and offered zero customer service. We almost lost everything due to their predatory refund policies. So I did what any developer would do: I built my own platform with direct Stripe integration and complete donor control.",
        "tech_stack": {
            "backend": ["Django 5.1.6", "Django REST Framework", "PostgreSQL", "Redis", "Celery"],
            "frontend": ["React 19", "TypeScript", "Tailwind CSS", "Responsive Design"],
            "payments": ["Direct Stripe Integration", "Zero Platform Fees", "Custom Donation Flow"],
            "deployment": ["Docker", "Fly.io", "Netlify", "Professional CI/CD"],
            "features": ["Custom Email System", "Documentary Integration", "Real-time Analytics"]
        },
        "problem": "GoFundMe made it nearly impossible to access my own fundraised money, took percentage cuts on donations meant for my medical needs, offered zero customer service when problems arose, and their refund policies almost cost us $26,000 that donors intended for my care and housing.",
        "solution": "Built a completely independent donation platform with React 19 + TypeScript frontend, Django REST Framework backend, direct Stripe integration bypassing all middleman fees, custom Celery-powered email system, and complete control over donor data and funds.",
        "special_features": [
            "Direct Stripe integration with zero platform fees (100% of donations reach recipient)",
            "React 19 + TypeScript SPA with modern responsive design",
            "Custom Celery email automation system for donor communication",
            "Professional documentary integration with seamless video embedding",
            "Real-time donation tracking and analytics dashboard",
            "Complete donor data ownership and privacy protection",
            "Mobile-optimized donation flow with accessibility features",
            "PostgreSQL + Redis infrastructure for enterprise-level reliability"
        ],
        "problems_solved": [
            "Eliminated predatory platform fees that siphon money from medical fundraisers",
            "Removed withdrawal restrictions and bureaucratic barriers to accessing funds",
            "Provided immediate access to donations without arbitrary hold periods",
            "Created transparent donor communication without platform censorship",
            "Built sustainable funding solution independent of third-party policy changes",
            "Established complete legal and financial control over fundraising operations"
        ],
        "improvements": [
            "Add recurring donation subscription options",
            "Integrate cryptocurrency payment methods",
            "Build donor portal for contribution history and tax receipts",
            "Add social media sharing optimization and viral mechanics",
            "Implement advanced donor analytics and engagement tracking"
        ],
        "proud_of": [
            "Saved $26,000 from GoFundMe's predatory policies through technical innovation",
            "Built enterprise-grade donation platform as a quadriplegic using adaptive technology",
            "Created sustainable funding model that eliminates exploitative middlemen",
            "Shipped production-ready React + Django architecture under extreme time pressure",
            "Turned institutional barriers into opportunities for technical problem-solving",
            "Delivered 100% fee-free donations directly to medical and housing needs"
        ],
        "build_notes": "<p>This platform represents a complete rebellion against exploitative fundraising platforms. Built using modern React 19 with TypeScript for type safety, Django REST Framework for robust API architecture, and direct Stripe integration to eliminate all middleman fees. The Celery email system ensures reliable donor communication, while the documentary integration provides professional storytelling capabilities. Deployed across Fly.io and Netlify for maximum reliability and performance.</p>",
        "github_url": "https://github.com/mattyray/fundraiser-website",
        "live_url": "https://www.mattsfreedomfundraiser.com",
        "video_url": "https://youtu.be/ZumlW-noN6E"
    },
    {
        "title": "AI Chat Widget (Open Source)",
        "slug": "chat-widget",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173483/django-chatwidget_tpyjby.jpg",
        "description": "A pip-installable Django package that adds a floating OpenAI-powered chat widget to any site.",
        "overview": "Built for storytelling and onboarding, this widget is fully open-source, customizable, and bundled with Twine for PyPI distribution. It's designed to help others create AI-enhanced web experiences.",
        "tech_stack": {
            "backend": ["Django", "Python", "OpenAI SDK", "Docker"],
            "frontend": ["Bootstrap 5", "JavaScript"],
            "deployment": ["Heroku", "Docker"],
            "tools": ["Twine", "Markdown", "JSON knowledge base"]
        },
        "problem": "I needed an easy way to share my story and resources interactively through an AI assistant embedded on my site.",
        "solution": "Created a floating chat widget backed by OpenAI, styled with Bootstrap, and deployed via PyPI as a reusable Django app.",
        "special_features": [
            "OpenAI API integration",
            "Floating widget UI with knowledge base",
            "Markdown support and chat history handling"
        ],
        "problems_solved": [
            "Enabled interactive onboarding and storytelling",
            "Offered a reusable template for AI-enhanced web UX"
        ],
        "improvements": [
            "Add persistence via user sessions or Firebase",
            "Enable audio output with text-to-speech"
        ],
        "proud_of": [
            "Published as a PyPI package with clean setup",
            "Useful as both a teaching tool and real product"
        ],
        "build_notes": "<p>Packaged with <code>twine</code>, includes JSON knowledge base ingestion and OpenAI GPT integration. Currently being tested in multiple live environments.</p>",
        "github_url": "https://github.com/mattyray/django-chatwidget",
        "live_url": "https://mattsfreedomfundraiser.com"
    },
    {
        "title": "Work Order Manager (React + Django)",
        "slug": "workorder-app",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173520/react-workorders_u14tws.jpg",
        "description": "A modern React + Django app for managing work orders, scheduling, and client jobs.",
        "overview": "A fully decoupled frontend and backend application for tracking work orders in real time, built with Django REST Framework and React using Vite + Tailwind CSS.",
        "tech_stack": {
            "backend": ["Django 5.1.6", "DRF", "PostgreSQL", "Docker"],
            "frontend": ["React", "Vite", "Tailwind CSS", "Axios"],
            "deployment": ["Heroku (API)", "Netlify (Frontend)", "Docker Compose"],
            "tools": ["WeasyPrint", "FullCalendar", "environs"]
        },
        "problem": "Managing client jobs and scheduling was inefficient and required a responsive, modern interface.",
        "solution": "Built a responsive single-page React frontend with REST API integration, dynamic work order creation, scheduling calendar, and PDF generation.",
        "special_features": [
            "Separate React + Django architecture",
            "PDF generation for work orders (WeasyPrint)",
            "Tailwind UI and dynamic event syncing"
        ],
        "problems_solved": [
            "Improved job tracking and scheduling",
            "Streamlined client communication with printable summaries"
        ],
        "improvements": [
            "Add notifications for due dates",
            "Integrate role-based permissions and team accounts"
        ],
        "proud_of": [
            "Seamless full-stack pipeline from UI to PDF export",
            "Smooth React-to-DRF integration with token auth"
        ],
        "build_notes": "<p>Backend on Heroku using Docker. Frontend on Netlify with Vite build. Axios used for API communication, and PDF output handled via WeasyPrint on the backend.</p>",
        "github_url": "https://github.com/mattyray/django-react-workorders",
    },
    {
        "title": "Matt's Bookstore API",
        "slug": "bookstore",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173585/bookstore_vw3vop.jpg",
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
    },
    {
        "title": "AI Motivational Chatbot",
        "slug": "motivational-chatbot",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173587/motivational-chatbot_b2e8qv.jpg",
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
    },
    {
        "title": "Lotus Path Learning Platform",
        "slug": "lotus-path",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173586/lotus-path_qvzp4w.jpg",
        "description": "An AI-powered learning platform offering custom tutorials, quizzes, and user-authenticated progress tracking.",
        "overview": "An interactive web app that generates AI-written tutorials, hosts quizzes, and lets users track progress with a personalized dashboard. Built with Django, integrated with OpenAI, and deployed on Fly.io.",
        "tech_stack": {
            "backend": ["Django 5.1.6", "Python 3.10", "PostgreSQL", "Docker"],
            "frontend": ["Bootstrap 5", "Crispy Forms"],
            "deployment": ["Fly.io", "Docker Compose", "Whitenoise"],
            "tools": ["django-environ", "OpenAI API", "CKEditor", "GitHub Actions"]
        },
        "problem": "Learners often struggle to find clear, custom-tailored explanations of programming topics and have no simple way to test themselves or track their growth.",
        "solution": "The platform allows users to generate AI-driven tutorials on demand, take JavaScript quizzes, and store their learning history via user accounts. It's optimized for accessibility and clarity.",
        "special_features": [
            "OpenAI-powered tutorial generation engine",
            "JavaScript quiz module with Django views and templates",
            "Authentication system with user dashboards and CSRF security",
            "Styled using Bootstrap with reusable templates and layout blocks"
        ],
        "problems_solved": [
            "Manual content creation bottlenecks",
            "Lack of personalized study support",
            "Difficulty integrating AI into a structured learning flow"
        ],
        "improvements": [
            "Add real-time chat tutoring via OpenAI API",
            "Allow users to bookmark and rate tutorials",
            "Enable code submission and validation for interactive practice"
        ],
        "proud_of": [
            "Integrated OpenAI API into a real Django application",
            "Configured secure, production-ready deployment using Fly.io and Docker",
            "Set up GitHub Actions for CI/CD with collectstatic and migrations"
        ],
        "build_notes": "<p>Deployed on Fly.io using Docker. Static files handled via Whitenoise. PostgreSQL database with `.env` integration via <code>django-environ</code>. Includes CKEditor for WYSIWYG content editing.</p>",
        "github_url": "https://github.com/mattyray/news-root",
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