from distutils.log import Log
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    RedirectView,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import Investigator


def get_investigator(user):
    return Investigator.objects.get_or_create(user=user)[0]


class InvestigatorCreateView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return "/accounts/login"
        return f"/investigator/{get_investigator(self.request.user).pk}/edit"


class InvestigatorListView(ListView):
    template_name = "investigator/list.html"
    model = Investigator
    context_object_name = "investigators"


class InvestigatorDetailView(DetailView):
    template_name = "investigator/detail.html"
    model = Investigator
    context_object_name = "investigator"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        investigator = kwargs.get("investigator")
        kwargs.update(dict(articles_investigated=investigator.articles))
        return kwargs


class InvestigatorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "investigator/edit.html"
    model = Investigator
    fields = "__all__"
    success_url = reverse_lazy("investigator_list")


class InvestigatorDeleteView(LoginRequiredMixin, DeleteView):
    model = Investigator
    template_name = "investigator/delete.html"
    success_url = reverse_lazy("investigator_list")


class InvestigatorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return "/investigator"
        return f"/investigator/{get_investigator(self.request.user).pk}"
