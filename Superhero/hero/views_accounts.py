from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, RedirectView, View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import Investigator


def get_investigator(user):
    return Investigator.objects.get_or_create(user=user)[0]


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/edit.html"
    model = User
    fields = ["first_name", "last_name", "username", "email"]
    success_url = reverse_lazy("hero_list")


class LoginView(CreateView):
    template_name = "registration/login.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("hero_list")


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("investigator_add")


class LogoutView(View):
    template_name = "registration/logout.html"
    model = User

    def logout_view(request):
        logout(request)
        return redirect("hero")

    success_url = reverse_lazy("hero_list")


# class InvestigatorRegisterView(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         if self.request.user.is_anonymous:
#             return '/investigator'
#         return f'/investigator/{get_investigator(self.request.user).pk}/edit'
