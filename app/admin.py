from django.contrib import admin
from app import models

# Register your models here.
@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "latitude", "longitude", "grid_x", "grid_y", "grid_id")
    list_editable = ("title", "latitude", "longitude")
    list_filter = ("grid_id",)
    ordering = ("title", "latitude", "longitude", "grid_x", "grid_y", "grid_id")