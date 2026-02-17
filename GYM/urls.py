from django.contrib import admin
from django.urls import path
from GYM.views import gym


urlpatterns = [
    path("gym/", gym, name="gym"),
]