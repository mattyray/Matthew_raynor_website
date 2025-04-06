from django.views.generic import TemplateView
from blog.models import Post  # For recent blog posts on the homepage

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
                "summary": "A deep feature on Matthew’s transformation from deep-sea fisherman to self-taught coder after a tragic accident that left him paralyzed. The story explores his rebirth through technology and creativity.",
                "image_url": "https://source.unsplash.com/400x250/?ocean,coding"
            },
            {
                "title": "Southampton Quadriplegic Inspires Others With Programming Projects",
                "source": "Patch – Southampton Edition",
                "link": "https://patch.com/new-york/southampton/southampton-quadriplegic-inspires-others-programming-projects",
                "summary": "How Matthew overcame the odds to create software and digital tools, serving as an inspiration for disabled individuals and the broader development community.",
                "image_url": "https://source.unsplash.com/400x250/?inspiration,tech"
            },
            {
                "title": "Local Man Turns Tragedy Into Triumph With Self-Taught Coding Career",
                "source": "27East – The Southampton Press",
                "link": "https://www.27east.com/southampton-press/local-man-turns-tragedy-into-triumph-with-coding-214982/",
                "summary": "This article covers Matthew's powerful story of rebuilding his life through resilience, coding, and a rediscovered love for creative self-expression.",
                "image_url": "https://source.unsplash.com/400x250/?recovery,resilience"
            },
            {
                "title": "Matthew Raynor Finds A New Lease On Life Through Art",
                "source": "27East – Arts Feature",
                "link": "https://www.27east.com/arts/matthew-raynor-finds-a-new-lease-on-life-through-art-1506186/",
                "summary": "From canvas to code, Matthew’s creative journey includes photography exhibits that give voice to his inner transformation.",
                "image_url": "https://source.unsplash.com/400x250/?art,photography"
            },
            {
                "title": "Man Paralyzed In Diving Accident Finds Hope In Art — But Needs Help",
                "source": "Patch – Westhampton-Hampton Bays Edition",
                "link": "https://patch.com/new-york/westhampton-hamptonbays/man-paralyzed-diving-accident-finds-hope-art-needs-help",
                "summary": "A heartfelt exploration of Matthew’s journey after injury and the urgent call for community support in helping him find new purpose through art and tech.",
                "image_url": "https://source.unsplash.com/400x250/?hope,community"
            },
            {
                "title": "Matthew Raynor Turns Sight From Sea To Sky Through Drone Photography",
                "source": "27East – Arts Feature",
                "link": "https://www.27east.com/arts/matthew-raynor-turns-sight-from-sea-to-sky-through-drone-photography-1725543/",
                "summary": "Using drones and a creative eye, Matthew captures breathtaking views of the ocean—transcending limits and expressing freedom through flight.",
                "image_url": "https://source.unsplash.com/400x250/?drone,ocean"
            },
            {
                "title": "Matthew Raynor Art Exhibit Opens At LTV",
                "source": "James Lane Post",
                "link": "https://jameslanepost.com/matthew-raynor-art-exhibit-opens-at-ltv",
                "summary": "This piece highlights the opening of Matthew’s art show, celebrating his journey through stunning aluminum prints and stories behind each frame.",
                "image_url": "https://source.unsplash.com/400x250/?gallery,exhibit"
            },
            {
                "title": "Get Matty Ray Back On The Bay",
                "source": "Dan’s Papers",
                "link": "https://danspapers.com/2019/07/get-matty-ray-back-on-the-bay",
                "summary": "A grassroots campaign to help Matthew regain independence after injury, this article reflects early community love and support.",
                "image_url": "https://source.unsplash.com/400x250/?bay,support"
            },
        ]
        return context
