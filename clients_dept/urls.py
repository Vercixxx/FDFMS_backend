from django.urls import path, include
from . import views

# Rest
urlpatterns = [
    path('api/managers/get_username_all/', views.GetUsernames.as_view(), name='get-usernames'),
]