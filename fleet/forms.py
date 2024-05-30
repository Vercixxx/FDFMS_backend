from django import forms
from .models import Fleet

class FleetAdminForm(forms.ModelForm):
    class Meta:
        model = Fleet
        fields = ['id', 'restaurant', 'cars']
