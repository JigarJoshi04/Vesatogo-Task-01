from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Shop(models.Model):
    # name = models.CharField(max_length=100)
    # location = models.PointField(srid=4326)
    # polygonn = models.PolygonField()
    # address = models.CharField(max_length=100)
    # city = models.CharField(max_length=50)
    name =  models.CharField(max_length=100)
    polygonn = models.PolygonField()