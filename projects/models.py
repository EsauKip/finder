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

    @classmethod
    def search_hood(self,search_name):
        hoods = Neighborhood.objects.filter(location__icontains=search_name) 
        return hoods       

class HoodMember(models.Model):
        member = models.ForeignKey(User,on_delete=models.CASCADE)
        hood = models.ForeignKey(Neighborhood,related_name='members',on_delete=models.CASCADE)
        date_joined = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return'{} in {}'.format(self.member, self.hood)

class Post(models.Model):
    image = CloudinaryField('image', null=True)
    content=models.TextField(max_length=100)
    author=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    neighborhood = models.ForeignKey(Neighborhood,related_name='hoodposts',on_delete=models.CASCADE)
    def __str__(self):
        return self.content

    def save_post(self):
        self.save()
    def delete_post(self):
        self.delete()      

    def edit_post(self,new_content):
        self.content = new_content
        self.save()     

    @classmethod
    def get_posts(cls):
        posts = Post.objects.all()
        return posts    