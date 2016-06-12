from rest_framework import viewsets
from apiv1 import serializers, models


class CountyView(viewsets.ModelViewSet):
    queryset = models.County.objects.all()
    serializer_class = serializers.CountySerializer
