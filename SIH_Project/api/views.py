from django.shortcuts import render
from rest_framework import generics

# Create your views here.
def main(request):
    return render(request, 'frontend/index.html')
