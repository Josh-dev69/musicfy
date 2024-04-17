from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length=100, null=True)
    favorite_artist = models.CharField(max_length=100, null=True)
    
    # Define any custom methods or properties
    def __str__(self):
        return self.user.username
