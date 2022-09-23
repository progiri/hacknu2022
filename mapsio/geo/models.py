from statistics import mode
from xml.dom.minidom import Identified
from django.contrib.gis.db import models


class GeoDataPacket(models.Model):
    point = models.PointField(srid=3857)
    identifier = models.CharField(max_length=255)
    timestamp = models.PositiveBigIntegerField()
    floor_label = models.IntegerField()
    hor_accuracy = models.FloatField()
    ver_accuracy = models.FloatField()
    cil_accuracy = models.FloatField()
    activity = models.CharField(max_length=255)

