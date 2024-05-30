from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import AssetUser
from users.models import GeneralUser

from users.serializers import GetAddressesSerializer

class GetAssetUser(serializers.ModelSerializer):
    class Meta:
        model = AssetUser
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
            self.fields[field_name] = serializers.CharField(source=source_field)
class AssetSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = AssetUser
        fields = ['email', 
                  'first_name', 
                  'is_active', 
                  'last_name', 
                  'user_role', 
                  'username', 
                  'phone' ,
                  'date_joined',]


class AddAssetUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AssetUser
        fields = '__all__'


class UpdateAssetUser(serializers.ModelSerializer):
    class Meta:
        model = AssetUser
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
    
