from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import django_user_form,user_profile_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return render(request,'user/index.html')
    else:
       return  HttpResponseRedirect(reverse('user:login'))

def user_signup_view(request):
    user_basic_data = django_user_form()
    user_additional_data = user_profile_form()
    if request.method == 'POST':
        user_basic_data = django_user_form(data=request.POST)
        user_additional_data = user_profile_form(request.POST,request.FILES)
        
        if user_basic_data.is_valid() and user_additional_data.is_valid():
            user = user_basic_data.save()
            user.set_password(user.password)
            user.save()

            additional_data = user_additional_data.save(commit=False)
            additional_data.user = user
            # code for profile pic in case added to model
            # if 'profile_pic' in request.FILES:
            print('request file',request.FILES['profile_pic'])  
            additional_data.profile_pic = request.FILES['profile_pic']
            additional_data.save()
            
            return HttpResponseRedirect(reverse('user:login'))
        print(user_basic_data.errors,user_additional_data.errors)
    return render(request, 'user/signup.html', {
        "user_basic_form": user_basic_data,
        "user_additional_form": user_additional_data
    })

def user_login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
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