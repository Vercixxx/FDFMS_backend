from django.urls import path, include
from . import views


urlpatterns = [
    
    # ========== Countries ==========
    
    # Add
    path('api/countries/add/', views.AddCountry.as_view(), name="add-country"),
    
    # Delete
    path('api/countries/delete/<str:name>/', views.DeleteCountry.as_view(), name="delete-country"),
    
    # Get
    path('api/countries/get/', views.GetCountries.as_view(), name="get-countries"),
    
    # ========== Countries ==========
    
    
    # ========== States ==========
    
    # Add
    path('api/states/add/', views.AddState.as_view(), name="add-state"),
    
    # Delete
    path('api/states/delete/<int:id>/', views.DeleteState.as_view(), name="delete-state"),
    
    # Edit
    path('api/states/edit/<int:id>/', views.EditState.as_view(), name="edit-state"),
    
    # Get
    path('api/states/get/', views.GetStates.as_view(), name="get-states"),

    # ========== States ==========
    
]