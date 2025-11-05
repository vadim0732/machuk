
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import main
from .views import library

urlpatterns = [
    path('main.html', main),
    path('library.html', library)
]
