from qr.models import gate_entry
from rest_framework import serializers

class gate_entry_Serializer(serializers.ModelSerializer):
    class Meta:
        model = gate_entry
        fields = '__all__'