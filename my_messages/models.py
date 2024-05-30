from django.db import models

# Models
from users.models import GeneralUser

class MyMessages(models.Model):
    id = models.AutoField(primary_key = True)
    
    sender = models.ForeignKey(GeneralUser, db_column='sender', on_delete=models.SET_NULL, related_name='sent_messages', null=True)
    receiver = models.ForeignKey(GeneralUser, db_column='receiver', on_delete=models.SET_NULL, related_name='received_messages', null=True)
    
    posted_date = models.DateTimeField(auto_now_add=True, null=True)
    
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    
    seen = models.BooleanField(default = False)
