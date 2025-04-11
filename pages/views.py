from django.views.generic import TemplateView
from blog.models import Post  
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("✅ Message sent:", form.cleaned_data)
            messages.success(request, "Thanks for reaching out!")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})



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
                "summary": "Explores your transition into photography and art exhibitions as a form of healing and purpose.",
                "image_url": "https://image.27east.com/2019/08/8.15x10.65_BackofBoat2.jpg"
            },
            {
                "title": "Matthew Raynor Photography At Southampton Cultural Center",
                "source": "27East",
                "link": "https://www.27east.com/arts/matthew-raynor-photography-at-southampton-cultural-center-1738556/",
                "summary": "Highlights your stunning drone and seascape photography exhibit at the SCC, blending grit and serenity.",
                "image_url": "https://image.27east.com/2020/11/Matt-Raynor-beautifulbirch-scaled.jpg"
            },
            {
                "title": "Before and After: Matt Raynor’s Life and Its Unexpected Turns",
                "source": "27East",
                "link": "https://www.27east.com/southampton-press/before-and-after-matt-raynors-life-and-its-unexpected-turns-chronicled-in-new-photography-book-2294539/",
                "summary": "Covers your memoir 'Before Me<>After Me,' sharing your powerful personal transformation through imagery.",
                "image_url": "https://image.27east.com/2024/10/party-1.jpg"
            },
            {
                "title": "Matthew Raynor Exhibits His Art at LTV Studios",
                "source": "27East",
                "link": "https://www.27east.com/arts/matthew-raynor-exhibits-his-art-at-ltv-studios-2249981/",
                "summary": "Your LTV Studios debut showcasing new aluminum prints, textures, and emotional storytelling through art.",
                "image_url": "https://image.27east.com/2024/05/Matt-Raynor-Boardwalk.jpg"
            },
            {
                "title": "Man Paralyzed While Diving Has No Health Aide: 'This Is A Crisis'",
                "source": "Patch",
                "link": "https://patch.com/new-york/westhampton-hamptonbays/man-paralyzed-while-diving-has-no-health-aide-crisis",
                "summary": "A heartbreaking look at the challenges you faced accessing in-home care following your accident.",
                "image_url": "https://patch.com/img/cdn20/users/1296254/20190912/061810/styles/patch_image/public/matt___12164446739.jpg?width=1200"
            },
            {
                "title": "Man Paralyzed In Diving Accident Finds Hope In Art — But Needs Help",
                "source": "Patch",
                "link": "https://patch.com/new-york/westhampton-hamptonbays/man-paralyzed-diving-accident-finds-hope-art-needs-help",
                "summary": "Details your emotional and creative healing journey while raising awareness for support needs.",
                "image_url": "https://patch.com/img/cdn20/users/1296254/20230421/085742/styles/patch_image/public/matthewraynor___21200506825.jpg?width=1200"
            },
            {
                "title": "Get Matty Ray Back On The Bay",
                "source": "Dan’s Papers",
                "link": "https://www.danspapers.com/2019/07/get-matty-ray-back-on-the-bay/",
                "summary": "Early community support feature spotlighting your recovery and the fundraiser to aid your journey.",
                "image_url": "https://www.danspapers.com/wp-content/uploads/2020/11/matt-raynor-benefit.jpg"
            },
            {
                "title": "The Matthew Raynor Story (PechaKucha Presentation)",
                "source": "PechaKucha",
                "link": "https://www.pechakucha.com/presentations/the-matthew-raynor-story",
                "summary": "A visual storytelling presentation of your journey from fisherman to artist to speaker.",
                "image_url": ""  # You can use a placeholder here or skip the image conditionally in the template
            },
            {
                "title": "Matt Raynor: A Creative Journey",
                "source": "MILK Books",
                "link": "https://www.milkbooks.com/blog/your-stories/matt-raynor-a-creative-journey/",
                "summary": "A deeply personal narrative exploring how art, writing, and resilience fueled your transformation.",
                "image_url": "https://cdn.milkbooks.com/media/20640/5_2x.webp"
            },
        ]
        return context
