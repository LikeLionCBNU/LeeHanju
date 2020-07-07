from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from django.utils import timezone
from .forms import ScheduleForm

# Create your views here.

def home(request):
    schedules = Schedule.objects.order_by('schedule_date')
    return render(request, 'home/home.html', {'schedules':schedules})

def detail(request, schedule_id):
    schedule_detail = get_object_or_404(Schedule, pk=schedule_id)
    return render(request, 'home/detail.html', {'schedule':schedule_detail})

def schedule_new(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.published_date = timezone.datetime.now()
            schedule.save()
            return redirect('detail', schedule_id=schedule.pk)
    else:
        form = ScheduleForm()
    return render(request, 'home/schedule_new.html', {'form': form})

def schedule_edit(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk = schedule_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance = schedule)
        if form.is_valid():
            schedule = form.save(commit = False)
            schedule.published_date = timezone.datetime.now()
            schedule.save()
            return redirect('detail', schedule_id = schedule.pk)
    else:
        form = ScheduleForm(instance = schedule)
    return render(request, 'home/schedule_edit.html', {'form': form})

def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    schedule.delete()
    return redirect('home')