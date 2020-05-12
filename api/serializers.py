from qr.models import gate_entry
from rest_framework import serializers
from .models import entry_status

class gate_entry_Serializer(serializers.ModelSerializer):
    class Meta:
        model = gate_entry
        fields = '__all__'

class entry_status_serializer(serializers.ModelSerializer):
    class Meta:
        model = entry_status
        fields = ['show_tick']