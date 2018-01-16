from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json

# Create your views here.
def index(request):
    song_list = models.Song.objects.filter(song_name="alchemist")
    print(song_list)
    context = {
        'song_list' : song_list,
    }
    #return render(request, 'hap_music/index.html', context)
    return HttpResponse("Welcome to my music app")

@csrf_exempt
def ret_song_on_genre(request, genre):
    result = []
    print(genre)
    return HttpResponse(models.Song.objects.filter(genre=genre))
    genre_based_song_list = models.Song.objects.filter(genre=genre)
    template = loader.get_template('hap_music/genre.html')
    context = {
        'genre_based_song_list' : genre_based_song_list,
    }

    return HttpResponse(template.render(context, ))

@csrf_exempt
def ret_song_on_artist(request, artist):
    return(HttpResponse(models.Song.objects.filter(artist=artist)))

@csrf_exempt
def ret_song_on_album(request, album):
    result = []
    songs = models.Song.objects.filter(album_title=album)

    for song in songs:
        result.append(song.song_name)
    return HttpResponse(json.dumps(result))

@csrf_exempt
def add_song(request):
    song_data = json.loads(request.body)

    song = models.Song()
    song.song_name = song_data['Name']
    song.duration = song_data["Duration"]
    song.artist = song_data["Artist"]
    song.album_title = song_data["Album"]
    song.genre = song_data["Genre"]
    song.save()
    return HttpResponse("add_music")