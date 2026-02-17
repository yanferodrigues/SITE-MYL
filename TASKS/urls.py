from django.contrib import admin
from django.urls import path
from TASKS.views import tasks

urlpatterns = [
    path("tasks/", tasks, name="tasks"),
]