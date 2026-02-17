from django.contrib import admin
from django.urls import path
from USER.views import user


urlpatterns = [
    path("user/", user, name="user"),
]