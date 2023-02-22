from django.db import models

# Create your models here.

# New model class
class Sched(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    notes = models.CharField(max_length=500)
    
