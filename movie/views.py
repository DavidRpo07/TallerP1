from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to the Home Page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'David Restrepo Aristizábal'})

def about(request):
    #return HttpResponse('<h1>Welcome to the About Page</h1>')
    return render(request, 'about.html')