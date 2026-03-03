from django.shortcuts import render
from tasks.models import Events
from datetime import date

def tasks(request):
    monday = "0"
    tuesday = "1"
    wednesday = "2"
    thursday = "3"
    friday = "4"
    saturday = "5"
    sunday = "6"
    
    today = date.today()
    
    general_tasks = Events.objects.all()
    today_tasks = []
    for event in Events.objects.all():
        if event.date == today:
            today_tasks.append(event)
        elif event.weekly and today.weekday() in event.weekly_options:
            today_tasks.append(event)
        elif event.monthly and event.date.day == today.day:
            today_tasks.append(event)
        elif event.yearly and (event.date.day == today.day and event.date.month == today.month):
            today_tasks.append(event)
            
    weekly_tasks = Events.objects.filter(weekly = True)
    monthly_tasks = Events.objects.filter(monthly = True)
    yearly_tasks = Events.objects.filter(yearly = True)
    
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