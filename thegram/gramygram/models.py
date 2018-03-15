from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    profile_picture=models.ImageField(upload_to='user/',blank=True)
    email=models.CharField(max_length=60)
    bio = models.CharField(max_length=100,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def save_profile(self):
          self.save()

    @classmethod
    def this_profile(cls):
          profile = cls.objects.all()
          return profile

    @property
    def profile_picture_url(self):
           if self.profile_picture and hasattr(self.profile_picture, 'url'):
                 return self.profile_picture.url
        

    

class Image(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=60, null=True)    
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


def Create_profile(sender, **kwargs):
      if kwargs['created']:
       user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(Create_profile,sender=User)
