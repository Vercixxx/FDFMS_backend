from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import GeneralUser


class GeneralUserAdminConf(UserChangeForm):
    
    new_password = forms.CharField(label='Set new password', widget=forms.PasswordInput, required=False)

    class Meta:
        model = GeneralUser
        fields = ['username', 'new_password', 'last_name', 'email', 'first_name' , 'is_active', 'user_role'] 