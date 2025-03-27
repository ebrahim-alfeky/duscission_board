from django import forms #! module in django  forms api
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm

class Board1(forms.ModelForm):
    class Meta:
        model=Board
        fields=['name','description','created_by']
    
class Topic1(forms.ModelForm):#! ModelForm => sub class in forms
    class Meta:
        model=Topic
        fields=['subject','board']

class Post1(forms.ModelForm):
    class Meta:
        model=Post
        fields=['message','topic']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'password1', 'password2'] 