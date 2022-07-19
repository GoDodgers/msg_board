import imp
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.


def login_form(req):
    
    return render(req, 'base/login_form.html', {})

def home(req):
    query = req.GET.get('q')

    if query is None:
        query = ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=query) |
        Q(name__icontains=query) |
        Q(description__icontains=query) 
    )

    topics = Topic.objects.all()
    # rooms = Room.objects.get()
    # rooms = Room.objects.filter()
    # rooms = Room.objects.exclude()

    room_count = rooms.count()

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count
    }
    return render(req, 'base/home.html', context)

def room(req, pk):
    return render(req, 'base/room.html', {
        'current_room': Room.objects.get(id=pk)
    })

def create_room(req):
    if req.method == 'POST':
        context = {'form': RoomForm(req.POST)}

        if context['form'].is_valid():
            context['form'].save()
            return redirect('home')
    else:
        context = {'form': RoomForm()}

    return render(req, 'base/room_form.html', context)

def update_room(req, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if req.method == "POST":
        form = RoomForm(req.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(req, 'base/room_form.html', context)

def delete_room(req, pk):
    room = Room.objects.get(id=pk)

    if req.method == "POST":
        room.delete()
        return redirect('home')

    return render(req, 'base/delete.html', {
        'current_room': room
    })
