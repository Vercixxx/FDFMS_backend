from rest_framework.response import Response

from django.http import JsonResponse

# Rest
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Models
from rest_manager.models import RestManager

# Serializers
from rest_manager.serializers import GetAllManagersUI

class DisablePagination(PageNumberPagination):
    page_size = None

class GetUsernames(APIView):

    def get(self, request):
        users = RestManager.objects.all()
        usernames = [user.username for user in users]

        return Response(usernames)