from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
        primary_key=True
    )
    
    def __str__(self):
        return f"{self.name}"

class State(models.Model):
    name = models.CharField(
        max_length=100,
    )
    country = models.ForeignKey(Country, db_column='country', on_delete = models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.country.name})"