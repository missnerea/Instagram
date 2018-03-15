from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class Profile(models.Model):
    profile_picture=models.ImageField(upload_to='user/',blank=True)
    email=models.CharField(max_length=60)
    password = models.CharField(max_length=80)
    user = models.OnetoOneField(User,on_delete=models.CASCADE,null=True)

    def save_profile(self):
          self.save()

    @classmethod
    def get_profiles(cls):
          profiles = Profile.objects.all()
          return profiles
    

class Image(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)    
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
      comments = models.CharField(max_length=60,blank=True,null=True)
      comment_time = models.DateTimeField(auto_now_add=True)
      user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
      pic = models.ForeignKey(Image,on_delete=models.CASCADE, related_name='comments',blank=True)

      def __str__(self):
            return self.comments

      class Meta:
            ordering = ['-comment_time']

      def save_comment(self):
            return self.save()

      def delete_comment(self):
            return self.delete()

      @classmethod
      def get_comments(cls):
            comment = Comment.objects.all()
            return comment

