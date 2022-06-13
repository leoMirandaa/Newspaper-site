from django.urls import path

from . import views

urlpatterns = [
  # path('main/', views.MainArticlesListView.as_view(), name="main_list"),
  path('sports/', views.SportsArticleListView.as_view(), name="sports_list"),
  path('social/', views.SocialArticleListView.as_view(), name="social_list"),
  path('entertainment/', views.EntertainmentArticleListView.as_view(), name="enternainment_list"),

  path('', views.ArticleListView.as_view(), name="articles"),
  path('new/', views.ArticlesCreateView.as_view(), name="new-article"),
  path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
  path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='update-article'),
  path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name='delete-article'),
]