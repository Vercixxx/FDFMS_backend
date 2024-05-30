from django.http import JsonResponse

from datetime import datetime, date, timedelta

# Rest
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import DestroyAPIView

# Models
from .models import Driver, DailyWork, WageTariff, Rating
from fleet.models import Fleet
from restaurant.models import Restaurant
from users.models import GeneralUser, Addresses

# Serializers
from .serializers import RestaurantDriversSerliazer, DriverUsernameSerializer, DailyDriverReportSerializer, WageTariffSerializer, WageTariffGetIdSerializer, NewBillingPeriodSerializer, GetRatingSerializer, UserRating
from users.serializers import ResidenceAddressSerializer
from restaurant.serializers import RestaurantNameIdSerializer, GetRestaurantPhoneSerializer


# DB
from django.db.models import Q,F

# Document
import csv
import uuid
from django.core.files import File
from wsgiref.util import FileWrapper
from django.http import FileResponse
import os


class GetRestaurants(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        driver = Driver.objects.get(username=username)
        restaurants = Restaurant.objects.filter(drivers=driver)
        result = {}

        for restaurant in restaurants:
            fleets = Fleet.objects.filter(restaurant=restaurant)
            result[restaurant.name] = [car.license_plate for fleet in fleets for car in fleet.cars.filter(active=True)]

        return JsonResponse(result, safe=False)
    
class UsersPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100

    def get_page_size(self, request):
        page_size = super().get_page_size(request)
        if page_size is None or page_size == 0:
            return self.max_page_size
        return page_size
    
    
class GetDriversUsernames(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        restaurant = self.request.query_params.get('restaurant', '').strip()

        # Choosing correct serializer and user model
        serializer_class = DriverUsernameSerializer
        user_model = Driver

        queryset = user_model.objects.all()
        
        # Get users from selected restaurant
        restaurants = Restaurant.objects.filter(name=restaurant)
        
        drivers = Driver.objects.none()

        for restaurant in restaurants:
            drivers |= restaurant.drivers.all().order_by('date_joined')

        queryset = drivers.filter(is_active=True)

        serialized_data = serializer_class(queryset, many=True).data
        return JsonResponse(serialized_data, status=200, safe=False)

    
class GetDrivers(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = UsersPagination

    @staticmethod
    def get_addresses(username):
        try:
            user = GeneralUser.objects.get(username=username)
            address = Addresses.objects.get(username=user)
            return ResidenceAddressSerializer(instance=address).data
        except GeneralUser.DoesNotExist:
            return {'error': 'User not found'}
        except Addresses.DoesNotExist:
            return {'error': 'Address not found'}

    def get(self, request):
        limit = self.request.query_params.get('limit', '').strip()
        query = self.request.query_params.get('search', '').strip()
        status = self.request.query_params.get('status', '').strip()
        restaurant = self.request.query_params.get('restaurant', '').strip()


        # Choosing correct serializer and user model
        serializer_class = RestaurantDriversSerliazer
        user_model = Driver

        queryset = user_model.objects.all().order_by('date_joined')
        
        if restaurant:
            # Get users from selected restaurant
            restaurants = Restaurant.objects.filter(name=restaurant)
        
            drivers = Driver.objects.none()

            for restaurant in restaurants:
                drivers |= restaurant.drivers.all().annotate(restaurant_name=F('restaurant__name')).order_by('date_joined')

            queryset = drivers
            
        else:
            queryset = queryset.annotate(restaurant_name=F('restaurant__name'))
        
        
        # Filtering by status
        if status == 'True':
            queryset = queryset.filter(is_active=True)
        elif status == 'False':
            queryset = queryset.filter(is_active=False)

        # Additional filtering using Q
        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) | Q(email__icontains=query))

        

        paginator = UsersPagination()
        result_page = paginator.paginate_queryset(queryset, request)

        serialized_data = []
        for user in result_page:
            user_data = serializer_class(user).data
            address_data = self.get_addresses(user.username)
            user_data.update(address_data)
            serialized_data.append(user_data)

        response_data = {
            'posts_amount': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'current_page': paginator.page.number,
            'results': serialized_data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'total_results': queryset.count(),
        }
        
        return JsonResponse(response_data, status=200)




class AddDailyReport(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        data['start_work'] = datetime.strptime(data['start_shift'], '%H:%M').time()
        data['end_work'] = datetime.strptime(data['end_shift'], '%H:%M').time()
        
        # Working time
        working_time = datetime.combine(date.min, data['end_work']) - datetime.combine(date.min, data['start_work'])
        hours, remainder = divmod(working_time.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        data['working_time'] = '{:02}:{:02}'.format(hours, minutes)
        # Working time
        
        data['driver'] = Driver.objects.get(username=data['driver'])

        serializer = DailyDriverReportSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'ok'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
        
class GenerateReport(APIView):
    permission_classes = [IsAuthenticated]
    
    def create_csv(self, user_working):
        
        self.filename = f"temp_{uuid.uuid4()}.csv"
        
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(['Driver', 'Date', 'Orders amount', 'Start work', 'End work', 'Working time', 'Orders per hour'])


            total_working_time = timedelta()
            
            total_orders = 0

            for item in user_working:
                writer.writerow([item.driver, item.date, item.orders, item.start_work, item.end_work, item.working_time, item.orders_per_hour])
                

                working_time = timedelta(hours=item.working_time.hour, minutes=item.working_time.minute, seconds=item.working_time.second)
                total_working_time += working_time
                
                total_orders += item.orders

            total_time = (datetime.min + total_working_time).time()

            writer.writerow(['Total', '', total_orders, '', '', total_time, ''])

        django_file = File(open(self.filename, 'r'))

        return django_file
    
    def get(self, request, username):
        start_date = self.request.query_params.get('start_date', '').strip()
        end_date = self.request.query_params.get('end_date', '').strip()
        monthly_day = self.request.query_params.get('monthly_day', '').strip()
        monthly = self.request.query_params.get('monthly', '').strip()
        
        
        user = Driver.objects.get(username=username)
        
        if monthly == 'true':
            user_working = DailyWork.objects.filter(driver=user, date__range=[start_date, end_date])
            
        else:
            user_working = DailyWork.objects.filter(driver=user, date__range=[start_date, end_date])

        self.create_csv(user_working)
        
        try:
            wrapper = FileWrapper(open(self.filename, 'rb'))
            response = FileResponse(wrapper, content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={self.filename}'
            return response
        finally:
            os.remove(self.filename)




class CreateWageTariff(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        serializer = WageTariffSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'ok'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
class EditWageTariff(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        tariff = WageTariff.objects.get(id=id)
        data = request.data
        
        serializer = WageTariffSerializer(instance=tariff, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'ok'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
        
class GetWageTariffs(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        tariffs = WageTariff.objects.all()
        serializer = WageTariffSerializer(tariffs, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    
    
class GetWageTariffId(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, name):
        tariff = WageTariff.objects.get(name=name)
        serializer = WageTariffGetIdSerializer(tariff)
        return JsonResponse(serializer.data, status=200, safe=False)    
    

class DeleteWageTariff(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WageTariff.objects.all()
    serializer_class = WageTariffSerializer
    lookup_field = 'id'


class AssignWageTariff(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, username):
        driver = Driver.objects.get(username=username)
        tariff = WageTariff.objects.get(id=request.data['wage_tariff'])
        driver.wage_tariff = tariff
        driver.save()
        
        return JsonResponse({'message': 'ok'}, status=201)
    
    

class GetNewBillingPeriodStartingDay(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, name):
        tariff = WageTariff.objects.get(name=name)
        serializer = NewBillingPeriodSerializer(tariff)
        return JsonResponse(serializer.data, status=200, safe=False) 

    
    
    
class GetDailyDriversReport(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = UsersPagination
    
    def create_csv(self, user_working):
        
        self.filename = f"temp_{uuid.uuid4()}.csv"
        
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(['Driver', 'Date', 'Orders amount', 'Start work', 'End work', 'Working time', 'Orders per hour'])


            total_working_time = timedelta()
            
            total_orders = 0

            for item in user_working:

                writer.writerow([item['driver'], item['date'], item['orders'], item['start_work'], item['end_work'], item['working_time'], item['orders_per_hour']])
                
                working_time_str = item['working_time']
                working_time_obj = datetime.strptime(working_time_str, "%H:%M:%S")

                working_time = timedelta(hours=working_time_obj.hour, minutes=working_time_obj.minute, seconds=working_time_obj.second)

                total_working_time += working_time
                
                total_orders += item['orders']

            total_time = (datetime.min + total_working_time).time()

            writer.writerow(['Total', '', total_orders, '', '', total_time, ''])

        django_file = File(open(self.filename, 'r'))

        return django_file
    
    def get(self, request):
        limit = self.request.query_params.get('limit', '').strip()
        query = self.request.query_params.get('search', '').strip()
        restaurant = self.request.query_params.get('restaurant', '').strip()
        download = self.request.query_params.get('download', '').strip()
        start_date = self.request.query_params.get('start_date', '').strip()
        end_date = self.request.query_params.get('end_date', '').strip()

        # print(DailyWork.objects.all().order_by('-date'))
        if start_date and end_date:
            queryset = DailyWork.objects.filter(date__range=[start_date, end_date]).order_by('-date')
        elif start_date:
            queryset = DailyWork.objects.filter(date__gte=start_date).order_by('-date')
        elif end_date:
            queryset = DailyWork.objects.filter(date__lte=end_date).order_by('-date')
        else:
            queryset = DailyWork.objects.all().order_by('-date')
            
        if restaurant:
            restaurants = Restaurant.objects.filter(id__in=restaurant)
            drivers = Driver.objects.none()

            for restaurant in restaurants:
                drivers |= restaurant.drivers.all().annotate(restaurant_name=F('restaurant__name')).order_by('date_joined')

            queryset = queryset.filter(driver__in=drivers)
            
        
        if query:
            try:
                query_date = datetime.strptime(query, "%Y-%m-%d").date()
                queryset = queryset.filter(
                    Q(driver__username__icontains=query) | Q(date=query_date))
            except ValueError:
                queryset = queryset.filter(driver__username__icontains=query)
            
            
            
        serializer = DailyDriverReportSerializer(queryset, many=True)

        paginator = UsersPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        
        if download == 'true':
            self.create_csv(serializer.data)
            
            try:
                wrapper = FileWrapper(open(self.filename, 'rb'))
                response = FileResponse(wrapper, content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename={self.filename}'
                return response
            finally:
                os.remove(self.filename)
                
        else:
            response_data = {
                'posts_amount': paginator.page.paginator.count,
                'total_pages': paginator.page.paginator.num_pages,
                'current_page': paginator.page.number,
                'results': serializer.data,
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link(),
                'total_results': queryset.count(),
            }

            return JsonResponse(response_data, status=200)
        
        
        
class GetMonthlySettlementForDrivers(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        drivers = request.data.get('drivers', [])
        




class GetRestaurants(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.query_params.get('username')
        user = Driver.objects.get(username=username)
        
        restaurants = Restaurant.objects.filter(drivers=user)
        serialized = RestaurantNameIdSerializer(restaurants, many=True)
        return JsonResponse(serialized.data, safe=False)
    
    
class GetRestaurantPhoneNumber(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, username):
        user = Driver.objects.get(username=username)
        
        restaurants = Restaurant.objects.filter(drivers=user)
        serializer = GetRestaurantPhoneSerializer(restaurants, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    
    
class GetRatings(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            ratings = Rating.objects.all().order_by('-rating')
            serializer = GetRatingSerializer(ratings, many=True)
            return JsonResponse(serializer.data, status=200, safe=False)
        except Rating.DoesNotExist:
            return JsonResponse({'error': 'No ratings found'}, status=404)
        


class ManageRating(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        serializer = GetRatingSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Successfully created'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    
    def put (self, request, id):
        rating = Rating.objects.get(id=id)
        data = request.data
        serializer = GetRatingSerializer(instance=rating, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Successfully updated '}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


class DeleteRating(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = GetRatingSerializer
    lookup_field = 'id'
    

class UpdateUserRating(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, username, rate):
        user = Driver.objects.get(username=username)
        
        data = {
            'rate': rate
        }
        
        serializer = UserRating(user, data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Successfully updated '}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
        
class GetRateInfoForDriver(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, username):
        user = Driver.objects.get(username=username)
        rate = user.rate
        
        serializer = GetRatingSerializer(rate)
        return JsonResponse(serializer.data, status=200, safe=False)
    
    
