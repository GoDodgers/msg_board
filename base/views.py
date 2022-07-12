from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

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