from django.shortcuts import render
from gym.models import Workout,MuscleGroup,Exercise
from django.contrib.auth.models import User

def gym(request):
    user = User.objects.get(username="yanfelipe")
    workouts = Workout.objects.all().filter(user=user).prefetch_related("muscle_groups__exercises")
    
    # if request.method == 'POST':
    #     workouts.filter(day = request.POST.get("day")).delete()
        
    #     muscle_groups = request.POST.getlist("muscle_group[]")
    #     exercises = request.POST.getlist("exercise[]")
    #     sets = request.POST.getlist("sets[]")
    #     reps = request.POST.getlist("reps[]")
        
    
    # else:

    week_days = [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY"
    ]

    workout_by_day = {w.day: w for w in workouts}

    days_of_workout = []

    for day in week_days:
        days_of_workout.append({
            "name":day,
            "workout":workout_by_day.get(day)
        })
    # return days_of_workout

    
    return render(request,"gym.html", {
        "days":days_of_workout
        })
    
