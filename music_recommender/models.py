from django.db import models

# Create your models here.

class MusicTrack(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    # Define any custom methods or properties
    def __str__(self):
        return self.title + ' by ' + self.artist

    # Customize the admin interface
    class Meta:
        verbose_name_plural = "Music Tracks"
