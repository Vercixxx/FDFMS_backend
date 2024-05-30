from rest_framework import serializers

from .models import Car, CarDailyReports, CarDamage

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = '__all__'
        
        
class CarVinLicensePlateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ('vin', 'license_plate')
        
class CarDailyReportsSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d-%m-%Y')
    
    class Meta:
        model = CarDailyReports
        fields = ['id', 'date', 'driver', 'car', 'car_mileage', 'car_condition', 'car_cleanliness', 'additional_remarks']
        

class CarDamageSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d-%m-%Y')
    class Meta:
        model = CarDamage
        fields = ('date', 'driver', 'car', 'car_mileage', 'description')
        

