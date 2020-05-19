from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView
from .models import timing

# Create your views here.

import datetime 
from datetime import date

#function to return day name
def day_today(): 
    current_time = datetime.datetime.now()  
    day_name = datetime.date(current_time.year, current_time.month, current_time.day) 
    return day_name.strftime("%A").upper()

class doc_list_view(ListView):
    model = timing
    context_object_name = 'docs'



# print(findDay().upper())
# # print(today)