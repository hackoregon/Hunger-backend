from django.conf.urls import url, include
from rest_framework import routers
from apiv1 import views



router = routers.DefaultRouter()
router.register(r'counties', views.CountyView)
