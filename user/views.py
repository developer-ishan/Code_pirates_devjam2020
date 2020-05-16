from django.shortcuts import render,reverse,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import django_user_form,user_profile_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from qr.models import gate_entry
from .models import user_profile
from api.models import entry_status
from communities.models import community

from mess.models import *
from mess.views import *
from datetime import datetime

def current_meal():
    today = datetime.now().strftime("%A")
    meals_today = Schedule.objects.get(day=today)
    to_vote = meal_to_vote()
    
    if to_vote == 'Breakfast':
        return meals_today.breakfast
    elif to_vote == 'Lunch':
        return meals_today.lunch
    else:
        return meals_today.dinner

@login_required
def home_view(request):
    if request.user.is_authenticated:
        user = get_object_or_404(user_profile,user = request.user)
        regno = user.regno
        entry = gate_entry.objects.filter(regno = regno,intime = None)
        isInsideHostel=True
        if entry:
            isInsideHostel = False
        context = {
            'isInsideHostel'  : isInsideHostel,
            'meal'            : meal_to_vote(),
            'is_meal_voted'   : user.meal_is_voted,
            'will_eat'        : user.will_eat,
            'current_meal'    : current_meal()
        }
        return render(request,'user/index.html',context)
    else:
       return  HttpResponseRedirect(reverse('user:login'))

def user_signup_view(request):
    user_basic_data = django_user_form()
    user_additional_data = user_profile_form()
    if request.method == 'POST':
        user_basic_data = django_user_form(data=request.POST)
        user_additional_data = user_profile_form(request.POST,request.FILES)
        
        if user_basic_data.is_valid() and user_additional_data.is_valid() and request.FILES['profile_pic']:
            user = user_basic_data.save()
            user.set_password(user.password)
            user.save()
            entry_status.objects.create(user=user)
            additional_data = user_additional_data.save(commit=False)
            additional_data.user = user
            # code for profile pic in case added to model
            # print('request file',request.FILES['profile_pic'])  
            additional_data.profile_pic = request.FILES['profile_pic']
            additional_data.save()
            #by default adding notice community to every user
            notice_community = community.objects.get(slug = 'notice')
            notice_community.followed_by.add(user)
            additional_data.following.add(notice_community)
            return HttpResponseRedirect(reverse('user:login'))
        print(user_basic_data.errors,user_additional_data.errors)
    return render(request, 'user/signup.html', {
        "user_basic_form": user_basic_data,
        "user_additional_form": user_additional_data
    })

def user_login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user:home'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin/')
            return HttpResponseRedirect(reverse('user:home'))
        else:
            if User.objects.filter(username=username):
                messages.error(request, 'invalid password')
            else:
                messages.error(
                    request, 'no user with username {} exist,username is case sensitive'.format(username))
            return HttpResponseRedirect(reverse('user:login'))
    
    return render(request,'user/login.html',{})

@login_required
def user_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))