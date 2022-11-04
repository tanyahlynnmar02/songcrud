from django.db import models


class Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.SmallIntegerField


class Song(models.Model):
    title = models.CharField(max_length=250)
    date_released = models.DateTimeField
    likes = models.Count
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.CharField(max_length=1000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

# Create your models here.
