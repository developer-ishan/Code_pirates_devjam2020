from django.shortcuts import render,reverse,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import django_user_form,user_profile_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from qr.models import gate_entry
from .models import user_profile,complaint
from api.models import entry_status
from communities.models import community,post
# from mess.models import *
# from mess.views import *
from healthcare.models import timing
from healthcare.views import day_today
from datetime import date,datetime

from timetable.views import *

from mess.views import *
    

@login_required
def home_view(request):
    if request.user.is_authenticated:
        user = get_object_or_404(user_profile,user = request.user)
        regno = user.regno
        entry = gate_entry.objects.filter(regno = regno,intime = None)
        isInsideHostel=True
        if entry:
            isInsideHostel = False

        #user followed communities posts
        community_followed_by_user = community.objects.filter(followed_by = request.user)
        posts = post.objects.all()


        context = {
            'isInsideHostel'  : isInsideHostel,
            'docs'            : timing.objects.filter(day = day_today()),
            'community_followed_by_user':community_followed_by_user,
            'posts':posts,
            'suggested':community.objects.order_by('?')[:4],
            'test':'nope'
            #todo change above "1" to 4 or 5
        }

        # Adding the timetable to context dict
        context.update(timetable_view(request))
        #adding meals to dict
        context.update(meals_today(request))
        #adding mess status to dict
        context.update(get_mess_status(request))
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
            #by default adding official communities to every user
            official_communities = community.objects.filter(isofficial = True)
            additional_data.following.set(official_communities)
            additional_data.save()
            #adding this new user to follower list of official communities
            for object in official_communities:
                object.followed_by.add(user)
                object.save()
            return HttpResponseRedirect(reverse('user:login'))
        print(user_basic_data.errors,user_additional_data.errors)
    #if logged in user tried to access signup page it will log him out
    logout(request)
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
            next_url = request.POST.get('next')
            if next_url and next_url != '/':
                return HttpResponseRedirect(next_url)
            
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

@login_required
def user_complaint_view(request):

    if request.method == "POST":
        sender = get_object_or_404(user_profile,user = request.user)
        text = request.POST['complaint']
        complaint.objects.create(sender = sender,desc = text)
        print('complaint added')
        return HttpResponseRedirect(reverse('user:home'))
    
    return render(request,'user/index.html',{})



