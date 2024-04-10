from django.contrib.auth.models import User
from django.db import models
from music_recommender.models import MusicTrack

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for user preferences
    favorite_genre = models.CharField(max_length=100, blank=True, null=True)
    favorite_artist = models.CharField(max_length=100, blank=True, null=True)
    saved_tracks = models.ManyToManyField(MusicTrack, related_name='saved_by_users', blank=True)
    
    # Define any custom methods or properties
    def __str__(self):
        return self.user.username

    # Customize the admin interface
    class Meta:
        verbose_name_plural = "User Profiles"
