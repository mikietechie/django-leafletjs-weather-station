'''
Copyrights 2021
Work Done By Mike Zinyoni https://github.com/mikietechie
mzinyoni7@gmail.com (Do not spam please)
(Open to work)
'''

from django.urls import path, re_path
from app import views


urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^", views.error_404, name="404")
]