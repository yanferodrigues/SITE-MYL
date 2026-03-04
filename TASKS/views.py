from django.shortcuts import render
from tasks.models import Events
from datetime import date
from django.contrib.auth.models import User

def tasks(request):
    user = User.objects.get(username = "yanfelipe")
    today = date.today()
    general_tasks = Events.objects.filter(user = user)

    days_map = {
            "MONDAY": 0,
            "TUESDAY": 1,
            "WEDNESDAY": 2,
            "THURSDAY": 3,
            "FRIDAY": 4,
            "SATURDAY": 5,
            "SUNDAY": 6,
    }
    today_tasks = []
    for event in general_tasks:
        repeat_list = []
        for option in event.weekly_options:
            repeat_list.append(days_map.get(option))
        if event.date == today:
            today_tasks.append(event)
        elif event.weekly and today.weekday() in repeat_list:
            today_tasks.append(event)
        elif event.monthly and event.date.day == today.day:
            today_tasks.append(event)
        elif event.yearly and (event.date.day == today.day and event.date.month == today.month):
            today_tasks.append(event)
            
    weekly_tasks = general_tasks.filter(weekly = True)
    monthly_tasks = general_tasks.filter(monthly = True)
    yearly_tasks = general_tasks.filter(yearly = True)
    
    passed_tasks = []
    for event in Events.objects.all():
        if event.date < today:
            passed_tasks.append(event)
        elif event.done == True:
            passed_tasks.append(event)

        
    return render(request, "tasks.html", {
        "general_tasks":general_tasks,
        "today_tasks":today_tasks,
        "weekly_tasks":weekly_tasks,
        "monthly_tasks":monthly_tasks,
        "yearly_tasks":yearly_tasks,
        "passed_tasks":passed_tasks,
    })