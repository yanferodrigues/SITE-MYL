from django.contrib import admin
from django.urls import path
from dashboard.views import index

urlpatterns = [
    path('', index, name='index')
]
