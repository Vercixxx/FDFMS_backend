from rest_framework import serializers

from .models import Fleet

class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = '__all__'
        
class UpdateFleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = ['id', 'cars']