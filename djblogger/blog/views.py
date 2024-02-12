from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.
class HomeView(ListView):
    model = models.Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 10  # Set the number of articles per page

    def get_queryset(self):
        return models.Article.objects.all().order_by('-date_created')