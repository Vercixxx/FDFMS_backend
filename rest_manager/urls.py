from django.urls import path

from . import views

urlpatterns = [
    # Get restaurants
    path('api/rest_manager/get_restaurants/', views.GetRestaurants.as_view()),
    
    # Get restaurants and drivers
    path('api/rest_manager/get_restaurants_and_drivers/', views.GetRestaurantsAndDrivers.as_view()),
]