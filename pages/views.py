from django.views.generic import TemplateView
from blog.models import Post  # For recent blog posts on the homepage

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add 3 most recently updated published posts
        context["recent_posts"] = Post.objects.filter(is_published=True).order_by('-updated_date')[:3]
        return context


class PressPageView(TemplateView):
    template_name = "pages/press.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["press_articles"] = [
            {
                "title": "Matthew Raynor: From Fisherman to Developer, A Story of Grit and Code",
                "source": "Newsday",
                "link": "https://www.newsday.com/long-island/matthew-raynor-fisherman-developer",
                "summary": "Explores Matthew’s transformation from commercial fisherman to self-taught coder after becoming a quadriplegic.",
            },
            {
                "title": "Southampton Quadriplegic Inspires Others With Programming Projects",
                "source": "Patch – Southampton Edition",
                "link": "https://patch.com/new-york/southampton/southampton-quadriplegic-inspires-others-programming-projects",
                "summary": "Details how Matthew overcame disability through tech and motivational content creation.",
            },
            {
                "title": "Local Man Turns Tragedy Into Triumph With Self-Taught Coding Career",
                "source": "27East – The Southampton Press",
                "link": "https://www.27east.com/southampton-press/local-man-turns-tragedy-into-triumph-with-coding-214982/",
                "summary": "Focuses on Matthew’s growth as a developer and transition out of the nursing home.",
            },
            {
                "title": "Matthew Raynor Finds A New Lease On Life Through Art",
                "source": "27East – Arts Feature",
                "link": "https://www.27east.com/arts/matthew-raynor-finds-a-new-lease-on-life-through-art-1506186/",
                "summary": "Explores Matthew’s journey into photography and art exhibitions as a healing practice.",
            },
            {
                "title": "Man Paralyzed In Diving Accident Finds Hope In Art — But Needs Help",
                "source": "Patch – Westhampton-Hampton Bays Edition",
                "link": "https://patch.com/new-york/westhampton-hamptonbays/man-paralyzed-diving-accident-finds-hope-art-needs-help",
                "summary": "Highlights the emotional and financial challenges Matthew faced after his accident and his pursuit of meaning through art.",
            },
            {
                "title": "Matthew Raynor Turns Sight From Sea To Sky Through Drone Photography",
                "source": "27East – Arts Feature",
                "link": "https://www.27east.com/arts/matthew-raynor-turns-sight-from-sea-to-sky-through-drone-photography-1725543/",
                "summary": "Details Matthew’s use of drones to explore photography and healing after his injury.",
            },
            {
                "title": "Matthew Raynor Art Exhibit Opens At LTV",
                "source": "James Lane Post",
                "link": "https://jameslanepost.com/matthew-raynor-art-exhibit-opens-at-ltv",
                "summary": "Announces Matthew’s exhibit at LTV Studios, showcasing photography and mixed media work.",
            },
            {
                "title": "Get Matty Ray Back On The Bay",
                "source": "Dan’s Papers",
                "link": "https://danspapers.com/2019/07/get-matty-ray-back-on-the-bay",
                "summary": "A look at the early fundraising efforts and community support for Matthew after his injury.",
            },
        ]
        return context
