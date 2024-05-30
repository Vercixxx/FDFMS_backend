from django.db import models
from users.models import GeneralUser

class HRUser(GeneralUser):

    class Meta:
        db_table = 'HRUser'
        
    def __str__(self):
        return self.username