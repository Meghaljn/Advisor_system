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
            result = urllib.request.urlretrieve(self.photo_url)
            self.image_file.save(
                os.path.basename(self.photo_url),
                File(open(result[0],'rb')),
                save = False
            )
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
