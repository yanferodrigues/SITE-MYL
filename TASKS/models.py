from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    user = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE)
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField(blank=False)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=True, null=True)
    repeat = models.BooleanField(default=False)
    weekly = models.BooleanField(default=False)
    monthly = models.BooleanField(default=False)
    yearly = models.BooleanField(default=False)
    weekly_options = models.JSONField(blank=True,null=True, default=list)
    importance = models.CharField(blank=False, null=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
