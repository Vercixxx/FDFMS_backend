from django.contrib import admin
from .models import MyMessages

@admin.register(MyMessages)
class MyMessagesAdmin(admin.ModelAdmin):
    pass
    