from django.contrib import admin
from .models import Restaurant, Brands, DriverShift

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Restaurant._meta.fields]
    filter_horizontal = ['managers', 'drivers']
    
@admin.register(DriverShift)
class DriverShiftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DriverShift._meta.fields]


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brands._meta.fields]