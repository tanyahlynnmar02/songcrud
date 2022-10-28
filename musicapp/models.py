from django.db import models


class Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.SmallIntegerField


class Song(models.Model):
    title = models.CharField(max_length=250)
    date_released = models.DateTimeField
    likes = models.Count
    artiste_id = models.ForeignKey(Artiste, on_delete=models.Cascade)


class Lyric(models.Model):
    content = models.charfield(max_length=1000)
    song_id = models.ForeignKey(Song, on_delete=models.Cascade)

# Create your models here.
