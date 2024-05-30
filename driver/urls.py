from django.urls import path, include
from . import views



urlpatterns = [
    path('api/drivers/get/restaurants/<str:username>/', views.GetRestaurants.as_view(), name='get_restaurants'),
    
    # Get Drivers
    path('api/drivers/get/all/', views.GetDrivers.as_view(), name='get_drivers'),
    
    # Get Drivers usernames
    path('api/drivers/get/usernames/', views.GetDriversUsernames.as_view(), name='get_drivers_usernames'),
    
    # Daily report
    path('api/drivers/daily_report/add/', views.AddDailyReport.as_view(), name='add_daily_report'),
    
    # Genre report
    path('api/drivers/generate_report/<str:username>/', views.GenerateReport.as_view(), name='generate_report'),
    
    # Get Daily reports
    path('api/drivers/daily_report/get/all/', views.GetDailyDriversReport.as_view(), name='get_daily_reports'),
    
    
    
    # WageTariff
    
    # Create WageTariff
    path('api/drivers/wage_tariff/create/', views.CreateWageTariff.as_view(), name='create_wage_tariff'),
    
    # Get WageTariffs
    path('api/drivers/wage_tariff/get/all/', views.GetWageTariffs.as_view(), name='get_wage_tariffs'),
    
    # Get WageTariffId
    path('api/drivers/wage_tariff/get/<str:name>/', views.GetWageTariffId.as_view(), name='get_wage_tariff_id'),
    
    # Edit WageTariff
    path('api/drivers/wage_tariff/edit/<int:id>/', views.EditWageTariff.as_view(), name='edit_wage_tariff'),
    
    # Delete WageTariff
    path('api/drivers/wage_tariff/delete/<int:id>/', views.DeleteWageTariff.as_view(), name='delete_wage_tariff'),
    
    # Assign WageTariff to Driver
    path('api/drivers/wage_tariff/assign/<str:username>/', views.AssignWageTariff.as_view(), name='assign_wage_tariff'),
    
    # Get New Billing Period starting day
    path('api/drivers/wage_tariff/get/new_billing_period/<str:name>/', views.GetNewBillingPeriodStartingDay.as_view(), name='get_new_billing_period'),
    
    
    # Get restaurant for driver
    path('api/drivers/get/restaurants/', views.GetRestaurants.as_view(), name='get_restaurant'),
    
    
    # Get ratings
    path('api/drivers/ratings/get/ratings/', views.GetRatings.as_view(), name='get_ratings'),
    
    # Add rating
    path('api/drivers/ratings/add/', views.ManageRating.as_view(), name='add_rating'),
    
    # Edit rating
    path('api/drivers/ratings/edit/<int:id>/', views.ManageRating.as_view(), name='edit_rating'),
    
    # Delete rating
    path('api/drivers/ratings/delete/<int:id>/', views.DeleteRating.as_view(), name='delete_rating'),
    
    # Update driver's rating
    path('api/drivers/ratings/update/<str:username>/<int:rate>/', views.UpdateUserRating.as_view(), name='update_rating'),
    
    
    # Get rate info for driver
    path('api/drivers/ratings/get/rate_info/<str:username>/', views.GetRateInfoForDriver.as_view(), name='get_rate_info'),
    
    
    
    
    # App
    path('api/drivers/get/restaurant_phone/<str:username>/', views.GetRestaurantPhoneNumber.as_view(), name='get_restaurant_phone'),
]