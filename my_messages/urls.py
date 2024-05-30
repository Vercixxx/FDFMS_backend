from django.urls import path, include
from . import views

urlpatterns = [ 
    # Get messages
    path('api/messages/get/', views.GetMessages.as_view(), name="get-messages"),
    
    # Delete messages
    path('api/messages/delete/', views.DeleteMessages.as_view(), name="delete-messages"),
    
    # Create message
    path('api/messages/create/', views.CreateMessage.as_view(), name="create-message"),

]