from django.db import models
from django.contrib.auth.models import

class Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.SmallIntegerField

    def __str__(self):
        return self.first_name + '' + self.last_name + '' + self.age


class Song(models.Model):
    title = models.CharField(max_length=250)
    date_released = models.DateTimeField
    likes = models.Count
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.CharField(max_length=1000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

# Create your models here.
