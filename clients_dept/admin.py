from django.contrib import admin
from .models import ClientsUser

@admin.register(ClientsUser)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_role', 'is_active']
