from django.urls import path
from .views import *
app_name='mess'
urlpatterns = [
    path('yes/',inc_student_view),
    path('no/',dec_student_view),
    path('newday/the_secret_token',reset_day)   # The secret token is used to pevent anonymous user
]                                           # from resetting the fields  
