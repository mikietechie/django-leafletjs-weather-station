'''
Copyrights 2021
Work Done By Mike Zinyoni https://github.com/mikietechie
mzinyoni7@gmail.com (Do not spam please)
(Open to work)
'''

from django.contrib import admin
from app import models

# Register your models here.
@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "latitude", "longitude", "grid_x", "grid_y", "grid_id")
    list_editable = ("title", "latitude", "longitude")
    list_filter = ("grid_id",)
    ordering = ("title", "latitude", "longitude", "grid_x", "grid_y", "grid_id")
    
    
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")