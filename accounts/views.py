from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout, get_user_model
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Example: Pass profile info, orders, and reviews
        # context['orders'] = Order.objects.filter(user=self.request.user)
        # context['reviews'] = Review.objects.filter(user=self.request.user)
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = "account/profile_edit.html"
    success_url = reverse_lazy("dashboard")

    def get_object(self):
        return self.request.user


