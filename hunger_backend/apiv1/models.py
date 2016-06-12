from django.db import models
from django.contrib import admin

# Create your models here.


class County(models.Model):
    class Meta:
        verbose_name_plural = 'counties'

    fips = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    # Housing
    median_housing_one = models.FloatField()
    median_housing_three = models.FloatField()
    median_housing_four = models.FloatField()
    # School Meal
    meal_supplement_in_dollar = models.FloatField()
    # Cost of Meal
    cost_per_meal = models.FloatField()
    monthly_cost_one = models.FloatField()
    monthly_cost_three = models.FloatField()
    monthly_cost_four = models.FloatField()

    def __str__(self):
        return self.name
