from django.db import models
from django.contrib import admin

# Create your models here.


class County(models.Model):
    class Meta:
        verbose_name_plural = 'counties'

    fips = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    #housing = models.ForeignKey('Housing')
    #school_meal = models.ForeignKey('SchoolMeal')
    #cost_of_meal = models.ForeignKey('CostOfMeal')

    def __str__(self):
        return self.name


class Housing(models.Model):
    fips = models.OneToOneField(County, primary_key=True)
    median_housing_one = models.FloatField()
    median_housing_three = models.FloatField()
    median_housing_four = models.FloatField()


class SchoolMeal(models.Model):
    fips = models.OneToOneField(County, primary_key=True,
                                related_name='school_meal')
    meal_supplement_in_dollar = models.FloatField()


class CostOfMeal(models.Model):
    fips = models.OneToOneField(County, primary_key=True,
                                related_name='cost_of_meal')
    cost_per_meal = models.FloatField()
    monthly_cost_one = models.FloatField()
    monthly_cost_three = models.FloatField()
    monthly_cost_four = models.FloatField()
