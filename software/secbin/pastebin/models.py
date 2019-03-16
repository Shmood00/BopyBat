from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from cryptography.fernet import Fernet
from secbin.settings import db_key
from django import forms
from datetime import datetime, timedelta
import os
from uuid import uuid4
from .validators import validate_file_size_type

#Changes post upload filename 
def unique_file_name(instance, filename):
    upload_to = 'post_content'
    ext = filename.split('.')[-1]

    if instance.title:
        filename = '{}.{}'.format(instance.title, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    
    return os.path.join(upload_to, filename)

# Create your models here.
class Bopie(models.Model):
    bopie_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #creating foreign key relationship with user and bopies
    
    #Slug field for the pastebin-like URLs to be stored in
    slug = models.SlugField(max_length=250,default="hallo",unique=True) 
    
    #for uploading posts w/ txt file
    postUpload = models.FileField(verbose_name="Upload Post",null=True, blank=True, upload_to=unique_file_name, validators=[validate_file_size_type])
    
    #admin disabling posts
    disable_bopie = models.BooleanField(default=False)
    
    #Date expiry field
    date_expiry = models.DateField(verbose_name='Expiry Date', blank=True, default=datetime.now()+timedelta(2), null=True)

    
   
    def save(self, *args, **kwargs):
        super(Bopie, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title  
    
    def get_absolute_url(self): #after new post, redirects to detailed view of new post
        return reverse('bopie-detail', kwargs={'slug': self.slug})

#for user profile

#Renames profile pic upload to random filename
def pic_file_path(instance, filename):
    upload_to = 'profile_pics'
    ext = filename.split('.')[-1]

    filename = '{}.{}'.format(uuid4().hex, ext)
    
    return os.path.join(upload_to, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.ImageField(verbose_name="Profile Picture", default='default.png', upload_to=pic_file_path, validators=[validate_file_size_type])

    def __str__(self):
        return '{} Profile'.format(self.user.username)
    
    def save(self, *args, **kwargs): #overriding main save function
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.profilePic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profilePic.path)


