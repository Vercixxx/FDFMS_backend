from django.contrib import admin

from .models import Car, CarDailyReports, CarDamage

admin.site.register(Car)
admin.site.register(CarDailyReports)
admin.site.register(CarDamage)

