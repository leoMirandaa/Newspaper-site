from django.urls import path
from .views import (
  ArticlesListView,
  ArticlesCreateView,
  ArticleUpdateView,
    ArticleDeleteView
)

urlpatterns = [
  path('', ArticlesListView.as_view(), name="articles"),
  path('new/', ArticlesCreateView.as_view(), name="new-article"),
  path('update/<int:pk>', ArticleUpdateView.as_view(), name='update-article'),
  path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete-article'),
]