
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
]
