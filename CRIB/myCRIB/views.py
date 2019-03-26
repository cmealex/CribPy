from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'index.html')

def display_rooms(request):
    items = Rooms.objects.all()
    context = {
        'items': items,
        'header': 'All Rooms'
    }

    return render(request, 'index.html', context)

def add_item(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_rooms')
    else:
        form = RoomForm()
        return render(request, 'add_new.html', {'form': form})

def edit_item(request, pk):
    item = get_object_or_404(Rooms, pk=pk)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_rooms')
    else:
        form = RoomForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})

def delete_item(request, pk):
    Rooms.objects.filter(id=pk).delete()

    items = Rooms.objects.all()
    context = {
        'items': items,
    }

    return render(request, 'index.html', context)