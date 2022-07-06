from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'python is awesome!'},
    {'id': 2, 'name': 'javascript is awesomeer!'},
    {'id': 3, 'name': 'coding templates'},
]

# Create your views here.

def home(req):
    return render(req, 'home.html')

def room(req):
    context = {'rooms': rooms}
    return render(req, 'room.html', context)