from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    #Just a drop down section
    
    countries = [
        #value & label, label will show to the user while value will go into database
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("United Kingdom", "UK"),
        ("USA", "USA"),
    ]

    states = [
        ("Oyo", "Oyo"),
        ("Lagos", "Lagos"),
        ("Osun", "Osun"),
        ("Abuja", "Abuja"),
        ("Kwara", "Kwara"),
        ("Ogun", "Ogun"),
    ]

    position = [
        ("CEO", "CEO"),
        ("General Manager", "General Manager"),
        ("Human Resourses Manager", "Human Resourses Manager"),
        ("Sales Manager", "Sales Manager"),
        ("Front-Desk Receptionist", "Front-Desk Receptionist"),
        ("House Keeper", "House Keeper"),
        ("Concierges", "Concierges"),
        ("Bartender", "Bartender"),
        ("Server", "Server"),
        ("Chef", "Chef"),
        ("Sous Chef", "Sous Chef"),
        ("Security", "Security"),
        ("Maintenace Technician", "Maintenace Technician"),
        
    ]

    dept = [
        ("Front Desk", "Front Desk"),
        ("House Keeping", "House Keeping"),
        ("Customer Care", "Customer Care"),
        ("Food & Beverages", "Food & Beverages"),
        ("Sales & Marketing", "Sales & Marketing"),
        ("Human Resources", "Human Resources"),
        ("Maintenance", "Maintenance"),
        ("Security", "Security"),
    ]
    
    ma_status = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
        ("Complicated", "Complicated"),
    ]


    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(unique=False, max_length=20, null=True)
    address = models.CharField(max_length=100, null=True, unique=False)
    phone = models.CharField(max_length=11, null=True, unique=True)
    email = models.EmailField(max_length=50, null=True, unique=True, default="you@gmail.com")
    date_of_birth = models.DateField(unique=False, max_length=11, null=True)
    gender = models.CharField(max_length=11, unique=False, null=True)
    nationality = models.CharField(choices=countries, max_length=50, unique=False, null=True)
    state = models.CharField(choices=states, max_length=20, unique=False, null=True)
    means_of_identity = models.ImageField(upload_to="identityImage/", unique=False, null=True)
    particulars = models.FileField(upload_to="particularsImage/", unique=False, null=True)
    profile_passport = models.ImageField(upload_to="profileImage/",  unique=False, null=True)
    position = models.CharField(choices=position, max_length=25, unique=False, null=True)
    department = models.CharField(choices=dept, max_length=25, unique=False, null=True)
    marital_status = models.CharField(choices=ma_status, max_length=20, unique=False, null=True)
    next_of_kin = models.CharField(unique=False, max_length=20, null=True)
    staff = models.BooleanField(default=False, unique=False)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()