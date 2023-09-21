from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from .forms import Rooms_form
from .models import Room
from django.urls import reverse
from django.contrib import messages


# Create your views here.
@login_required
def addRoom(request):
    if request.method == 'POST':
        room_form = Rooms_form(request.POST, request.FILES)
        if room_form.is_valid():
            room_form.save()
            messages.success(request, ('Room was successfully Created!'))
            return displayRooms(request, "service_admin")
        else:
            messages.error(request, ('Room was not created successfully!'))
            return render(request=request, template_name='roomsApp/add_room.html', context={"roomForm": room_form})

    else:
        room_form = Rooms_form()
        return render(request=request, template_name='roomsApp/add_room.html', context={"roomForm": room_form})
    
@login_required
def displayRooms(request, display):
    rooms = Room.objects.all()
    if display == "service_nologin":
        return render(request=request, template_name='roomsApp/rooms.html', context={"rooms": rooms})
    else:
        return render(request=request, template_name='roomsApp/display_rooms.html', context={"rooms": rooms})
