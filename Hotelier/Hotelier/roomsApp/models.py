from django.db import models
from django.contrib.auth.models import User
from Hotelier.userApp.models import Profile
from django.utils import timezone

# Create your models here.
class Status:

        user_status = [
            ("Check in", "Check in"),
            ("Check out", "Check out"),
        ]


class Room(models.Model):     
        room_id = models.AutoField(primary_key=True)
        room_name = models.CharField(max_length=70, null=False, unique=True)
        date_created = models.DateTimeField(auto_now_add=True)
        room_image = models.ImageField(upload_to="room_image/", blank=True, null=True, unique=False)
        price = models.BigIntegerField(unique=False)
        description = models.CharField(max_length=300, blank=True, null=True)
