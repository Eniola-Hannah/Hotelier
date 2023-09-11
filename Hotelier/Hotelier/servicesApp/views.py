from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from .forms import Services_form, BooksService_form
from .models import Service, BookingService
from django.urls import reverse
from django.contrib import messages
from django.db import transaction
from django.core.mail import send_mail
from datetime import time


# Create your views here.
@login_required
def createService(request):
    if request.method == 'POST':
        service_form = Services_form(request.POST, request.FILES)
        if service_form.is_valid():
            service_form.save()
            messages.success(request, ('Service was successfully Created!'))
            return displayServices(request, "service_admin")
        else:
            messages.error(request, ('Service was not created successfully!'))
            return render(request=request, template_name='servicesApp/create_service.html', context={"serviceForm": service_form})

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


@transaction.atomic
@login_required
def serviceDetails(request, serv_id):
    if request.method == 'POST':
        service_form = BooksService_form(request.POST)
        service = Service.objects.get(service_id = serv_id)
        print(service)
        if service_form.is_valid():
            
            reserved_time = service_form.cleaned_data.get('reserved_time')
            start_time = time(7, 0)  # 7:00 AM
            end_time = time(22, 0)   # 10:00 PM

            if start_time <= reserved_time <= end_time:

                form = service_form.save(commit=False)
                form.manager_id = service.manager_id
                form.user_id = request.user.id
                form.service_id = service.service_id
                form.price = service.price
                form.service_name = service.service_name
                form.save()

                send_mail(
                    'A BOOKING HAS BEEN MADE BY A PATIENT', # Subject of the mail
                    f'Dear Mr. {service.manager.first_name}, a Guest has booked for a service. Please choose the reservation status of the booking. Thanks', # Body
                    'hotelierhaven@gmail.com', # from email(sender),
                    [service.manager.email], # To email reciever
                    fail_silently=False #Handle any error
                )
                
                
                messages.success(request, ('RESERVATION MADE SUCCESSFULLY!'))
                return HttpResponsePermanentRedirect(reverse('service_details', args=(serv_id,)))
            
            else: 
                messages.error(request, ('RESERVATION CAN ONLY BE BETWEEN THE HOUR OF 7:00 AM AND 10:00 PM'))
                return HttpResponsePermanentRedirect(reverse('service_details', args=(serv_id,)))

        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('service_details', args=(serv_id,)))
        
    else:
        service_detail = Service.objects.filter(service_id=serv_id)
        service_form = BooksService_form()
        return render(request=request, template_name='servicesApp/service_details.html', context={"service_details":service_detail,"service_form": service_form})


@login_required
def myBooking(request, user):
    booking = BookingService.objects.filter(user_id=user).order_by("date_created").reverse()
    return render(request=request, template_name='servicesApp/my_booking.html', context={"booking_service":booking})



@login_required
def bookingPayment(request, book_id):
    pass