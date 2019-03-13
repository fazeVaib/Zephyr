from django.contrib import admin
from .models import Article


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "link", "image"]
    list_filter = ["updated"]

    class Meta:
        model = Article


admin.site.register(Article, ArticleModelAdmin)
