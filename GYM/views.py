from django.shortcuts import render
from gym.models import Workout,MuscleGroup,Exercise
from django.contrib.auth.models import User

def gym(request):
    user = User.objects.get(username="yanfelipe")
    workouts = Workout.objects.all().filter(user=user).prefetch_related("muscle_groups__exercises")

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

    if request.method == "POST":
        workout_day_post = request.POST.get("workout_day")
        muscle_group_post = request.POST.get("muscle_group")
        exercises_post = request.POST.getlist("exercise[]")
        sets_post = request.POST.getlist("sets[]")
        reps_post = request.POST.getlist("reps[]")

        workout = Workout.objects.get(user = user, day = workout_day_post)
        muscle_group = MuscleGroup.objects.filter(name = muscle_group_post , workout = workout)
        
        muscle_group.delete()
        
        new_muscle_group = MuscleGroup.objects.create(
            name = muscle_group_post,
            workout = workout
        )
        
        for sets, reps, exercise in zip(sets_post,reps_post, exercises_post):
            
            Exercise.objects.create(
                muscle_group = new_muscle_group,        
                name = exercise,
                sets = sets,
                reps = reps
            )
        
        
        workouts = Workout.objects.all().filter(user=user).prefetch_related("muscle_groups__exercises")

        workout_by_day = {w.day: w for w in workouts}
        
        days_of_workout = []
        
        for day in week_days:
            days_of_workout.append({
                "name":day,
                "workout":workout_by_day.get(day)
            })
            
    
    return render(request,"gym.html", {
        "days":days_of_workout
        })
    
