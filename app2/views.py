from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def virat(request):
    return HttpResponse('<h1><marquee>Virat is the best batsman in the world</marquee></h1>')
