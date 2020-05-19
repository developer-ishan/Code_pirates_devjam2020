from django.shortcuts import render
from qr.models import gate_entry
from user.models import user_profile
# from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import gate_entry_Serializer,entry_status_serializer
import datetime
from .models import entry_status


# 1.this api return the current status of tick(checked or not)
@api_view(['GET'])
def show_tick_api(request,regno):
    user = get_object_or_404(user_profile,regno = regno)
    tick_data = get_object_or_404(entry_status,user = user.user)
    serializer = entry_status_serializer(tick_data,many = False)
    return Response(serializer.data)

# 2.this api will toggle the status of show tick to true after scanning qr
@api_view(['GET'])
def set_tick_to_true(request,regno):
    user = get_object_or_404(user_profile,regno = regno)
    tick_data = get_object_or_404(entry_status,user = user.user)
    #this line is changing the tick status to true after scannig qr
    tick_data.show_tick = True
    previous_entries = (gate_entry.objects.filter(regno = regno,intime = None))
    #these conditions are setting is_opening a fresh entry
    if previous_entries:
        tick_data.is_opening_entry = False
    else:
        tick_data.is_opening_entry = True
    tick_data.save()
    serializer = entry_status_serializer(tick_data,many = False)
    return Response(serializer.data)

# 3. this is class method to implement list 
    #this api will return all the gate entries
# class list_gate_entry_api(generics.ListCreateAPIView):
#     http_method_names = ['get']
#     queryset = gate_entry.objects.all()
#     serializer_class = gate_entry_Serializer
@api_view(['GET'])
def list_gate_entry_api(request):
    gate_entries = gate_entry.objects.all()
    serializer = gate_entry_Serializer(gate_entries,many = True)
    return Response({"Entry data": serializer.data})


 
# 4. this api open/close the gate entry with a input of regno
@api_view(['POST'])
def create_gate_entry_api(request,regno):
    user_details = get_object_or_404(user_profile,regno = regno)
    print(user_details)
    now=datetime.datetime.now()
    data={
 
    "name": user_details.user.first_name,
    "regno": user_details.regno,
    "roomno": user_details.roomno,
    "intime":None,
    "outtime": now,
    }
    previous_entries = (gate_entry.objects.filter(regno = regno,intime = None))
    if previous_entries:
        previous_entry = previous_entries[0]
        data['intime']  = now
        print(user_details.regno)
        data['outtime']= previous_entry.outtime
        serializer = gate_entry_Serializer(instance = previous_entry,data=data)
    else:
        serializer = gate_entry_Serializer(data=data)
    
    if serializer.is_valid():
        tick_data = get_object_or_404(entry_status,user = user_details.user)
        #this line is changing the tick status to false after opening/closing gate entry
        tick_data.show_tick = False
        tick_data.save()
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
