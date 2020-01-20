from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django import forms
from .models import Profile,

class UpdateProfileForm(forms.ModelForm):
    bio = forms.Textarea()
    class Meta:
        model = Profile
        exclude =[
            'user',
]

class UserUpdateform(forms.ModelForm):
      email = forms.EmailField()
  class Meta:
    model = User
    fields = [
        'username',
        'email',
]



