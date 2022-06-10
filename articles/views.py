from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  # DeleteView
)

from .models import Article

class ArticlesListView(ListView):
    model = Article
    template_name = "articles/list.html"


class ArticlesCreateView(CreateView):
    model = Article
    template_name = "articles/new.html"
    fields = '__all__'
    success_url = reverse_lazy('articles')

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "articles/update.html"
    fields = '__all__'
    success_url = reverse_lazy('articles')

# class ArticleDeleteView(DeleteView):
#     model = Article
#     template_name = "articles/delete.html"

