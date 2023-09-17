from django import forms
from django.contrib.auth.models import User
from Hotelier.userApp.models import Profile
from .models import Room

class Rooms_form(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'room_name',
            'room_image',
            'price',
            'description',

        ]

        widgets = {
            'description': forms.Textarea(attrs={'cols':60, 'rows': 3}),
        }