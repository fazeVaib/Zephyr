from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .articles_scrape import get_articles
from .models import Article


class Articles(View):
    def get(self, requests, *args, **kwargs):
        queryset = Article.objects.all()
        context = {
            "object_list": queryset,
            "title": "Articles"
        }
        return render(requests, "articles/articles.html", context)


class ScrapeArticles(View):
    def get(self, requests, *args, **kwargs):
        posts = get_articles()
        for i in range(len(posts)):
            article = Article()
            # print("Article: ", i + 1)
            try:
                article.title = posts[i].a.section.h3.text
                print(article.title)
            except:
                article.title = ""
                print(article.title)
            try:
                article.link = posts[i].a['href']
                print(article.link)
            except:
                article.link = ""
                print(article.link)
            try:
                article.image = posts[i].a.section.figure.img['src']
                print(article.image)
            except:
                article.image = ""
                print(article.image)
            article.save()
        context = {}
        return render(requests, "articles/scrape_articles.html", context)
