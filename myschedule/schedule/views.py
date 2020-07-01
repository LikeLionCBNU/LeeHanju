from django.shortcuts import render
from .models import Schedule

# Create your views here.

def home(request):
    schedules = Schedule.objects
    return render(request, 'home/home.html', {'schedules':schedules})