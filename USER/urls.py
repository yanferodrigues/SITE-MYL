from django.contrib import admin
from django.urls import path
from user.views import user


urlpatterns = [
    path("user/", user, name="user"),
]