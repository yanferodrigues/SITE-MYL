from django.shortcuts import render
from tasks.models import Events

def tasks(request):
    
    return render(request, "tasks.html")