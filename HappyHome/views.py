from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import json
# import requests
from .models import Provider, User, Category, Classification, Review, Reply

# views
def home(request):
    if request.method == 'GET':
        message = "Hello World"
    else:
        message = "Hello World!"
    return render(request, 'home.html', {'message':message})
