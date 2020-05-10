from django.urls import path,include
from .views import home_view,user_login_view,user_signup_view,user_logout_view
app_name = 'user'
urlpatterns = [
    path('home/',home_view,name='home'),
    path('login/',user_login_view,name='login'),
    path('logout/',user_logout_view,name='logout'),
    path('signup/',user_signup_view,name='signup')
]