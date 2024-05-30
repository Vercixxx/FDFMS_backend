from django.db import models
from users.models import GeneralUser

class AssetUser(GeneralUser):

    class Meta:
        db_table = 'AssetUser'
        
    def __str__(self):
        return self.username