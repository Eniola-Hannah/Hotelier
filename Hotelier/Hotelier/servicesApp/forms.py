from django import forms
from django.contrib.auth.models import User
from Hotelier.userApp.models import Profile
from .models import Service, Room


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
            'price',
            'description',
        ]


class Rooms_form(forms.ModelForm):
    room_image = forms.FileField(required=False)
    description = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Room
        fields = [
            'room_name',
            'room_image',
            'price',
            'description',
        ]
        