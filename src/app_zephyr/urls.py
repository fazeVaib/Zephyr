from django.urls import path
from .views import (indexView,
                    dataPageView,
                    LiveDataView,
                    StatisticsView,
                    StatisticsDataView,
                    DailyDataView,
                    MonthlyDataView,
                    YearlyDataView,
                    DatabaseDailyPredictedDatafill,
                    DatabaseMonthlyPredictedDatafill,
                    DatabaseYearlyPredictedDatafill,
                    # , Index
                    )

urlpatterns = [
    # path('', Index.as_view()),
    path('', indexView, name="index"),
    path('data', dataPageView, name="data-page"),
    path('live-data', LiveDataView.as_view()),
    path('statistics', StatisticsView.as_view()),
    path('statistics-data', StatisticsDataView.as_view()),
    path('daily-pred', DailyDataView.as_view()),
    path('monthly-pred', MonthlyDataView.as_view()),
    path('yearly-pred', YearlyDataView.as_view()),
    path('database-dailyfill', DatabaseDailyPredictedDatafill.as_view()),
    path('database-monthlyfill', DatabaseMonthlyPredictedDatafill.as_view()),
    path('database-yearlyfill', DatabaseYearlyPredictedDatafill.as_view()),
]
