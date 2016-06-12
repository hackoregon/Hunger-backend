from apiv1 import models
from rest_framework import serializers


class CountySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.County
