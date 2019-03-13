from django.db import models


class CityName(models.Model):
    city = models.CharField(max_length=200, null=True, blank=False)
