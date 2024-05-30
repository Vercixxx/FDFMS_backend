from django.db import models
from users.models import GeneralUser

class RestManager(GeneralUser):

    class Meta:
        db_table = 'Managers'
        
    def __str__(self):
        return self.username