from django.contrib import admin
from .models import Driver, DailyWork, WageTariff, Rating

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(DailyWork)
class DailyWorkAdmin(admin.ModelAdmin):
    pass

@admin.register(WageTariff)
class WageTariffAdmin(admin.ModelAdmin):
    pass

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
    