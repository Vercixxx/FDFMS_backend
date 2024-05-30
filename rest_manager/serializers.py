from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import RestManager
from users.models import GeneralUser

from users.serializers import GetAddressesSerializer

class GetRestManager(serializers.ModelSerializer):
    class Meta:
        model = RestManager
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
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        addresses_serializer = GetAddressesSerializer()
        for field_name, _ in addresses_serializer.fields.items():
            source_field = f'addresses.{field_name}'
            self.fields[field_name] = serializers.CharField(
                source=source_field)

class RestManagerSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = RestManager
        fields = ['email',
                  'first_name',
                  'is_active',
                  'last_name',
                  'user_role',
                  'username',
                  'phone',
                  'date_joined']


class AddManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestManager
        fields = '__all__'

    
class UpdateRestManager(serializers.ModelSerializer):
    class Meta:
        model = RestManager
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
        ]


class GetAllManagersUI(serializers.ModelSerializer):
    class Meta:
        model = RestManager
        fields = ['username']


class GetRestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestManager
        fields = ['restaurants']