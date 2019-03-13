from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .stats import get_stat_data
from .daily_predicted_data_delhi import get_daily_delhi_pred
from .monthly_predicted_data import get_monthly_pred
from .yearly_predicted_data import get_yearly_pred
from .live_data import get_live_data
from pprint import pprint
from .models import CityName
from zephyr.settings import BASE_DIR
from zephyr_api.models import ZephyrDailyAPI, ZephyrMonthlyAPI, ZephyrYearlyAPI
import os
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# class Index(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(requests, "app_zephyr/index.html", context)
#
#     def post(self, requests, *args, **kwargs):
#         city_n = requests.POST.get("clickedCity")
#         print(city_n)
#         q_set = CityName.objects.filter(id=1)
#         if q_set.count() != 0:
#             obj = q_set.first()
#         obj.city = city_n
#         obj.save()
#         context = {}
#         return render(request, "app_zephyr/index.html", context)


@csrf_exempt
def indexView(request, *args, **kwargs):
    if request.method == "GET":
        context = {}
        print(BASE_DIR)
        return render(request, "app_zephyr/index.html", context)
    elif request.method == "POST":
        city_n = request.POST.get("clickedCity")
        print(city_n)
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            obj = q_set.first()
        obj.city = city_n
        obj.save()
        context = {}
        return render(request, "app_zephyr/index.html", context)


@csrf_exempt
def dataPageView(request, *args, **kwargs):
    if request.method == "GET":
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        live_data = get_live_data(city)
        print(live_data)
        context = {
            "city_name": city,
            "data": live_data
        }
        return render(request, "app_zephyr/second.html", context)
    elif request.method == "POST":
        pass


class LiveDataView(View):
    def get(self, request, *args, **kwargs):
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        live_data = get_live_data(city)
        # pprint(stat_data)
        return JsonResponse(live_data, safe=False)


class DailyDataView(View):
    def get(self, request, *args, **kwargs):
        daily_delhi_pred = get_daily_delhi_pred(BASE_DIR)
        # pprint(daily_delhi_pred)
        return JsonResponse(daily_delhi_pred)


class MonthlyDataView(View):
    def get(self, request, *args, **kwargs):
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        monthly_data = get_monthly_pred(city, BASE_DIR)
        # pprint(monthly_data)
        return JsonResponse(monthly_data)


class YearlyDataView(View):
    def get(self, request, *args, **kwargs):
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        # monthly_data = get_monthly_pred(city)
        yearly_data = get_yearly_pred(city, BASE_DIR)
        # pprint(yearly_data)
        return JsonResponse(yearly_data)


class StatisticsDataView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse("<h1> This is the Home Page. </h1>")
        stat_data = get_stat_data(BASE_DIR)
        # pprint(stat_data)
        return JsonResponse(stat_data)


class StatisticsView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse("<h1> This is the Home Page. </h1>")
        stat_data = get_stat_data(BASE_DIR)
        # pprint(stat_data)
        return render(request, "app_zephyr/sidebar.html", stat_data)


class DatabaseDailyPredictedDatafill(View):
    def get(self, request, *args, **kwargs):
        # qs = ZephyrDailyAPI.objects.all()
        # for i in qs:
        #     print(i, type(i), i.daily_updated)
        #     i.delete()
        #     print("Object deleted")
        # df = pd.read_csv("/media/rishi/01D3D31D70AD1520/MINOR_PROJECT/zephyr_project/src/app_zephyr/daily_predicted_data_delhi/predicted_delhi.csv")
        # print(df.count())
        # print(df.values)
        # c = 0
        # for j in df.values:
        #     print(j[0], j[1])
        #     obj = ZephyrDailyAPI()
        #     obj.daily_city = "Delhi"
        #     obj.daily_date = j[0]
        #     obj.daily_aqi = j[1]
        #     obj.save()
        #     print(c)
        #     print("================================")
        #     c += 1
        # print(c)
        return HttpResponse("<h1> This is the Database Daily Predicted Data Fill Page. </h1>")


class DatabaseMonthlyPredictedDatafill(View):
    def get(self, request, *args, **kwargs):
        # qs = ZephyrMonthlyAPI.objects.all()
        # for i in qs:
        #     # print(i, type(i), i.daily_updated)
        #     i.delete()
        #     # print("Object deleted")
        # folder_path = "/media/rishi/01D3D31D70AD1520/MINOR_PROJECT/zephyr_project/src/app_zephyr/monthly_predicted_data/"
        # dirs = os.listdir(
        #     "/media/rishi/01D3D31D70AD1520/MINOR_PROJECT/zephyr_project/src/app_zephyr/monthly_predicted_data")
        # # print(dirs)
        # # c = 0
        # for i in dirs:
        #     # print(folder_path+i)
        #     df = pd.read_csv(folder_path + i)
        #     # print(i[5:-4])
        #     # print(df.count())
        #     # print(df.values)
        #     for j in df.values:
        #         # print(j[0], j[6], i[5:-4])
        #         obj = ZephyrMonthlyAPI()
        #         obj.monthly_city = i[5:-4]
        #         obj.monthly_date = j[0]
        #         obj.monthly_aqi = j[6]
        #         obj.save()
        #     # print(c)
        #     # print("================================")
        #     # c += 1
        # # print(c)
        return HttpResponse("<h1> This is the Database Monthly Predicted Data Fill Page. </h1>")


class DatabaseYearlyPredictedDatafill(View):
    def get(self, request, *args, **kwargs):
        # qs = ZephyrYearlyAPI.objects.all()
        # for i in qs:
        #     # print(i, type(i), i.daily_updated)
        #     i.delete()
        #     # print("Object deleted")
        # folder_path = "/media/rishi/01D3D31D70AD1520/MINOR_PROJECT/zephyr_project/src/app_zephyr/yearly_predicted_data/"
        # dirs = os.listdir(
        #     "/media/rishi/01D3D31D70AD1520/MINOR_PROJECT/zephyr_project/src/app_zephyr/yearly_predicted_data")
        # # print(dirs)
        # # c = 0
        # for i in dirs:
        #     # print(folder_path+i)
        #     df = pd.read_csv(folder_path + i)
        #     # print(i[5:-4])
        #     # print(df.count())
        #     # print(df.values)
        #     for j in df.values:
        #         # print(j[0], j[6], i[5:-4])
        #         obj = ZephyrYearlyAPI()
        #         obj.yearly_city = i[5:-4]
        #         obj.yearly_date = j[0]
        #         obj.yearly_aqi = j[6]
        #         obj.save()
        #     # print(c)
        #     # print("================================")
        #     # c += 1
        # # print(c)
        return HttpResponse("<h1> This is the Database Yearly Predicted Data Fill Page. </h1>")
