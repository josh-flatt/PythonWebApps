from distutils.log import Log
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import Author

def get_author(user):
    return Author.objects.get_or_create(user=user)[0]


class AuthorCreateView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/accounts/login'
        return f'/author/{get_author(self.request.user).pk}/edit'

class AuthorListView(ListView):
    template_name = 'author/list.html'
    model = Author
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    template_name = 'author/detail.html'
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        author = kwargs.get('author')
        kwargs.update(dict(articles_authored=author.articles))
        return kwargs

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'author/edit.html'
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author/delete.html'
    success_url = reverse_lazy('author_list')

class AuthorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/author'
        return f'/author/{get_author(self.request.user).pk}'