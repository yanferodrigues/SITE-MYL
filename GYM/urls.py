from django.contrib import admin
from django.urls import path
from gym.views import gym


urlpatterns = [
    path("gym/", gym, name="gym"),
]