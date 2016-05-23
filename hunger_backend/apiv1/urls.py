from django.conf.urls import url, include
from rest_framework import routers
from apiv1 import views



router = routers.DefaultRouter()
router.register(r'counties', views.CountyView)
router.register(r'housing', views.HousingView)
router.register(r'schoolmeal', views.SchoolMealView)
router.register(r'costofmeal', views.CostOfMealView)
