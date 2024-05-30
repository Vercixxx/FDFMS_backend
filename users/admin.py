from django.contrib import admin

from .models import GeneralUser, Addresses
from .forms import GeneralUserAdminConf


class GeneralUserAdmin(admin.ModelAdmin):
    form = GeneralUserAdminConf
    list_display = ['username', 'user_role', 'is_active']
    
admin.site.register(GeneralUser, GeneralUserAdmin)

@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ['username']