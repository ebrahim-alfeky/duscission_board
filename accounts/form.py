from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    # email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2', 'last_name'] 