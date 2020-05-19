from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *
from user.models import user_profile
from datetime import datetime
from datetime import time

# def is_time_between(x,y):
#     check_time = datetime.now().time()
#     return check_time >= x and check_time <= y

# def meal_to_vote():
#     if is_time_between(time(9,0),time(12,0)):
#         return "Lunch"
#     elif is_time_between(time(12,0),time(19,0)):
#         return "Dinner"
#     else:
#         return "Breakfast"
        
# print(meal_to_vote())

def is_voted(request,meal):
    if meal == 'breakfast':
        obj = user_profile.objects.get(user = request.user)
        obj.is_voted_bre = True
    if meal == 'lunch':
        obj = user_profile.objects.get(user = request.user)
        obj.is_voted_lun = True
    if meal == 'dinner':
        obj = user_profile.objects.get(user = request.user)
        obj.is_voted_din = True
    obj.save()

def will_eat(request,meal):
    if meal == 'breakfast':
        obj = user_profile.objects.get(user = request.user)
        obj.will_eat_bre = not obj.will_eat_bre
    if meal == 'lunch':
        obj = user_profile.objects.get(user = request.user)
        obj.will_eat_lun = not obj.will_eat_lun
    if meal == 'dinner':
        obj = user_profile.objects.get(user = request.user)
        obj.will_eat_din = not obj.will_eat_lun
    obj.save()

def inc_student_view(request,meal_type):
    if(request.user.is_authenticated):
        obj = Meal.objects.get(meal_type=meal_type)
        obj.stu_number+=1
        obj.save()
        is_voted(request,meal_type)
        will_eat(request,meal_type)
        return redirect('../../')
    else:
       return  HttpResponseRedirect(reverse('user:login'))

def dec_student_view(request,meal_type):
    if(request.user.is_authenticated):
        obj = Meal.objects.get(meal_type=meal_type)
        obj.stu_number-=1
        obj.save()
        is_voted(request,meal_type)
        will_eat(request,meal_type)

        # obj = user_profile.objects.get(user = request.user)
        # obj.will_eat = False
        # obj.save()
        return redirect('../../')
    else:
        return  HttpResponseRedirect(reverse('user:login'))

# def reset_day(request):
#     if request.user.is_superuser:
#         meals = Meal.objects.all()
#         for meal in meals:
#             meal.stu_number = 0
#             meal.save()

#         users = user_profile.objects.all()
#         for user in users:
#             user.meal_is_voted = False
#             user.wll_eat = True
#             user.save()
    
#     return HttpResponseRedirect(reverse('user:home'))

def meals_today(request):
     try:
        today = datetime.now().strftime("%A").lower()
        meals_today = Schedule.objects.get(day=today)

        meals_today = {
            'breakfast' : meals_today.breakfast,
            'lunch'     : meals_today.lunch,
            'dinner'    : meals_today.dinner,
        }

        return meals_today

     except (Schedule.DoesNotExist):
         meals_today = {
            'breakfast' : '',
            'lunch'     : '',
            'dinner'    : '',
        }
         return meals_today

def get_mess_status(request):
    user = get_object_or_404(user_profile,user = request.user)
    mess_status = {
        "is_voted_bre":user.is_voted_bre,
        "is_voted_lun":user.is_voted_lun,
        "is_voted_din":user.is_voted_din,
        "will_eat_bre":user.will_eat_bre,
        "will_eat_lun":user.will_eat_lun,
        "will_eat_din":user.will_eat_din,
    }
    return mess_status
