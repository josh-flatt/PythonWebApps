from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import Investigator, Photo


def get_investigator(user):
    return Investigator.objects.get_or_create(user=user)[0]

class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = "photo/add.html"
    model = Photo
    fields = '__all__'