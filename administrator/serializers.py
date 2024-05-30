from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Administrator
from users.models import GeneralUser

from users.serializers import GetAddressesSerializer


class GetAdministrator(serializers.ModelSerializer):
    class Meta:
        model = Administrator
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


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ['email',
                  'first_name',
                  'is_active',
                  'last_name',
                  'user_role',
                  'username',
                  'phone',
                  'date_joined']


class AddAdministratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Administrator
        fields = '__all__'


class UpdateAdministrator(serializers.ModelSerializer):
    class Meta:
        model = Administrator
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
