from django.shortcuts import render
from gym.models import DayPlan,MuscleGroup,Exercise
from django.contrib.auth.models import User

def gym(request):
    user = User.objects.get(username="yanfelipe")
    dayplan = DayPlan.objects.all().filter(user=user).prefetch_related("muscle_groups__exercises")
    
    sunday = dayplan.filter(name="SUNDAY").first()
    monday = dayplan.filter(name="MONDAY").first()
    tuesday = dayplan.filter(name="TUESDAY").first()
    wednesday = dayplan.filter(name="WEDNESDAY").first()
    thursday = dayplan.filter(name="THURSDAY").first()
    friday = dayplan.filter(name="FRIDAY").first()
    saturday = dayplan.filter(name="SATURDAY").first()
    
    return render(request,"gym.html", {
        "sunday": sunday,
        "monday": monday,
        "tuesday": tuesday,
        "wednesday": wednesday,
        "thursday": thursday,
        "friday": friday,
        "saturday": saturday,
        })
    
