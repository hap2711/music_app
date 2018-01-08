from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Handle path '/'
    url(r'^$', views.index, name='index'),
    url(r'^add-song$', views.add_song, name='add_song'),
    url(r'^(?P<genre>[a-z]+)$', views.ret_song_on_genre, name='ret_music')
]