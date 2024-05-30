from django.http import JsonResponse

# Serializers
from restaurant.serializers import RestaurantNameIdSerializer, GetRestAndDriversSerializer

# Models
from restaurant.models import Restaurant
from driver.models import Driver 
from .models import RestManager

# Rest
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

class GetRestaurants(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.query_params.get('username')
        user = RestManager.objects.get(username=username)
        
        restaurants = Restaurant.objects.filter(managers=user)
        serialized = RestaurantNameIdSerializer(restaurants, many=True)
        return JsonResponse(serialized.data, safe=False)
    
class GetRestaurantsAndDrivers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.query_params.get('username')
        user = RestManager.objects.get(username=username)
        
        restaurants = Restaurant.objects.filter(managers=user)
        serialized = GetRestAndDriversSerializer(restaurants, many=True)
        return JsonResponse(serialized.data, safe=False)