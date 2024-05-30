from django.contrib import admin
from .models import RestManager

@admin.register(RestManager)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_role', 'is_active']
