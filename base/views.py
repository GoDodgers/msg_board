from django.shortcuts import render
from .models import Room

# Create your views here.

def home(req):
    rooms = Room.objects.all()
    # rooms = Room.objects.get()
    # rooms = Room.objects.filter()
    # rooms = Room.objects.exclude()
    context = { 'rooms': rooms }
    return render(req, 'base/home.html', context)

def room(req, pk):
    room = Room.objects.get(id=pk)
    context = { 'current_room': room } 
    return render(req, 'base/room.html', context)

def create_room(req):
    context = {}
    return render(req, 'base/room_form.html', context)