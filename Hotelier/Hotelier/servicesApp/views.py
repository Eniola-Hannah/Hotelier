from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from .forms import Services_form
from .models import Service
from django.urls import reverse


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
