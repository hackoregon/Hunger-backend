from django.contrib import admin
from . import models


@admin.register(models.County)
class CountyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Housing)
class HousingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SchoolMeal)
class SchoolMealAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CostOfMeal)
class CostOfMealAdmin(admin.ModelAdmin):
    pass
