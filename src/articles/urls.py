from django.urls import path
from .views import Articles, ScrapeArticles

urlpatterns = [
    path('articles', Articles.as_view()),
    path('a-scrape', ScrapeArticles.as_view()),
]
