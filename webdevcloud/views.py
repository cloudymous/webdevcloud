from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Index </h1>")

def about(request):
    return HttpResponse("<h1> Ini adalah About </h1>")