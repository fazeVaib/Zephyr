from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import ZephyrDailyAPI, ZephyrMonthlyAPI, ZephyrYearlyAPI


class ZephyrDailyAPISerializer(ModelSerializer):

    class Meta:
        model = ZephyrDailyAPI
        fields = '__all__'


class ZephyrDailyAPIViewSet(ReadOnlyModelViewSet):
    """
        list:
        Returns a list of all the existing data.

        read:
        Returns the data of a particular id.
    """
    queryset = ZephyrDailyAPI.objects.all()
    serializer_class = ZephyrDailyAPISerializer


# class ZephyrDailyAPIViewSet(ReadOnlyModelViewSet):
#     """
#         list:
#         Returns a list of all the existing data.
#
#         read:
#         Returns the data of a particular id.
#     """
#     queryset = ZephyrDailyAPI.objects.filter(city="delhi".capitalize())
#     serializer_class = ZephyrDailyAPISerializer


class ZephyrMonthlyAPISerializer(ModelSerializer):

    class Meta:
        model = ZephyrMonthlyAPI
        fields = '__all__'


class ZephyrMonthlyAPIViewSet(ReadOnlyModelViewSet):
    """
        list:
        Returns a list of all the existing data.

        read:
        Returns the data of a particular id.
    """
    queryset = ZephyrMonthlyAPI.objects.all()
    serializer_class = ZephyrMonthlyAPISerializer


class ZephyrYearlyAPISerializer(ModelSerializer):

    class Meta:
        model = ZephyrYearlyAPI
        fields = '__all__'


class ZephyrYearlyAPIViewSet(ReadOnlyModelViewSet):
    """
        list:
        Returns a list of all the existing data.

        read:
        Returns the data of a particular id.
    """
    queryset = ZephyrYearlyAPI.objects.all()
    serializer_class = ZephyrYearlyAPISerializer

