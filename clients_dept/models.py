from django.db import models
from users.models import GeneralUser

class ClientsUser(GeneralUser):

    class Meta:
        db_table = 'ClientsUsers'
        
    def __str__(self):
        return self.username