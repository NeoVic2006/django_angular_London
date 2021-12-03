from django.db import models

# Create your models here.

class DeviceNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=10, blank=True)


class Device(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    date = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='pictures/', blank=True)
    is_out = models.BooleanField(default=False)

    # One to one relationship
    number = models.OneToOneField(DeviceNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Specification(models.Model):
    name = models.CharField(max_length=30)
     # One to many relationship
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='specification')


class Brand(models.Model):
    name = models.CharField(max_length=30)
    # Many to many relationship
    devices = models.ManyToManyField(Device, related_name='brand')




