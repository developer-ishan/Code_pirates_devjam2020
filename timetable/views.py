from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from user.models import user_profile
from .models import Subject, Day, Time_Table
from datetime import datetime
from user.models import user_profile

# Create your views here.

def timetable_view(request):
    try:
        today = today = datetime.now().strftime("%A").lower()
        group  = user_profile.objects.get(user = request.user).group
        timetable = Time_Table.objects.get(group = group).days.get(day_name=today).subjects.all().order_by('start_time')
        context = {
            'group'     :group,
            'timetable' :timetable,
        }
        return context 
    except (Time_Table.DoesNotExist, Day.DoesNotExist):
        return {'group':[],'timetable':[]}
    
