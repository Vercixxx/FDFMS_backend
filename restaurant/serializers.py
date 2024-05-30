from rest_framework import serializers
from django.utils.dateparse import parse_datetime
from datetime import datetime

from .models import Restaurant, Brands, DriverShift
from rest_manager.models import RestManager

from driver.serializers import BasicDriverDataSerializer


class GetAllRestaurants(serializers.ModelSerializer):

    managers = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = '__all__'

    def get_managers(self, obj):
        return [manager.username for manager in obj.managers.all()]

    def get_brand(self, obj):
        return obj.brand.name




# Brand serializers
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'
        
     
# Restaurant serializers   
class RestaurantInfoSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'city', 'brand_name', 'phone', 'country', 'state', 'street', 'home', 'apartament', 'zip', 'managers', 'drivers']
        
    def get_brand_name(self, obj):
        return obj.brand.name
    
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        
class RestaurantNameIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']
        
class GetRestaurantPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'phone']
        
class GetRestAndDriversSerializer(serializers.ModelSerializer):
    drivers = BasicDriverDataSerializer(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'drivers']
        
class RestaurantAndDriversSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()
    drivers = BasicDriverDataSerializer(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'brand_name', 'drivers']
        
    def get_brand_name(self, obj):
        return obj.brand.name   
    
    
class GetDriverShiftsSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.SerializerMethodField()
    class Meta:
        model = DriverShift
        fields = ['id', 'driver', 'time_start', 'time_end', 'restaurant', 'restaurant_name']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        start_time = parse_datetime(representation['time_start'])
        end_time = parse_datetime(representation['time_end'])
        
        representation['time'] = {
            'start': start_time.strftime('%Y-%m-%d %H:%M'),
            'end': end_time.strftime('%Y-%m-%d %H:%M'),
        }

        representation['with'] = representation.pop('driver')

        del representation['time_start']
        del representation['time_end']
        
        if instance.driver is not None:
            representation['color'] = instance.driver.user_color
        else:
            representation['color'] = 'red'

        return representation
    
    def get_restaurant_name(self, obj):
        return obj.restaurant.name
    
class SaveDriverShiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverShift
        fields = ['id', 'driver', 'time_start', 'time_end']
        
class CreateDriverShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverShift
        fields = ['driver', 'time_start', 'time_end', 'restaurant']
        
    
