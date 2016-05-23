from rest_framework import viewsets
from apiv1 import serializers, models


class CountyView(viewsets.ModelViewSet):
    queryset = models.County.objects.all()
    serializer_class = serializers.CountySerializer


class HousingView(viewsets.ModelViewSet):
    queryset = models.Housing.objects.all()
    serializer_class = serializers.HousingSerializer


class SchoolMealView(viewsets.ModelViewSet):
    queryset = models.SchoolMeal.objects.all()
    serializer_class = serializers.SchoolMealSerializer


class CostOfMealView(viewsets.ModelViewSet):
    queryset = models.CostOfMeal.objects.all()
    serializer_class = serializers.CostOfMealSerializer
