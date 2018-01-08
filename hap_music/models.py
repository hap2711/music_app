from django.db import models


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=5)

    def __str__(self):
        return self.song_name