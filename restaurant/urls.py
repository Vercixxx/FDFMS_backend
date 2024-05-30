from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # Creating restaurant
    path('api/restaurant/create/', views.CreateRestaurant.as_view(), name="create-restaurant"),
    
    # Updating restaurant
    path('api/restaurant/update/<str:name>/', views.UpdateRestaurant.as_view(), name="update-restaurant"),
    
    # Deliting restaurant
    path('api/restaurant/delete/<int:id>/', views.DeleteRestaurant.as_view(), name='delete-restaurant'),
    
    # Get restaurants
    path('api/restaurants/get/', views.GetRestaurants.as_view(), name='get-restaurants'),
    
    # Get restaurant
    path('api/restaurant/get/<int:id>/', views.GetRestaurants.as_view(), name='get-restaurant'),
    
    # Get restaurant name, id
    path('api/restaurant/get/name-id/', views.GetRestaurantsNameId.as_view(), name='get-restaurant-name-id'),
    
    # Get Restaurant and their drivers with brands
    path('api/restaurant/get/drivers/<str:restaurant>/', views.GetRestaurantsAndDriversWithBrands.as_view(), name='get-restaurant-drivers'),
    
    
    # Brands Brands Brands
    
    # Creating Brand
    path('api/brands/create/', views.CreateBrand.as_view(), name="create-brand"),
    
    # Getting all brands
    path('api/brands/get-all/', views.GetBrands.as_view(), name='get-all-brands'),
    
    # Getting brand info
    path('api/brands/get-info/<int:id>/', views.GetBrands.as_view(), name='get-existing-brands'),
    
    # Deleting brand
    path('api/brands/delete/<int:id>/', views.DeleteBrands.as_view(), name='delete-brand'),
    
    # Updating Brand
    path('api/brands/update/<int:brandID>/', views.UpdateBrand.as_view(), name='update-brand'),
    
    # Get Driver shifts
    path('api/restaurant/driver-shifts/', views.GetDriverShifts.as_view(), name='driver-shifts'),
    
    # Create od update driver shift
    path('api/restaurant/driver-shifts/create-update/', views.CreateUpdateDriverShift.as_view(), name='create-update-driver-shift'),
    
    # Delete driver shift
    path('api/restaurant/driver-shifts/delete/<int:id>/', views.DeleteDriverShift.as_view(), name='delete-driver-shift'),
    
    
    # Assign driver for shift
    path('api/restaurant/assign-driver/', views.AssignDriverForShift.as_view(), name='assign-driver'),
    
    
]

    