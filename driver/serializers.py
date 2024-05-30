from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import Driver, DailyWork, WageTariff, Rating
from users.models import GeneralUser

from users.serializers import GetAddressesSerializer


class BasicDriverDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['username', 'first_name', 'last_name', 'user_color']

class GetDriver(serializers.ModelSerializer):
    wage_tariff = serializers.StringRelatedField()
    class Meta:
        model = Driver
        fields = ['email',
                  'username',
                  'first_name',
                  'last_name',
                  'is_active',
                  'user_role',
                  'phone',
                  'bank_account_number',
                  'pesel_nip',
                  'tax_office_name',
                  'tax_office_address',
                  'nfz',
                  'license_number',
                  'ln_release_date',
                  'ln_expire_date',
                  'ln_published_by',
                  'ln_code',
                  'wage_tariff',
                  'rate',
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        addresses_serializer = GetAddressesSerializer()
        for field_name, _ in addresses_serializer.fields.items():
            source_field = f'addresses.{field_name}'
            self.fields[field_name] = serializers.CharField(
                source=source_field)


class DriverSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')
    wage_tariff = serializers.StringRelatedField()

    class Meta:
        model = Driver
        fields = ['email',
                  'first_name',
                  'is_active',
                  'last_name',
                  'user_role',
                  'username',
                  'phone',
                  'date_joined',
                  'wage_tariff',
                  'rate',
                  ]


class RestaurantDriversSerliazer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(read_only=True)
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')
    wage_tariff = serializers.StringRelatedField()

    class Meta:
        model = Driver
        fields = ['email',
                  'first_name',
                  'is_active',
                  'last_name',
                  'user_role',
                  'username',
                  'phone',
                  'date_joined',
                  'restaurant_name',
                  'wage_tariff',
                  'rate',
                  ]

class DriverUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['username', 'first_name', 'last_name']


class AddDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class UpdateDriverUser(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'phone',
            'bank_account_number',
            'pesel_nip',
            'tax_office_name',
            'tax_office_address',
            'nfz',
            'license_number',
            'ln_release_date',
            'ln_expire_date',
            'ln_published_by',
            'ln_code',
            'wage_tariff',
            'rate',
        ]


class DailyDriverReportSerializer(serializers.ModelSerializer):
    start_work = serializers.TimeField(format='%H:%M')
    end_work = serializers.TimeField(format='%H:%M')
    working_time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = DailyWork
        fields = ['id','driver', 'date', 'orders', 'start_work', 'end_work', 'working_time', 'orders_per_hour']
        
class NewBillingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = WageTariff
        fields = ['starting_new_billing_period', 'name']
        

class WageTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = WageTariff
        fields = '__all__'
        
class WageTariffGetIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = WageTariff
        fields = ['id']
        

class GetRatingSerializer(serializers.ModelSerializer):
    hour = serializers.TimeField(format='%H:%M')
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'day', 'hour']

class UserRating(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['rate']