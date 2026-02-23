from django.shortcuts import render
from gym.models import Workouts,MuscleGroup,Exercise
from django.contrib.auth.models import User

def gym(request):
    user = User.objects.get(username="yanfelipe")
    workouts = Workouts.objects.all().filter(user=user).prefetch_related("muscle_groups__exercises")

    days = [
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    ]

    
    
    sunday = workouts.filter(day="SUNDAY").first()
    monday = workouts.filter(day="MONDAY").first()
    tuesday = workouts.filter(day="TUESDAY").first()
    wednesday = workouts.filter(day="WEDNESDAY").first()
    thursday = workouts.filter(day="THURSDAY").first()
    friday = workouts.filter(day="FRIDAY").first()
    saturday = workouts.filter(day="SATURDAY").first()

    
    return render(request,"gym.html", {
        "sunday": sunday,
        "monday": monday,
        "tuesday": tuesday,
        "wednesday": wednesday,
        "thursday": thursday,
        "friday": friday,
        "saturday": saturday,
        })
    
