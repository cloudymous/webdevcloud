from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> Index </h1>")

def about(request):
    return render(request, 'about.html')

def homepage(request):
    return render(request, 'index.html')