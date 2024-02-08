# crops/models.py
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    production = models.FloatField()

    def __str__(self):
        return self.name
