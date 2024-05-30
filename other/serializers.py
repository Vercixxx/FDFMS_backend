from rest_framework import serializers

from .models import Country, State

# Country
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name']

class CountryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = []
# Country


# State
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class StateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name', 'country']

class StateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = []
        
class StateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name']
# State