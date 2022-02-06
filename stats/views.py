from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'stats.html')

def individual(requet):
    return HttpResponse('<h1> Individual Pages </h1>')