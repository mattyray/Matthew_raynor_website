from django.views.generic import TemplateView
from django.http import Http404

PROJECTS = {
    "matthewraynor-com": {
        "title": "MatthewRaynor.com",
        "slug": "matthewraynor-com",
        "summary": "My flagship personal site: blog, store, press, portfolio, and custom accounts system—all built with Django and Docker.",
        "tech": ["Django", "Bootstrap", "Docker", "SASS", "PostgreSQL"],
        "github": "https://github.com/mattyray/Matthew_raynor_website",
        "live": "https://www.matthewraynor.com",
        "image": "/static/images/portfolio/matthewraynor-site.png",
        "details": "This site showcases my entire digital journey—from my memoir and aluminum prints to my blog, media features, and development portfolio. The design is fully responsive and built with custom SASS styling, deployed using Docker and Heroku.",
    },
    "art-mover-app": {
        "title": "Art Mover Application",
        "slug": "art-mover-app",
        "summary": "A logistics dashboard for work orders, invoicing, scheduling, and client tracking—built for real business use.",
        "tech": ["Django", "Bootstrap", "PostgreSQL", "Heroku", "Crispy Forms"],
        "github": "https://github.com/mattyray/art_moving_buisness",
        "live": "https://art-moving-buisness-0a734245a61f.herokuapp.com",
        "image": "/static/images/portfolio/art-mover.png",
        "details": "Built for a real art handling business, this app includes scheduling, client management, invoicing, calendar integration, PDF generation, and authentication. It’s fully styled and production-ready.",
    },
    "bookstore-api": {
        "title": "Matt’s Bookstore API",
        "slug": "bookstore-api",
        "summary": "REST-powered Django API with user accounts, book reviews, ratings, and Google login.",
        "tech": ["Django REST Framework", "Docker", "Heroku", "AllAuth"],
        "github": "https://github.com/mattyray/ch4-bookstore",
        "live": "https://mattsbookstore-c15521949514.herokuapp.com",
        "image": "/static/images/portfolio/bookstore.png",
        "details": "This bookstore API supports authenticated users, rating and reviewing books, and full CRUD functionality via DRF. Built using Docker and deployed to Heroku with environment variables.",
    },
    "fundraiser-website": {
        "title": "Fundraiser Website",
        "slug": "fundraiser-website",
        "summary": "Donation site with blogging, embedded videos, and storytelling tools—styled like GoFundMe.",
        "tech": ["Django", "Bootstrap", "Heroku", "PostgreSQL", "SASS"],
        "github": "https://github.com/mattyray/fundraiser-website",
        "live": "https://www.mattsfreedomfundraiser.com",
        "image": "/static/images/portfolio/fundraiser.png",
        "details": "Created to raise funds for my transition out of the nursing home, this website features blog posts, donation links, embedded video, and contact forms. Clean UI, real-world impact.",
    },
}

class PortfolioView(TemplateView):
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = PROJECTS.values()
        return context


class ProjectDetailView(TemplateView):
    template_name = "portfolio/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        project = PROJECTS.get(slug)

        if not project:
            raise Http404("Project not found.")

        context["project"] = project
        return context
