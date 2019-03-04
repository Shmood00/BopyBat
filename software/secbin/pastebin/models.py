from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.
class Bopie(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #creating foreign key relationship with user and bopies

    def __str__(self):
        return self.title

    def get_absolute_url(self): #after new post, redirects to detailed view of new post
        return reverse('bopie-detail', kwargs={'pk': self.pk})



#for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return '{} Profile'.format(self.user.username)
    
    def save(self, *args, **kwargs): #overriding main save function
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.profilePic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profilePic.path)


