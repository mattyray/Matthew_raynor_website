from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

def custom_logout(request):
    """Logs out the user and redirects to the homepage."""
    print("🚀 custom_logout was called!")
    request.session.flush()  # Clears session data manually
    logout(request)
    return redirect("/")  # Redirect to the root URL explicitly

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("account_login")  # Redirect to login page after sign-up
    template_name = "account/signup.html"




class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "account/dashboard.html"