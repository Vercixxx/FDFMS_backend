from django.urls import path, include
from . import views

urlpatterns = [
    
    # Creating account
    path('api/create/', views.AddUser.as_view(), name="add-user"),
    
    # Deliting account
    path('api/users/delete/<str:username>/', views.DeleteUser.as_view(), name='delete_user'),
    
    # Modify user
    path('api/users/update/<str:username>/<str:user_role>/', views.UpdateUser.as_view(), name='update-user'),
    
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    
    # Logging
    path('api/v1/login/', views.UserAuth.as_view(), name='login'),
    
    # Get User data
    path('api/users/get/<str:username>/<str:user_role>/', views.getUser.as_view(), name="get-user"),
    
    # Get users
    path('api/users/getall', views.GetGeneralUsers.as_view(), name="get-users"),
    
    # Save User data
    path('api/users/save/<str:username>/<str:user_role>/', views.UpdateUser.as_view(), name="save-user"),
    
    # Change user state
    path('api/users/change-state/<str:username>/', views.ChangeUserState.as_view(), name="change-user-state"),

    # Get usernames
    path('api/users/get-usernames/', views.GetUsernames.as_view(), name="get-usernames"),
    
    # Get user info CSV
    path('api/users/get-info-csv/<str:username>/<str:user_role>/', views.GenerateUserInfoCSV.as_view(), name="get-user-info-csv"),
    
]