from django.db import models
from users.models import GeneralUser

class PayrollUser(GeneralUser):

    class Meta:
        db_table = 'PayrollUsers'
        
    def __str__(self):
        return self.username