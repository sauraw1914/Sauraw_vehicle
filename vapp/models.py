from django.db import models

# Create your models here.
class VehicleModel(models.Model):
    name = models.CharField(max_length=15)
    camera1 = models.CharField(max_length=5)
    camera2 = models.CharField(max_length=5)
    staticmap = models.CharField(max_length=10)
    speed = models.CharField(max_length=10)
    avgspeed = models.CharField(max_length=10)
    temperature = models.CharField(max_length=10)
    energystatus = models.CharField(max_length=10)
    fuellevel = models.CharField(max_length=5)
    def __str__(self):
        return self.name