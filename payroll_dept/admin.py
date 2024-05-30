from django.contrib import admin
from .models import PayrollUser

@admin.register(PayrollUser)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_role', 'is_active']
