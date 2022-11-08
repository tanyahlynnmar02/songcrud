from json import JSONEncoder
from django.http import JsonResponse
from rest_framework import status
from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer
from  rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET' ,'POST'])
def artist_list(request):

    if request.method == 'GET':
        artists = Artiste.objects.all()
        serializers = ArtisteSerializer(artists, many=True)
        return JsonResponse({'artists': serializers.data}, safe=False)

    if request.method == 'POST':
        serializers = ArtisteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

def song_list(request):

    if request.method == 'GET':
        songs = Song.title.all()
        serializers = SongSerializer(songs, many=True)
        return JsonResponse({'songs' : serializers.data}, safe=False)

    if request.method == 'POST':
        serializers = SongSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)


