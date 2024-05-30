from django.db import models
from restaurant.models import Restaurant
from car.models import Car


class Fleet(models.Model):
    # Remove restaurant 
    restaurant = models.ForeignKey(Restaurant, db_column='restaurant', on_delete=models.SET_NULL, null=True, blank=True)
    cars = models.ManyToManyField(Car, db_column='cars', blank=True)
