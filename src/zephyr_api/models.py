from django.db import models


class ZephyrDailyAPI(models.Model):
    daily_city = models.CharField(max_length=100, null=True, blank=True)
    daily_date = models.CharField(max_length=20, null=True, blank=True)
    daily_aqi = models.FloatField(null=True, blank=True)
    daily_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    daily_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'ZephyrDailyAPI'


class ZephyrMonthlyAPI(models.Model):
    monthly_city = models.CharField(max_length=100, null=True, blank=True)
    monthly_date = models.CharField(max_length=20, null=True, blank=True)
    monthly_aqi = models.FloatField(null=True, blank=True)
    monthly_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    monthly_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'ZephyrMonthlyAPI'


class ZephyrYearlyAPI(models.Model):
    yearly_city = models.CharField(max_length=100, null=True, blank=True)
    yearly_date = models.CharField(max_length=20, null=True, blank=True)
    yearly_aqi = models.FloatField(null=True, blank=True)
    yearly_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    yearly_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'ZephyrYearlyAPI'
