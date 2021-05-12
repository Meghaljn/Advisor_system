import urllib

from django.core.files import File
from django.db import models
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import os
#from django.contrib.auth.models import AbstractUser


class advisors(models.Model):
    name = models.CharField(max_length=100,default='')
    photo_url = models.URLField(max_length = 250,default ='')
    image_file = models.ImageField(upload_to='images',blank = True,)

    def save(self, *args, **kwargs):
        if self.photo_url and not self.image_file:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.photo_url).read())
            img_temp.flush()
            self.image_file = self.image_file.save(f"image_{self.pk}", File(img_temp))
        super(advisors, self).save(*args, **kwargs)

class Users(models.Model):
    username = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=30,default='')
    password = models.CharField(max_length=30,default='')
   # password2 =  models.CharField(max_length=30,default='')

class booking(models.Model):
    user_id = models.CharField(max_length=100,default='')
    advisor_id =models.CharField(max_length=100,default='')
    booking_date_time = models.DateTimeField(null = True,blank =True)

# Create your models here.
