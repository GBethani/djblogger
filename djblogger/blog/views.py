from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.
class HomeView(ListView):
    model = models.Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'