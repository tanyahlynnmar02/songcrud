from django.db.migrations import serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer

class ArtistListApiView():
    def get(self, artiste_list,request):
        artists = Artiste.object.all()
        serializers = ArtisteSerializer(artists, many=False)
        return Response(serializer.data)

    def post(self, artiste_list, request):

        serializer = ArtisteSerializer(data=object)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_UPDATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,artiste_list, request):

        serializer = ArtisteSerializer(data=object)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_DELETED)



class SongListApiView():

    def get(self, song_list, request):

        songs = Song.object.all()
        serializers = SongSerializer(songs, many=False)
        return Response(serializer.data)

    def post(self, song_list, request):

            serializer = SongSerializer(data=object)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_UPDATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, song_list, request):

        serializer = SongSerializer(data=object)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_DELETED)

    @classmethod
    def as_view(cls):
        pass
