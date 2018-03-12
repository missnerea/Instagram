from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class User(models.Model):
    profile_picture=models.ImageField(upload_to='user/',blank=True)
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=60)
    password = models.CharField(max_length=80)
    editor = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    

class Image(models.Model):
    
    user = models.ForeignKey(User,null = True)
    image_image =models.ImageField(upload_to='images/',blank=True)
    caption=models.CharField(max_length=100)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='image_likes')
         
    @classmethod
    def this_image(cls):
        img = cls.objects.all()
        return img 

    def save_image(self):
        self.save

    

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True)
    image_image = models.ForeignKey(Image, null=True)
    time_comment = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
       ordering=['-time_comment'] 