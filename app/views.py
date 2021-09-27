from django.shortcuts import render
from app.models import Location
import statistics

# Create your views here.
def index(request):
    locations = Location.objects.all()
    try:
        center_x = statistics.fmean([location.latitude for location in locations])
        center_y = statistics.fmean([location.longitude for location in locations])
    except statistics.StatisticsError:
        center_x, center_y = 39.300299, -94.833984
    return render(request, "app/index.html", {
        "locations": locations,
        "center_x": center_x,
        "center_y": center_y
    })