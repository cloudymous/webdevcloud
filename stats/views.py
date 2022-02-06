from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ctx = {
        'title' : 'Statistic',
        'body' : 'This is Statistic pages'
    }
    return render(request, 'stats.html', ctx)

def individual(request):
    ctx = {
        'title' : 'Individual',
        'body' : 'This is individual pages'
    }
    return render(request, 'stats.html', ctx)