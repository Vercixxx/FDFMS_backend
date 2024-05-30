from django.urls import path

from . import views

urlpatterns = [
    path('create-hr/', views.create_user),
]
