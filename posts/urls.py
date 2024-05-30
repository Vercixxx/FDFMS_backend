from django.urls import path, include
from . import views

urlpatterns = [ 
    # Get posts
    path('api/posts/get/<str:target>/', views.GetPosts.as_view(), name="get-posts"),
    
    # Get drivers posts for mobile
    path('api/app/posts/get/drivers/', views.GetDriversPostsMobile.as_view(), name="get-drivers-posts-mobile"),
    
    # Create post
    path('api/posts/create/<str:target>', views.CreatePost.as_view(), name="create-post"),
    
    # Delete post
    path('api/posts/delete/<str:target>/<int:id>/', views.DeletePost.as_view(), name="delete-post"),
    
]