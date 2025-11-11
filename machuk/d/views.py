from django.shortcuts import render, HttpResponse
from .models import Artist, Track, Album

def main(request):
    popular_tracks = Track.objects.order_by('-listens_count')[:8]
    new_albums = Album.objects.order_by('-release_date')[:6]
    featured_artists = Artist.objects.filter(verified=True)[:6]

    context = {
        'popular_tracks': popular_tracks,
        'new_albums': new_albums,
        'featured_artists': featured_artists,
    }
    return render(request, 'main.html', context)

def library(request):
    favorite_tracks = Track.objects.all()[:15]
    subscribed_artists = Artist.objects.all()[:12]

    context = {
        'favorite_tracks': favorite_tracks,
        'subscribed_artists': subscribed_artists,
    }
    return render(request, 'library.html', context)