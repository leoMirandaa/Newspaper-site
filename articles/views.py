from distutils.log import Log
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
  ListView,
  DetailView
)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles/list.html"


# class MainArticlesListView(ArticleListView):

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_list"] = Article.objects.filter(
#             section="1).order_by("created_on").reverse()

class SportsArticleListView(ArticleListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Article.objects.filter(
        section=1).order_by("created_on").reverse()
        context['section']= "Sports"
        return context

class SocialArticleListView(ArticleListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Article.objects.filter(
        section=2).order_by("created_on").reverse()
        context['section']= "Social"

        return context

class EntertainmentArticleListView(ArticleListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Article.objects.filter(
        section=3).order_by("created_on").reverse()
        context['section']= "Entertainment"

        return context

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "articles/detail.html"
    fields = ['title', 'section', 'body']


class ArticlesCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Article
    template_name = "articles/new.html"
    fields = '__all__'
    success_url = reverse_lazy('articles')

    def test_func(self):
        print('********** ',self.request.user.role.id)
        return self.request.user.role.id > 1

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Article
    template_name = "articles/update.html"
    fields = '__all__'
    # success_url = reverse_lazy('articles')

    def test_func(self):
        if self.request.user.role.id > 1:
            article = self.get_object()
            return article.author == self.request.user
        return False

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy('articles')

    def test_func(self):
        if self.request.user.role.id > 1:
            article = self.get_object()
            return article.author == self.request.user
        return False
