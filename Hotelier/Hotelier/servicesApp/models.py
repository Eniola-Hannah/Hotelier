from django.db import models
from django.contrib.auth.models import User
from Hotelier.userApp.models import Profile
from django.utils import timezone

# Create your models here.

class GeneralPurpose:
        dept = [
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

        reserve_status = [
            ("Pending", "Pending"),
            ("Confirmed", "Confirmed"),
            ("Cancelled", "Cancelled"),
        ]

    

class Service(models.Model): 
        genP = GeneralPurpose()
    
        service_id = models.AutoField(primary_key=True)
        manager = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
        service_name = models.CharField(choices=genP.dept, max_length=50, null=False, unique=True)
        date_created = models.DateTimeField(auto_now_add=True)
        service_logo = models.ImageField(upload_to="service_logo/", blank=True, null=True, unique=False)
        service_image = models.ImageField(upload_to="service_image/", blank=True, null=True, unique=False)
        price = models.BigIntegerField(unique=False)
        description = models.CharField(max_length=300, blank=True, null=True)


class BookingService(models.Model):
        genP = GeneralPurpose()
        
        booking_id = models.AutoField(primary_key=True)
        user = models.ForeignKey(User, null=False, blank=False, unique=False, on_delete=models.CASCADE)
        service = models.ForeignKey(Service, null=False, blank=False, unique=False, on_delete=models.CASCADE)
        service_name = models.CharField(max_length=100, blank=True, null=True, unique=False)
        price = models.BigIntegerField(unique=False, blank=True, null=True)
        date_created = models.DateField(auto_now_add=True)
        reserved_date = models.DateField(null=True, blank=True, unique=False)
        reserved_time = models.TimeField(null=True, blank=True, unique=False)
        reservation_status = models.CharField(choices=genP.reserve_status, max_length=70, null=True, blank=True, unique=False)
        No_Of_Guest = models.BigIntegerField(unique=False, blank=True, null=True)
        special_request = models.CharField(max_length=300, blank=True, null=True)
        payment = models.BooleanField(default=False, blank=True, null=True, unique=False)
        manager = models.ForeignKey(User, related_name="manager", null=False, blank=False, unique=False, on_delete=models.CASCADE )