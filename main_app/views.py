from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render('<h1>About</h1>')

def dogs_index(request):
    return render('<h1>Dogs</h1>')