from django.shortcuts import render, redirect
from tasks.models import Events
from datetime import date
from django.contrib.auth.models import User
from tasks.models import Events

def tasks(request):
    user = User.objects.get(username = "yanfelipe")
    all_tasks = Events.objects.filter(user = user).order_by("date","time") 
    today = date.today()
    days_map = {
            "MONDAY": 0,
            "TUESDAY": 1,
            "WEDNESDAY": 2,
            "THURSDAY": 3,
            "FRIDAY": 4,
            "SATURDAY": 5,
            "SUNDAY": 6,
    }

    if request.method == "POST":
        button = request.POST.get("action")
        task_title = request.POST.get("task_title")
        task_description = request.POST.get("task_description")
        task_date = request.POST.get("task_date")
        task_time = f"{request.POST.get("start_hour")}:{request.POST.get("start_minute")}:00"
        task_repeat = True if request.POST.get("task_repeat") == "on" else False
        task_weekly = True if request.POST.get("task_weekly") == "on" else False
        task_monthly = True if request.POST.get("task_monthly") == "on" else False
        task_yearly = True if request.POST.get("task_yearly") == "on" else False
        task_weekly_options = request.POST.getlist("days") or "NO WEEKDAYS REPEATS"
        task_importance = request.POST.get("task_priority")
        current_task_title = request.POST.get("current_task_title")

            # user = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE)
            # title = models.CharField(max_length=25, blank=False)
            # description = models.TextField(blank=False)
            # date = models.DateField(blank=False, null=False)
            # time = models.TimeField(blank=True, null=True)
            # repeat = models.BooleanField(default=False)
            # weekly = models.BooleanField(default=False)
            # monthly = models.BooleanField(default=False)
            # yearly = models.BooleanField(default=False)
            # weekly_options = models.JSONField(blank=True,null=True, default=list)
            # importance = models.CharField(blank=False, null=False)
            # done = models.BooleanField(default=False)
        if button == "save":
            Events.objects.create(
                user = user,
                title = task_title,
                description = task_description,
                date = task_date,
                time = task_time,
                repeat = task_repeat,
                weekly = task_weekly,
                monthly = task_monthly,
                yearly = task_yearly,
                weekly_options = task_weekly_options,
                importance = task_importance,
                done = False
            )
        elif button == "done":
            current_task = Events.objects.filter(title = current_task_title, user = user).update(done=True)
        
        return redirect("tasks")
        


    passed_tasks = []
    for event in all_tasks:
        if event.date < today:
            passed_tasks.append(event)
        elif event.done == True:
            passed_tasks.append(event)
 

    general_tasks = [] 
    for event in all_tasks:
        if event not in passed_tasks:
            general_tasks.append(event)
        else:
            pass


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

    if today_tasks:
        pendent_task = today_tasks[0]
    else:
        pendent_task = []

    weekly_tasks = all_tasks.filter(weekly = True)


    monthly_tasks = all_tasks.filter(monthly = True)


    yearly_tasks = all_tasks.filter(yearly = True)
        
        
    return render(request, "tasks.html", {
        "general_tasks":general_tasks,
        "today_tasks":today_tasks,
        "pendent_task":pendent_task,
        "weekly_tasks":weekly_tasks,
        "monthly_tasks":monthly_tasks,
        "yearly_tasks":yearly_tasks,
        "passed_tasks":passed_tasks,
    })