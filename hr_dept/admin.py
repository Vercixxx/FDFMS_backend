from django.contrib import admin
from .models import HRUser

@admin.register(HRUser)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_role', 'is_active']
