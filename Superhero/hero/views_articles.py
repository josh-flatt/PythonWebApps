from distutils.log import Log
from django.core.exceptions import PermissionDenied
from django.conf import settings
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
from .models import Superhero, Article, Investigator


class ArticleListView(ListView):
    template_name = "article/list.html"
    model = Article
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    template_name = "article/detail.html"
    model = Article
    context_object_name = "article"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/add.html"
    model = Article
    fields = "__all__"

    def form_valid(self, form):
        investigator_id = Investigator.objects.get_or_create(user=self.request.user)[0]
        form.instance.investigator = investigator_id
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article/edit.html"
    model = Article
    fields = "__all__"

    def dispatch(self, request, *args, **kwargs):
        article_user = self.get_object().investigator.user
        current_user = self.request.user
        if not self.request.user.is_superuser:
            if current_user != article_user:
                raise PermissionDenied()
        return super(ArticleUpdateView, self).dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "Article/delete.html"
    model = Article
    success_url = reverse_lazy("hero_list")

    def dispatch(self, request, *args, **kwargs):
        article_user = self.get_object().investigator.user
        current_user = self.request.user
        if not self.request.user.is_superuser:
            if current_user != article_user:
                raise PermissionDenied()
        return super(ArticleDeleteView, self).dispatch(request, *args, **kwargs)
