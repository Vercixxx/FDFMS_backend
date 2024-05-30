from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Country, State
from .serializers import *


# ========== Countries ==========
class GetCountries(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.headers)
        countries = Country.objects.all().order_by('name')
        serialized = CountrySerializer(countries, many=True)
        return JsonResponse(serialized.data, safe=False, status=200)


class AddCountry(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = self.request.data['name'].strip()

        if name:
            if Country.objects.filter(name=name).exists():
                return JsonResponse({'error': 'Country already exists'}, safe=False, status=400)
            country = Country.objects.create(name=name)
            return JsonResponse({'message': 'Ok'}, status=201)

        return JsonResponse({'error': 'Country name is required'}, safe=False, status=400)

class DeleteCountry(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, name):
        name = name.strip()

        if name:
            country = Country.objects.get(name=name)
            country.delete()
            return JsonResponse({'message': 'Ok'}, status=201)
        
        return JsonResponse({'error': 'Country name is required'}, safe=False, status=400)
    
# ========== Countries ==========

        
        
        
        
        
# ========== States ==========
class GetStates(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        country = self.request.query_params.get('country', '').strip()

        output = []
        if country:
            states = State.objects.filter(country__name=country)
            serialized = StateSerializer(states, many=True)
            output = serialized.data

        else:
            states = State.objects.all().order_by('name')
            serialized = StateSerializer(states, many=True)
            output = serialized.data

        return JsonResponse(output, safe=False, status=200)
    
class AddState(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        country = self.request.data.get('country', '').strip()
        name = self.request.data.get('name', '').strip()


        if country and name:
            if State.objects.filter(country__name=country, name=name).exists():
                return JsonResponse({'error': 'State already exists for that country'}, safe=False, status=400)
            
            serializer = StateSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Ok'}, status=201)
            else:
                return JsonResponse({'errors': serializer.errors}, status=400)


        return JsonResponse({'error': 'Country and state name are required'}, safe=False, status=400)

    
class EditState(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        
        try :
            state = State.objects.get(id = id)
            serialized = StateSerializer(state, data=request.data)
            
            if serialized.is_valid():
                serialized.save()
                return JsonResponse({'message': 'Ok'}, status=201)
            else:
                return JsonResponse({'errors': serialized.errors}, status=400)
            
        except State.DoesNotExist:
            return JsonResponse({'error': 'State not found'}, safe=False, status=404)
     

class DeleteState(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = State.objects.all()
    serializer_class = StateSerializer
# ========== States ==========


