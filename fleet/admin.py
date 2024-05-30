from django.contrib import admin
from .models import Fleet
from .forms import FleetAdminForm
from car.models import Car

@admin.register(Fleet)
class FleetAdmin(admin.ModelAdmin):
    form = FleetAdminForm
    list_display = ['id', 'restaurant', 'display_cars']
    filter_horizontal = ['cars']

    def display_cars(self, obj):
        return ", ".join([car.vin for car in obj.cars.all()])

    display_cars.short_description = "Cars"

