from django.shortcuts import render
from .models import name, audio
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def add_name(request):
    records = {
        "name" : "chinmay",
    }
    name.insert_one(records)
    return HttpResponse("Name Added")