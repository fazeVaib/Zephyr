# api/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ZephyrDailyAPIViewSet, ZephyrMonthlyAPIViewSet, ZephyrYearlyAPIViewSet


router = DefaultRouter()

router.register(r'api-daily', ZephyrDailyAPIViewSet),
router.register(r'api-monthly', ZephyrMonthlyAPIViewSet),
router.register(r'api-yearly', ZephyrYearlyAPIViewSet),
# router.register(r'api_city', ZephyrCityAPIViewSet),

urlpatterns = router.urls
