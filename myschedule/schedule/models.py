from django.db import models
from django.utils import timezone

# Create your models here.

class Schedule(models.Model):
    title = models.CharField(max_length=200)
    memo = models.TextField()
    schedule_date = models.DateTimeField(default=timezone.now, null=False)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title