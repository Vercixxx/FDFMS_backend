from django.urls import path, include
from . import views

urlpatterns = [
    # Add Fleet
    path('api/fleet/add/', views.AddFleet.as_view()),
    
    # Get Fleet
    path('api/fleet/get/', views.GetFleet.as_view()),
    
    # Edit Fleet
    path('api/fleet/edit/', views.EditFleet.as_view()),
    
    # Delete Fleet
    path('api/fleet/delete/<int:id>/', views.DeleteFleet.as_view()),
    
]