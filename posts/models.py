from django.db import models

# Models
from users.models import GeneralUser


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    
    author = models.ForeignKey(GeneralUser, db_column='author', on_delete=models.CASCADE, null=True)
    posted_date = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    
class DriverPosts(models.Model):
    id = models.AutoField(primary_key=True)
    
    author = models.ForeignKey(GeneralUser, db_column='author', on_delete=models.CASCADE, null=True)
    posted_date = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)