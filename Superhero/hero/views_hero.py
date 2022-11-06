from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Superhero, Author

class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = 'hero/add.html'
    model = Superhero
    fields = '__all__'

    def form_valid(self, form):
        author_id = Author.objects.get_or_create(user=self.request.user)[0]
        form.instance.author = author_id
        return super().form_valid(form)


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'hero/edit.html'
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'hero/delete.html'
    model = Superhero
    success_url = reverse_lazy('hero_list')