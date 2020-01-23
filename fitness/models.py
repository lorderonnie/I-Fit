from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete = models.CASCADE, default='')
    profile_pic = models.ImageField(upload_to = 'media/', default='default.jpg',blank=True)
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
    

class Workouts(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    workout_name = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    body_section = models.CharField(max_length=60)
    date_created =  models.DateTimeField(auto_now_add=True)
    number_of_sets = models.IntegerField(default=0)
    
    def save_workout():
        self.save()
        
    def delete_workout():
        self.delete()
        
    @classmethod
    def get_all_workouts(cls):
        workouts = cls.objects.all()
        return workouts
        
    @classmethod
    def get_workout_by_workout_name(cls,name):
        workouts = cls.objects.filter(workout_name=workout_name)
        return workouts

    
    
    
    
          