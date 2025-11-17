
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import main
from .views import library
from .views import artist_detail
from .views import artist_search

urlpatterns = [
    path('main', main, name='main'),
    path('library', library, name='library'),
    path('artist/<str:artist_name>/', artist_detail, name='artist_detail'),
    path('search/', artist_search, name='artist_search'),
]
