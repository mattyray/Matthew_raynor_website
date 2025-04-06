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
                "title": "Matthew Raynor Finds A New Lease On Life Through Art",
                "source": "27East",
                "link": "https://www.27east.com/arts/matthew-raynor-finds-a-new-lease-on-life-through-art-1506186/",
                "summary": "Explores Matthew’s journey into photography and art exhibitions as a healing practice following his spinal cord injury.",
                "image_url": "https://source.unsplash.com/400x250/?art,healing"
            },
            {
                "title": "Matthew Raynor Photography At Southampton Cultural Center",
                "source": "27East",
                "link": "https://www.27east.com/arts/matthew-raynor-photography-at-southampton-cultural-center-1738556/",
                "summary": "Announces Matthew’s photography exhibition at SCC, showcasing both pre- and post-injury artwork including aerial prints.",
                "image_url": "https://source.unsplash.com/400x250/?gallery,photography"
            },
            {
                "title": "Before and After: Matt Raynor’s Life and Its Unexpected Turns",
                "source": "27East",
                "link": "https://www.27east.com/southampton-press/before-and-after-matt-raynors-life-and-its-unexpected-turns-chronicled-in-new-photography-book-2294539/",
                "summary": "Covers Matthew’s memoir 'Before Me<>After Me,' documenting his transformation from fisherman to developer and artist.",
                "image_url": "https://source.unsplash.com/400x250/?book,portrait"
            },
            {
                "title": "Matthew Raynor Exhibits His Art at LTV Studios",
                "source": "27East",
                "link": "https://www.27east.com/arts/matthew-raynor-exhibits-his-art-at-ltv-studios-2249981/",
                "summary": "Features Matthew’s first art show in East Hampton with drone and oceanic works on display at LTV.",
                "image_url": "https://source.unsplash.com/400x250/?studio,exhibit"
            },
            {
                "title": "Man Paralyzed While Diving Has No Health Aide: 'This Is A Crisis'",
                "source": "Patch",
                "link": "https://patch.com/new-york/westhampton-hamptonbays/man-paralyzed-while-diving-has-no-health-aide-crisis",
                "summary": "Details the healthcare crisis Matthew faced post-accident and community responses to his struggle for daily care.",
                "image_url": "https://source.unsplash.com/400x250/?hospital,crisis"
            },
            {
                "title": "Man Paralyzed In Diving Accident Finds Hope In Art — But Needs Help",
                "source": "Patch",
                "link": "https://patch.com/new-york/westhampton-hamptonbays/man-paralyzed-diving-accident-finds-hope-art-needs-help",
                "summary": "Covers Matthew’s emotional and financial journey toward healing through art after his spinal injury.",
                "image_url": "https://source.unsplash.com/400x250/?hope,recovery"
            },
            {
                "title": "Get Matty Ray Back On The Bay",
                "source": "Dan’s Papers",
                "link": "https://www.danspapers.com/2019/07/get-matty-ray-back-on-the-bay/",
                "summary": "Highlights an early fundraiser to support Matthew’s recovery and return to independence post-injury.",
                "image_url": "https://source.unsplash.com/400x250/?fundraiser,community"
            },
            {
                "title": "The Matthew Raynor Story (PechaKucha Presentation)",
                "source": "PechaKucha.com",
                "link": "https://www.pechakucha.com/presentations/the-matthew-raynor-story",
                "summary": "Matthew shares his transformation in a video talk—from seafarer to artist and motivational storyteller.",
                "image_url": "https://source.unsplash.com/400x250/?presentation,story"
            },
            {
                "title": "Matt Raynor: A Creative Journey",
                "source": "MILK Books",
                "link": "https://www.milkbooks.com/blog/your-stories/matt-raynor-a-creative-journey/",
                "summary": "An inspiring feature on Matthew’s use of photography and publishing to heal and inspire others.",
                "image_url": "https://source.unsplash.com/400x250/?creative,journal"
            },
        ]
        return context
