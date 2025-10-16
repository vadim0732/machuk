from django.shortcuts import render, HttpResponse
from .models import *

def index(request):

    artist = Artist.name

    return render(request, 'index.html', {'artist': artist})