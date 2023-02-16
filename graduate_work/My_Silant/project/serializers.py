from rest_framework import serializers
from .models import Machine,Maintenance_operation,Reclamation

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('__all__')

class Maintenance_operationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance_operation
        fields = ('__all__')
        
class ReclamationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamation
        fields = ('__all__')