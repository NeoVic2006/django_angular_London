from rest_framework import serializers
from .models import Brand, Device, DeviceNumber, Specification


class DeviceNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['id', 'name']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class DeviceSeializer(serializers.ModelSerializer):
    number = DeviceNumberSerializer(many=False)
    specification = SpecificationSerializer(many=True)
    brand = BrandSerializer(many=True)
    class Meta:
        model = Device
        fields = ['id', 'name', 'description', 'number', 'specification', 'brand']