from django.shortcuts import render, HttpResponse
from .models import *

def main(request):

    return render(request, 'main.html')