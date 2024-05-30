from django.urls import path, include
from . import views


urlpatterns = [
    # path('api/cars/', include(car_router.urls)),
    
    # Get Cars
    path('api/car/getall/', views.GetCars.as_view(), name="get-cars"),
    
    # Creating car
    path('api/car/create/', views.AddCar.as_view(), name="add-cars"),
    
    # Delete car
    path('api/car/delete/<int:vin>/', views.DeleteCar.as_view(), name="delete-car"),
    
    # Get car info
    path('api/car/get/<int:vin>/', views.GetCar.as_view(), name="get-car"),
    
    # Edit car
    path('api/car/edit/<int:vin>/', views.EditCar.as_view(), name="edit-car"),
    
    # Get cars by search
    path('api/cars/get/', views.GetVinLicensePlate.as_view(), name="get-cars-by-search"),
    
    
    # Create car daily reports
    path('api/car/dailyreport/add/', views.AddDailyReport.as_view(), name="add-daily-report"),
    
    # Get car daily reports
    path('api/car/dailyreport/get/', views.GetCarsDailyReports.as_view(), name="get-daily-report"),
    
    # Add car damage
    path('api/car/damage/add/', views.AddCarDamage.as_view(), name="add-car-damage"),
    
    # Get car damage
    path('api/car/damage/get/<int:vin>/', views.GetCarDamages.as_view(), name="get-car-damage"),
]