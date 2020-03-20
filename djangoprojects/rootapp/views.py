from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def root(request):
    return HttpResponse("The server has started")
    
