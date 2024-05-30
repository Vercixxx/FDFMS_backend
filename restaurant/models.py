from django.db import models
from rest_manager.models import RestManager
from driver.models import Driver
from car.models import Car

from datetime import datetime


class Brands(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    
    #address 
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    home = models.CharField(max_length=10, blank=True, null=True)
    apartament = models.CharField(max_length=10, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)

class Restaurant(models.Model):
    id = models.AutoField(primary_key=True) 
    
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brands, db_column='brand', on_delete=models.SET_NULL, null=True)
    managers = models.ManyToManyField(RestManager, blank=True)
    
    phone = models.CharField(max_length=20, blank=True, null=True)

    #address 
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    home = models.CharField(max_length=10, blank=True, null=True)
    apartament = models.CharField(max_length=10, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    
    # Drivers
    drivers = models.ManyToManyField(Driver, blank=True)

class DriverShift(models.Model):
    driver = models.ForeignKey(Driver, db_column='driver', on_delete=models.SET_NULL, null=True, default=None)
    restaurant = models.ForeignKey(Restaurant, db_column='restaurant', on_delete=models.SET_NULL, null=True, default=None)
    
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    
