from django.contrib import admin
from django.urls import path
from FINANCE.views import finance


urlpatterns = [
    path("finance", finance, name="finance"),
]