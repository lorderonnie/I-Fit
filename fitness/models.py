from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete = models.CASCADE, default='')
    profile_pic = models.ImageField(upload_to = 'media/', default='default.jpg')
    bio = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    goal1 = models.CharField(max_length=50)
    goal2 = models.CharField(max_length=50)
    goal3 = models.CharField(max_length=50)
    goal4 = models.CharField(max_length=50)
    goal5 = models.CharField(max_length=50)
    
    
    def save_profile(self):
        
        self.save()

    @classmethod
    def get_profile_by_name(cls,name):
       
        profile = cls.objects.filter(user = name)

        return  name 
    

