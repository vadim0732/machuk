
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import main
from .views import library

urlpatterns = [
    path('main', main, name='main'),
    path('library', library, name='library')
]
