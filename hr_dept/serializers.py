from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import HRUser
from users.models import GeneralUser

from users.serializers import GetAddressesSerializer


class GetHRUser(serializers.ModelSerializer):
    class Meta:
        model = HRUser
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


class HRUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = HRUser
        fields = ['email',
                  'first_name',
                  'is_active',
                  'last_name',
                  'user_role',
                  'username',
                  'phone',
                  'date_joined']


class AddHRUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = HRUser
        fields = '__all__'


class UpdateHRUser(serializers.ModelSerializer):
    class Meta:
        model = HRUser
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
