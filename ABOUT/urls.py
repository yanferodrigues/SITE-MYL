from django.contrib import admin
from django.urls import path
from ABOUT.views import about


urlpatterns = [
    path("about", about, name="about"),
]