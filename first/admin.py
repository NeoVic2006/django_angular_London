from django.contrib import admin
from django.db.models import fields

from .models import Brand, Device, DeviceNumber, Specification

# Register your models here.


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(DeviceNumber)
admin.site.register(Specification)
admin.site.register(Brand)