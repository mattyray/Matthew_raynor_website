from django.views.generic import TemplateView

class PortfolioView(TemplateView):
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = [
            {
                "title": "MatthewRaynor.com",
                "summary": "My flagship personal site: blog, store, press, portfolio, and custom accounts system—all built with Django and Docker.",
                "tech": ["Django", "Bootstrap", "Docker", "SASS"],
                "github": "https://github.com/yourusername/matthewraynor.com",
                "live": "https://www.matthewraynor.com",
                "image": "/static/images/portfolio/matthewraynor-site.png",
            },
            {
                "title": "Art Mover App",
                "summary": "A logistics dashboard for work orders, invoicing, scheduling, and client tracking—built for real business use.",
                "tech": ["Django", "PostgreSQL", "Bootstrap"],
                "github": "https://github.com/yourusername/art-mover-app",
                "live": "https://artmover.matthewraynor.com",
                "image": "/static/images/portfolio/art-mover.png",
            },
            {
                "title": "Bookstore API",
                "summary": "REST API with user authentication, reviews, image uploads, and Dockerized production.",
                "tech": ["Django Rest Framework", "Docker"],
                "github": "https://github.com/yourusername/bookstore-api",
                "live": "https://bookstore.matthewraynor.com",
                "image": "/static/images/portfolio/bookstore.png",
            },
            {
                "title": "Fundraiser Website",
                "summary": "Donation site with blogging, embedded videos, and contact features, styled like GoFundMe.",
                "tech": ["Django", "Bootstrap", "Heroku"],
                "github": "https://github.com/yourusername/fundraiser-site",
                "live": "https://freematt.matthewraynor.com",
                "image": "/static/images/portfolio/fundraiser.png",
            },
        ]
        return context
