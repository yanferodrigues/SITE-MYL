from django.db import models
from django.contrib.auth.models import User

class Day(models.Model):
    user = models.ForeignKey(User, related_name="gym_days" ,on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    
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

    nome = models.CharField(max_length=20, choices=MUSCLE_GROUP_CHOICES, default="GENERAL")
    dia = models.ForeignKey(Day, related_name="muscle_groups", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.dia}'
    
class Exercise(models.Model):
    sets = models.IntegerField(default='1')
    reps = models.IntegerField(default='1')
    nome = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(MuscleGroup, related_name="exercises", on_delete=models.CASCADE)