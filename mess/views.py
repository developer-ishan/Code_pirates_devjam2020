from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Meal
from user.models import user_profile
from datetime import datetime
from datetime import time

def is_time_between(x,y):
    check_time = datetime.now().time()
    return check_time >= x and check_time <= y

def meal_to_vote():
    if is_time_between(time(9,0),time(12,0)):
        return "Lunch"
    elif is_time_between(time(12,0),time(19,0)):
        return "Dinner"
    else:
        return "Breakfast"
        
print(meal_to_vote())

def inc_student_view(request):
    if(request.user.is_authenticated):
        obj = Meal.objects.get(meal_type=meal_to_vote())
        obj.stu_number+=1
        obj.save()

        obj = user_profile.objects.get(user = request.user)
        obj.meal_is_voted = True
        obj.save()

        obj = user_profile.objects.get(user = request.user)
        obj.will_eat = True
        obj.save()
        return redirect('../../')
    else:
       return  HttpResponseRedirect(reverse('user:login'))

def dec_student_view(request):
    if(request.user.is_authenticated):
        obj = Meal.objects.get(meal_type=meal_to_vote())
        obj.stu_number-=1
        obj.save()

        obj = user_profile.objects.get(user = request.user)
        obj.meal_is_voted = True
        obj.save()

        obj = user_profile.objects.get(user = request.user)
        obj.will_eat = False
        obj.save()
        return redirect('../../')
    else:
        return  HttpResponseRedirect(reverse('user:login'))

def reset_day(request):

    meals = Meal.objects.all()
    for meal in meals:
        meal.stu_number = 0
        meal.save()

    users = user_profile.objects.all()
    for user in users:
        user.meal_is_voted = False
        user.wll_eat = True
        user.save()
    
