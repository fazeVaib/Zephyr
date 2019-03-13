from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
