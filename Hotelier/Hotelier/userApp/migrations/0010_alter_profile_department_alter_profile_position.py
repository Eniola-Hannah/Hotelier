# Generated by Django 4.2.4 on 2023-09-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0009_alter_profile_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="department",
            field=models.CharField(
                choices=[
                    ("Executive/management ", "Executive/management "),
                    ("Human Resources", "Human Resources"),
                    ("Rooms & Apartment", "Rooms & Apartment"),
                    ("House Keeping", "House Keeping"),
                    ("Food & Beverages", "Food & Beverages"),
                    ("Sales & Marketing", "Sales & Marketing"),
                    ("Restaurant & Dining", "Restaurant & Dining"),
                    ("Spa & Fitness", "Spa & Fitness"),
                    ("Gym & Yoga", "Gym & Yoga"),
                    ("Event & Party", "Event & Party"),
                    ("Maintenance", "Maintenance"),
                    ("Security", "Security"),
                ],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="position",
            field=models.CharField(
                choices=[
                    ("CEO", "CEO"),
                    ("General Manager", "General Manager"),
                    ("Manager", "Manager"),
                    ("Sales Manager", "Sales Manager"),
                    ("Front-Desk Receptionist", "Front-Desk Receptionist"),
                    ("House Keeper", "House Keeper"),
                    ("Concierges", "Concierges"),
                    ("Bartender", "Bartender"),
                    ("Server", "Server"),
                    ("Chef", "Chef"),
                    ("Sous Chef", "Sous Chef"),
                    ("Security", "Security"),
                    ("Maintenance Technician", "Maintenance Technician"),
                ],
                max_length=25,
                null=True,
            ),
        ),
    ]