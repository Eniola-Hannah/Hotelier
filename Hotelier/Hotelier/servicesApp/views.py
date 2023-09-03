from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from .forms import Services_form, Rooms_form
from .models import Service, Room
from django.urls import reverse
from django.contrib import messages


# Create your views here.
@login_required
def createService(request):
    if request.method == 'POST':
        service_form = Services_form(request.POST, request.FILES)
        if service_form.is_valid():
            service_form.save()
        return displayServices(request, "service_admin")
    else:
        service_form = Services_form()
        return render(request=request, template_name='servicesApp/create_service.html', context={"serviceForm": service_form})
    

def indexService(request):
    services = Service.objects.all()
    services = services[0:6]
    return render(request=request, template_name='index.html', context={"services": services})


@login_required
def displayServices(request, display):
    services = Service.objects.all()
    if display == "service_nologin":
        return render(request=request, template_name='servicesApp/services.html', context={"services": services})
    else:
        return render(request=request, template_name='servicesApp/display_service.html', context={"services": services})
    

@login_required
def editServices(request, serv_id):
    form = get_object_or_404(Service, service_id=serv_id)
    if request.method == "POST":
        service_form = Services_form(request.POST or None, request.FILES or None, instance=form)
        if service_form.is_valid():
            service_form.save()
            messages.success(request, ('Service was successfully updated!'))
            return HttpResponsePermanentRedirect(reverse('display_service', args=("service_admin",)))
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('edit_service', args=(serv_id,)))
    else:
        service_form = Services_form(instance=form)
        return render(request, 'servicesApp/edit_service_form.html', {
        'service_form': service_form,    
    })


@login_required
def serviceDetails(request, serv_id):
    service_detail = Service.objects.filter(service_id=serv_id)
    # service_form = BooksService_form()
    # return render(request=request, template_name='servicesApp/service_details.html', context={"service_details":service_detail,"serviceForm": service_form})
    return render(request=request, template_name='servicesApp/service_details.html')


@login_required
def createRoom(request):
    if request.method == 'POST':
        room_form = Rooms_form(request.POST, request.FILES)
        if room_form.is_valid():
            room_form.save()
        return displayRooms(request, "adminRoomPage")
    else:
        room_form = Rooms_form()
        return render(request=request, template_name='servicesApp/create_room.html', context={"roomForm": room_form})
    

@login_required
def displayRooms(request, display):
    rooms = Room.objects.all()
    if display == "indexRoomPage":
        return render(request=request, template_name='servicesApp/rooms.html', context={"rooms": rooms})
    else:
        return render(request=request, template_name='servicesApp/display_room.html', context={"rooms": rooms})
    

@login_required
def editRooms(request, room_id):
    form = get_object_or_404(Room, room_id=room_id)
    if request.method == "POST":
        room_form = Rooms_form(request.POST or None, request.FILES or None, instance=form)
        if room_form.is_valid():
            room_form.save()
            messages.success(request, ('Room has been successfully updated!'))
            return HttpResponsePermanentRedirect(reverse('display_room', args=("adminRoomPage",)))
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('edit_room', args=(room_id,)))
    else:
        room_form = Rooms_form(instance=form)
        return render(request, 'servicesApp/edit_room_form.html', {
        'room_form': room_form,    
    })