from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    users = User.username

    return render(request, 'index.html')