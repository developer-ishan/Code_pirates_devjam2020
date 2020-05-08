from django.urls import path,include
from .views import home_view,user_login_view,user_signup_view

urlpatterns = [
    path('',home_view,name='home'),
    path('login/',user_login_view,name='login'),
    path('signup/',user_signup_view,name='signup')
]