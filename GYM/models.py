from django.db import models
from django.contrib.auth.models import User

class DayPlan(models.Model):
    WEEK_DAYS = [
    ("SUNDAY", "Sunday"),
    ("MONDAY", "Monday"),
    ("TUESDAY", "Tuesday"),
    ("WEDNESDAY", "Wednesday"),
    ("THURSDAY", "Thursday"),
    ("FRIDAY", "Friday"),
    ("SATURDAY", "Saturday")
    ]
    user = models.ForeignKey(User, related_name="gym_days" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, choices=WEEK_DAYS)
    
    def __str__(self):
        return self.name
    
class MuscleGroup(models.Model):
    MUSCLE_GROUP_CHOICES = [
    ("CHEST", "Chest"),
    ("BACK", "Back"),
    ("TRICEPS", "Triceps"),
    ("BICEPS", "Biceps"),
    ("SHOULDERS", "Shoulders"),
    ("FOREARM", "Forearm"),
    ("TRAPS", "Traps"),
    ("QUADS", "Quads"),
    ("HAMSTRINGS", "Hamstrings"),
    ("GLUTES", "Glutes"),
    ("CALVES", "Calves"),
    ("ADDUCTORS", "Adductors"),
    ("ABDUCTORS", "Abductors"),
    ("ABS", "Abs"),
    ]

    name = models.CharField(max_length=20, choices=MUSCLE_GROUP_CHOICES, default="GENERAL")
    day = models.ForeignKey(DayPlan, related_name="muscle_groups", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.dia}'
    
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField(default='1')
    reps = models.IntegerField(default='1')
    muscle_group = models.ForeignKey(MuscleGroup, related_name="exercises", on_delete=models.CASCADE)