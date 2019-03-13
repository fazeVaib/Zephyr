from django.contrib import admin
from .models import CityName


class CityNameModelAdmin(admin.ModelAdmin):
    list_display = ["id", "city"]
    list_display_links = ["id"]


admin.site.register(CityName, CityNameModelAdmin)
