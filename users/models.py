from django.db import models
from django.contrib.auth.models import AbstractUser

from other.models import Country, State

class GeneralUser(AbstractUser):
    
    # Username
    username = models.CharField(
        max_length=10,
        primary_key = True,
    )

    # User rank
    ROLE_CHOICES = (
        ('HR', 'HR'),
        ('Payroll', 'Payroll'),
        ('Asset', 'Asset'),
        ('Clients', 'Clients'),
        ('Manager', 'Manager'),
        ('Driver', 'Driver'),
        ('Administrator', 'Administrator'),
        )
    
    user_role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Administrator'
    )
    
    phone = models.CharField(max_length=20, blank=True, null=True)

    
    bank_account_number = models.CharField(max_length=30, blank=True, null=True)
    pesel_nip = models.CharField(max_length=12, blank=True, null=True)
    tax_office_name = models.CharField(max_length=80, blank=True, null=True)
    tax_office_address = models.CharField(max_length=220, blank=True, null=True)

    nfz = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.username
    
    
    
class Addresses(models.Model):
    username = models.OneToOneField(GeneralUser, db_column="username", on_delete=models.CASCADE, primary_key=True)
    
    # Address of residence
    residence_country = models.ForeignKey(Country, db_column="residence_country", on_delete=models.CASCADE, related_name='residence_addresses')
    residence_state = models.ForeignKey(State, db_column="residence_state", on_delete=models.CASCADE, related_name='residence_addresses')
    
    residence_city = models.CharField(max_length=100, blank=True, null=True)
    residence_street = models.CharField(max_length=200, blank=True, null=True)
    residence_home_number = models.CharField(max_length=10, blank=True, null=True)
    residence_apartment_number = models.CharField(max_length=10, blank=True, null=True)
    residence_zip_code = models.CharField(max_length=10, blank=True, null=True)
    
    
    # Address of registeredresidence_country
    registered_country = models.ForeignKey(Country, db_column="registered_country", on_delete=models.CASCADE, related_name='registered_addresses')
    registered_state = models.ForeignKey(State, db_column="registered_state", on_delete=models.CASCADE, related_name='registered_addresses')
    
    registered_city = models.CharField(max_length=100, blank=True, null=True)
    registered_street = models.CharField(max_length=200, blank=True, null=True)
    registered_home_number = models.CharField(max_length=10, blank=True, null=True)
    registered_apartment_number = models.CharField(max_length=10, blank=True, null=True)
    registered_zip_code = models.CharField(max_length=10, blank=True, null=True)
    
    # Address of correspondence
    correspondence_country = models.ForeignKey(Country, db_column="correspondence_country", on_delete=models.CASCADE, related_name='correspondence_addresses')
    correspondence_state = models.ForeignKey(State, db_column="correspondence_state", on_delete=models.CASCADE, related_name='correspondence_addresses')
    
    correspondence_city = models.CharField(max_length=100, blank=True, null=True)
    correspondence_street = models.CharField(max_length=200, blank=True, null=True)
    correspondence_home_number = models.CharField(max_length=10, blank=True, null=True)
    correspondence_apartment_number = models.CharField(max_length=10, blank=True, null=True)
    correspondence_zip_code = models.CharField(max_length=10, blank=True, null=True)
