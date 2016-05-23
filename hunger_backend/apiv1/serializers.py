from apiv1 import models
from rest_framework import serializers


class CountySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.County
        fields = ('fips', 'name', 'housing', 'school_meal',
                  'cost_of_meal')
        depth = 1


class HousingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Housing
        fields = ('median_housing_one', 'median_housing_three',
                  'median_housing_four')


class SchoolMealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SchoolMeal
        fields = ('meal_supplement_in_dollar',)


class CostOfMealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CostOfMeal
        fields = ('meal_cost_one', 'meal_cost_three', 'meal_cost_four')
