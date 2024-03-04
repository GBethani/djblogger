# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
# Create your views here.
class HomeView(ListView):
    model = models.Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 10  # Set the number of articles per page

    def get_queryset(self):
        return models.Article.objects.all().order_by('-date_created')

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        article = context['article']
        related_posts = models.Article.objects.filter(tags__in=article.tags.all()).exclude(id=article.id).distinct()[:3]
        context['related_articles'] = related_posts
        return context

class TagPostListView(ListView):
    model = models.Article
    template_name = 'blog/posts_by_tag.html'
    paginate_by = 10
    context_object_name = 'posts_by_tag'

    def get_queryset(self):
        tag_name = self.kwargs['tag']
        return models.Article.objects.filter(tags__name=tag_name).order_by('-date_created',)
        