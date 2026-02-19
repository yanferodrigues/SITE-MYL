from django.contrib import admin
from django.urls import path
from tasks.views import tasks

urlpatterns = [
    path("tasks/", tasks, name="tasks"),
]