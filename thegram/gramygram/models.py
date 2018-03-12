from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=60)
    password = models.CharField(max_length=80)

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
