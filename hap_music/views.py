from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my music app")

def ret_song_on_genre(request, genre):
    if genre == 'rock':
        return HttpResponse("Rock on")
    elif genre == 'punk':
        return HttpResponse("Punk on")
    else:
        return HttpResponse("Test")

def add_song(request):
    print(request.data)