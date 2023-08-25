from django.db import models
from django.contrib.auth.models import User
from Hotelier.userApp.models import Profile
from django.utils import timezone

# Create your models here.

class GeneralPurpose:
        dept = [
            ("Executive/management", "Executive/management"),
            ("Front Desk", "Front Desk"),
            ("House Keeping", "House Keeping"),
            ("Customer Care", "Customer Care"),
            ("Food & Beverages", "Food & Beverages"),
            ("Sales & Marketing", "Sales & Marketing"),
            ("Human Resources", "Human Resources"),
            ("Maintenance", "Maintenance"),
            ("Security", "Security"),
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
        hod = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
        service_name = models.CharField(choices=genP.dept, max_length=50, null=False, unique=True)
        date_created = models.DateTimeField(auto_now_add=True)
        service_logo = models.ImageField(upload_to="service_logo/", blank=True, null=True, unique=False)
        price = models.BigIntegerField(unique=False)
        description = models.CharField(max_length=300, blank=True, null=True)
