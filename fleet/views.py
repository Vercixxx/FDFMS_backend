from django.http import JsonResponse

# Rest
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import DestroyAPIView

# DB
from django.db.models import Q

# Models
from .models import Fleet
from restaurant.models import Restaurant
from car.models import Car

# Serializers
from .serializers import FleetSerializer, UpdateFleetSerializer


# Add Fleet
class AddFleet(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        data = request.data
        
        data['restaurant'] = Restaurant.objects.get(name = data['restaurant']).id
        
        serializer = FleetSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Fleet added'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
# Add Fleet

# Edit Fleet
class EditFleet(APIView):
    permission_classes = (IsAuthenticated,)
    
    def put(self, request):
        data = request.data
        
        try:
            fleet = Fleet.objects.get(id=data['fleet_id'])
        except Fleet.DoesNotExist:
            return JsonResponse({'message': 'Fleet not found'}, status=404)

        serializer = UpdateFleetSerializer(fleet, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Fleet updated successfully'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
# Edit Fleet


# Get Fleet
class GetFleet(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        rest_id = self.request.query_params.get('restaurant_id', '').strip()

        try:
            restaurant = Restaurant.objects.get(id=rest_id)
            fleet = Fleet.objects.get(restaurant=restaurant)
        except Fleet.DoesNotExist:
            return JsonResponse({'message': 'Fleet does not exist'}, status=404)
        
        serializer = FleetSerializer(fleet)
        
        return JsonResponse(serializer.data, status=200)
# Get Fleet


# Delete Fleet
class DeleteFleet(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    lookup_field = 'id'
# Delete Fleet
