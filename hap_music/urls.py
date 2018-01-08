from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Handle path '/'
    url(r'^$', views.index, name='index'),
    url(r'^add-song$', views.add_song, name='add_song'),
    url(r'^genre/(?P<genre>[a-z]+[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*)$', views.ret_song_on_genre, name='ret_music_on_genre'),
    url(r'^artist/(?P<artist>[a-z]+[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*)$', views.ret_song_on_artist, name='ret_music_on_artist'),
    url(r'^album/(?P<album>[a-z]+[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*[\s]*[a-z]*)$', views.ret_song_on_album, name='ret_music_on_album')
]