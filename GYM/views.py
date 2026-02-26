from django.shortcuts import render, redirect
from gym.models import Workout, MuscleGroup, Exercise
from django.contrib.auth.models import User

def gym(request):

    user = User.objects.get(username="yanfelipe")

    week_days = [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY"
    ]

    if request.method == "POST":
        button = request.POST.get("action")
        workout_day_post = request.POST.get("workout_day")
        muscle_group_post = request.POST.get("muscle_group")
        exercises_post = request.POST.getlist("exercise[]")
        sets_post = request.POST.getlist("sets[]")
        reps_post = request.POST.getlist("reps[]")

        workout, created = Workout.objects.get_or_create(
            user=user,
            day=workout_day_post
        )

        if button == "delete":
            muscle_group = MuscleGroup.objects.filter(
                workout = workout
            )

            muscle_group.get(
                name=muscle_group_post,
                workout=workout
            ).delete()
        else:
            old_group = MuscleGroup.objects.filter(
                name=muscle_group_post,
                workout=workout
            ).first()

            if old_group:
                old_group.delete()

            new_muscle_group = MuscleGroup.objects.create(
                name=muscle_group_post,
                workout=workout
            )

            for sets, reps, exercise in zip(sets_post, reps_post, exercises_post):
                Exercise.objects.create(
                    muscle_group=new_muscle_group,
                    name=exercise,
                    sets=sets,
                    reps=reps
                )

            return redirect("gym")

    workouts = Workout.objects.filter(user=user).prefetch_related(
        "muscle_groups__exercises"
    )

    workout_by_day = {w.day: w for w in workouts}

    days_of_workout = [
        {
            "name": day,
            "workout": workout_by_day.get(day)
        }
        for day in week_days
    ]

    return render(request, "gym.html", {
        "days": days_of_workout
    })
    
