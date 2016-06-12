from django.contrib import admin
from . import models


@admin.register(models.County)
class CountyAdmin(admin.ModelAdmin):
    pass
