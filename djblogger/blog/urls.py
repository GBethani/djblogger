from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('<slug>/',views.ArticleDetailView.as_view(),name="article-detail"),
    path('tag/<str:tag>/',views.TagPostListView.as_view(),name="tagged-posts"),
]