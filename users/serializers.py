from rest_framework import serializers 

from .models import GeneralUser, Addresses



class GeneralUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = GeneralUser
        fields = ['username', 'email' , 'user_role', 'is_active', 'date_joined']
        

class GetAllUsernamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralUser
        fields = ['username']
        
        
class GeneralAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'
        
   
class ResidenceAddressSerializer(serializers.ModelSerializer):
    residence_state = serializers.StringRelatedField(source='residence_state.name')
    class Meta:
        model = Addresses
        fields = ['residence_country',
                  'residence_state',
                  'residence_city',
                  'residence_street',
                  'residence_home_number',
                  'residence_apartment_number',
                  'residence_zip_code',
                  ]

    
class GetAddressesSerializer(serializers.Serializer):
    residence_country = serializers.CharField()
    residence_state = serializers.CharField()
    residence_city = serializers.CharField()
    residence_street = serializers.CharField()
    residence_home_number = serializers.CharField()
    residence_apartment_number = serializers.CharField()
    residence_zip_code = serializers.CharField()

    registered_country = serializers.CharField()
    registered_state = serializers.CharField()
    registered_city = serializers.CharField()
    registered_street = serializers.CharField()
    registered_home_number = serializers.CharField()
    registered_apartment_number = serializers.CharField()
    registered_zip_code = serializers.CharField()

    correspondence_country = serializers.CharField()
    correspondence_state = serializers.CharField()
    correspondence_city = serializers.CharField()
    correspondence_street = serializers.CharField()
    correspondence_home_number = serializers.CharField()
    correspondence_apartment_number = serializers.CharField()
    correspondence_zip_code = serializers.CharField()

    def to_representation(self, instance):
        return {
            'residence_country': instance.residence_country.name if instance.residence_country else None,
            'residence_state': instance.residence_state.name if instance.residence_state else None,
            'residence_city': instance.residence_city,
            'residence_street': instance.residence_street,
            'residence_home_number': instance.residence_home_number,
            'residence_apartment_number': instance.residence_apartment_number,
            'residence_zip_code': instance.residence_zip_code,

            'registered_country': instance.registered_country.name if instance.registered_country else None,
            'registered_state': instance.registered_state.name if instance.registered_state else None,
            'registered_city': instance.registered_city,
            'registered_street': instance.registered_street,
            'registered_home_number': instance.registered_home_number,
            'registered_apartment_number': instance.registered_apartment_number,
            'registered_zip_code': instance.registered_zip_code,

            'correspondence_country': instance.correspondence_country.name if instance.correspondence_country else None,
            'correspondence_state': instance.correspondence_state.name if instance.correspondence_state else None,
            'correspondence_city': instance.correspondence_city,
            'correspondence_street': instance.correspondence_street,
            'correspondence_home_number': instance.correspondence_home_number,
            'correspondence_apartment_number': instance.correspondence_apartment_number,
            'correspondence_zip_code': instance.correspondence_zip_code,
        }