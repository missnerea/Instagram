from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=60)
    password = models.CharField(max_length=80)

class Image(models.Model):
    image =models.ImageField(upload_to='/thegram',blank=True)
    caption=models.CharField(max_length=100)
    