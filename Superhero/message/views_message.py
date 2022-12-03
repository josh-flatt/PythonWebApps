from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
)

from .models_message import Message


class MessageView(RedirectView):
    url = reverse_lazy("message_list")


class MessageListView(ListView):
    template_name = "message/list.html"
    model = Message
    context_object_name = "messages"


class MessageDetailView(DetailView):
    template_name = "message/detail.html"
    model = Message
    context_object_name = "message"

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     message = kwargs.get('message')
    #     kwargs['dependents'] = message.dependents
    #     return kwargs


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = "message/add.html"
    model = Message
    fields = "__all__"

    # def form_valid(self, form):
    #     form.instance.book = 1
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "message/edit.html"
    model = Message
    fields = "__all__"


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = "message/delete.html"
    success_url = reverse_lazy("message_list")
