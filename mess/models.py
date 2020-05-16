from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    stu_number  = models.IntegerField(default=0)
    meal_type   = models.CharField(max_length=20)
    start_time  = models.TimeField()
    end_time    = models.TimeField()
    
    def __str__(self):
        return self.meal_type


class Schedule(models.Model):
    day = models.CharField(max_length=20)
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()

    def __str__(self):
        return self.day
    
    @classmethod
    def now(cls):
        pass