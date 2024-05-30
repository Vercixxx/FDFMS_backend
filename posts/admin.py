from django.contrib import admin

from .models import Posts,DriverPosts

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Posts._meta.fields]
    
@admin.register(DriverPosts)
class DriverPostsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DriverPosts._meta.fields]