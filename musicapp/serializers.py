from .models import Artiste, Song, Lyric
from rest_framework import serializers

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields =['first_name', 'last_name', 'age']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields =['title', 'date_released', 'likes', 'artiste_id']

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content', 'song_id']

