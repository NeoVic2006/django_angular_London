from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.decorators import authentication_classes
from .models import Device
from rest_framework import serializers, viewsets
from .serializers import DeviceSeializer
from rest_framework.authentication import TokenAuthentication
# Create your views here.



class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSeializer
    queryset = Device.objects.all()
    authentication_classes = (TokenAuthentication, )
