from django.urls import path, re_path
from app import views


urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^", views.error_404, name="404")
]