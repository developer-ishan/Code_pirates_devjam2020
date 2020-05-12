from django.shortcuts import render
from qr.models import gate_entry
from user.models import user_profile
# from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import gate_entry_Serializer
import datetime
from user.models import user_profile



# 1. this is class method to implement list 

class list_gate_entry_api(generics.ListCreateAPIView):
    http_method_names = ['get']
    queryset = gate_entry.objects.all()
    serializer_class = gate_entry_Serializer

 
# 2. this api open/close the gate entry with a input of regno
@api_view(['POST'])
def create_gate_entry_api(request,regno):
    user_details = get_object_or_404(user_profile,regno = regno)
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
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
