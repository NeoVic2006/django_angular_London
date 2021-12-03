from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import DeviceViewSet
from .serializers import DeviceSeializer


router = routers.DefaultRouter()
router.register('devices', DeviceViewSet)


urlpatterns = [
    path('', include(router.urls))
]
