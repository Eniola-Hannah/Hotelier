from django.db import models
from django.contrib.auth.models import User
from Hotelier.userApp.models import Profile
from django.utils import timezone

# Create your models here.

class GeneralPurpose:
        dept = [
            ("Rooms & Apartment", "Rooms & Apartment"),
            ("Food & Restaurant/Dining", "Food & Restaurant/dining"),
            ("Concierges", "Concierges"),
            ("Housekeeping", "Housekeeping"),
            ("Spa & Fitness", "Spa & Fitness"),
            ("Gym & Yoga", "Gym & Yoga"),
            ("Event & Party", "Event & Party"),
        ]

        user_status = [
            ("Active", "Active"),
            ("Check in", "Check in"),
            ("Check out", "Check out"),
            ("Retired", "Retired"),
            ("Resigned", "Resigned"),
            ("Fired", "Fired"),
        ]

    

class Service(models.Model): 
        genP = GeneralPurpose()
    
        service_id = models.AutoField(primary_key=True)
        manager = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
        service_name = models.CharField(choices=genP.dept, max_length=50, null=False, unique=True)
        date_created = models.DateTimeField(auto_now_add=True)
        service_logo = models.ImageField(upload_to="service_logo/", blank=True, null=True, unique=False)
        price = models.BigIntegerField(unique=False)
        description = models.CharField(max_length=300, blank=True, null=True)



class Room(models.Model):     
        room_id = models.AutoField(primary_key=True)
        room_name = models.CharField(max_length=70, null=False, unique=True)
        date_created = models.DateTimeField(auto_now_add=True)
        room_image = models.ImageField(upload_to="room_image/", blank=True, null=True, unique=False)
        price = models.BigIntegerField(unique=False)
        description = models.CharField(max_length=300, blank=True, null=True)
