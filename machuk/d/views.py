from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Artist, Track, Album
from django.db.models import Q


def main(request):

    sort_order = request.GET.get('sort', 'desc')
    
    popular_tracks = Track.objects.all()
    
    if sort_order == 'asc':
        popular_tracks = popular_tracks.order_by('listens_count')
    else:
        popular_tracks = popular_tracks.order_by('-listens_count')
    
    popular_tracks = popular_tracks[:8]
    new_albums = Album.objects.order_by('-release_date')[:6]
    featured_artists = Artist.objects.filter(verified=True)[:6]

    context = {
        'popular_tracks': popular_tracks,
        'new_albums': new_albums,
        'featured_artists': featured_artists,
        'current_sort': sort_order,
    }
    return render(request, 'main.html', context)

def library(request):
    favorite_tracks = Track.objects.all()[:6]
    subscribed_artists = Artist.objects.all()[:6]

    context = {
        'favorite_tracks': favorite_tracks,
        'subscribed_artists': subscribed_artists,
    }
    return render(request, 'library.html', context)

def artist_detail(request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)
    tracks = Track.objects.filter(main_artist=artist).order_by('-listens_count')
    albums = Album.objects.filter(artist=artist).order_by('-release_date')
    
    context = {
        'artist': artist,
        'tracks': tracks,
        'albums': albums,
    }
    return render(request, 'artist.html', context)

def artist_search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        artist = Artist.objects.filter(name__iexact=query).first()
        
        if artist:
            return redirect('artist_detail', artist_name=artist.name)
        else:
            return render(request, 'artist_not_found.html', {'query': query})
    
    return redirect('main')