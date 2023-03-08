from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse('MSD is best all rounder')

def rohith(request):
    return HttpResponse('<h1>He is the best player</h1>')