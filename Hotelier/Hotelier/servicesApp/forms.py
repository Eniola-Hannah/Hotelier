from django import forms
from django.contrib.auth.models import User
from Hotelier.userApp.models import Profile
from .models import Service, BookingService


class Services_form(forms.ModelForm):
    
    list_MANAGER = []
    for managers in Profile.objects.all().filter(position="Manager"):
        list_MANAGER.append((managers.user_id, managers.user.first_name + " " + managers.user.last_name + " (" + managers.department +")"))
    
        service_logo = forms.FileField(required=False)
    manager = forms.ChoiceField(choices=list_MANAGER, required=True)
    description = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Service
        fields = [
            'service_name',
            'manager',
            'service_logo',
            'service_image',
            'price',
            'description',
        ]


class BooksService_form(forms.ModelForm):
    class Meta:
        model = BookingService
        fields = [
            'reserved_date',
            'reserved_time',
            'No_Of_Guest',
            'special_request',

        ]

        widgets = {
            'reserved_date': forms.DateInput(attrs={'type': 'date'}),
            'reserved_time': forms.TimeInput(attrs={'type': 'time'}),
            'special_request': forms.Textarea(attrs={'cols':60, 'rows': 3}),
        }
