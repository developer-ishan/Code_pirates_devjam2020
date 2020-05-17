from django.urls import path,include
from .views import home_view,user_login_view,user_signup_view,user_logout_view,user_complaint_view
app_name = 'user'
urlpatterns = [
    path('',home_view,name='home'),
    path('home/',home_view,name='home'),
    path('login/',user_login_view,name='login'),
    path('logout/',user_logout_view,name='logout'),
    path('signup/',user_signup_view,name='signup'),
    path('complaint/',user_complaint_view,name='complaint')
]