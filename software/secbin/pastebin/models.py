from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Bopie(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #creating foreign key relationship with user and bopies

    def __str__(self):
        return self.title