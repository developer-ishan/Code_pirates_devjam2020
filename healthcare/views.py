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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        monday = timing.objects.filter(day = 'MONDAY')
        tuesday = timing.objects.filter(day = 'TUESDAY')
        wednesday = timing.objects.filter(day = 'WEDNESDAY')
        thrusday = timing.objects.filter(day = 'THRUSDAY')
        friday = timing.objects.filter(day = 'FRIDAY')
        saturday = timing.objects.filter(day = 'SATURDAY')
        sunday = timing.objects.filter(day = 'SUNDAY')

        context = {
            'monday':monday,
            'tuesday':tuesday,
            'wednesday':wednesday,
            'thrusday':thrusday,
            'friday':friday,
            'saturday':saturday,
            'sunday':sunday
        }
        # context['days_context']
    
        return context



# print(findDay().upper())
# # print(today)