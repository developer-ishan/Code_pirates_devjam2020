from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login
from .forms import django_user_form,user_profile_form

# Create your views here.
def home_view(request):
    return HttpResponse('this is home page')

def user_signup_view(request):
    user_basic_data = django_user_form()
    user_additional_data = user_profile_form()
    if request.method == 'POST':
        user_basic_data = django_user_form(data=request.POST)
        user_additional_data = user_profile_form(data=request.POST)
        
        if user_basic_data.is_valid() and user_additional_data.is_valid():
            user = user_basic_data.save()
            user.set_password(user.password)
            user.save()

            additional_data = user_additional_data.save(commit=False)
            additional_data.user = user
            # code for profile pic in case added to model
            # if 'profile_pic' in request.FILES:
            #     additional_data.profile_pic = request.FILES['profile_pic']
            additional_data.save()
            
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'user/signup.html', {
        "user_basic_form": user_basic_data,
        "user_additional_form": user_additional_data
    })

def user_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)
        if user:
            login(request,user)
            return HttpResponse('login successful')
        else:
            return HttpResponse('invlaid login')
    
    return render(request,'user/login.html',{})