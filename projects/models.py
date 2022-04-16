from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    creator = models.ForeignKey(User,null =True,on_delete=models.SET_NULL)
    profile_pic = CloudinaryField('image', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    def delete_hood(self):
        self.delete() 

    def save_hood(self,value):
        self.name = value
        self.save()
    @classmethod
    def all_hoods(self):
        hoods =Neighborhood.objects.all()
        return hoods    