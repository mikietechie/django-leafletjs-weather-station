from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import requests, json


# Create your models here.
class User(AbstractUser):
    pass

class Location(models.Model):
    title = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()
    grid_x = models.IntegerField(blank=True, null=True)
    grid_y = models.IntegerField(blank=True, null=True)
    grid_id = models.CharField(max_length=32, blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        # validate
        point = json.loads(requests.get(f"https://api.weather.gov/points/{self.latitude},{self.longitude}").content)
        self.grid_id = point["properties"]["gridId"]
        self.grid_x = point["properties"]["gridX"]
        self.grid_y = point["properties"]["gridY"]
        self.data = point
        super().save(*args, **kwargs)
    
    @property
    def weather(self):
        return json.loads(
            requests.get(f"https://api.weather.gov/gridpoints/{self.grid_id}/{self.grid_x},{self.grid_y}/forecast").content
            )
    
    @property
    def weather_now(self):
        return self.weather['properties']['periods'][0]
    
    def __str__(self): return f"{self.title} ({self.grid_x}, {self.grid_y})"
            