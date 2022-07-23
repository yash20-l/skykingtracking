from datetime import date, datetime
from statistics import mode
from django.db import models

# Create your models here.

class Tracking(models.Model):
    tcode = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='booked')
    date = models.DateField(default=datetime.now())