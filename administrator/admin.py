from django.contrib import admin
from .models import Administrator

@admin.register(Administrator)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_role', 'is_active']
