from django.shortcuts import render
from app.models import Location
import statistics

# Create your views here.
def index(request):
    locations = Location.objects.all()
    center_x = statistics.fmean([location.latitude for location in locations])
    center_y = statistics.fmean([location.longitude for location in locations])
    loc = locations[0]
    print(loc.weather_now)
    return render(request, "app/index.html", {
        "locations": locations,
        "center_x": center_x,
        "center_y": center_y
    })