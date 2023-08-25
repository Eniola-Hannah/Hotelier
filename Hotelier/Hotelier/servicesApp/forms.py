from django import forms
from django.contrib.auth.models import User
from Hotelier.userApp.models import Profile

class Services_form(forms.ModelForm):
    
    list_HOD = []
    for hods in Profile.objects.all().filter(position="HOD"):
        list_HOD.append((hods.user_id, hods.user.first_name + " " + hods.user.last_name + " (" + hods.department +")"))
    
        service_logo = forms.FileField(required=False)
    hod = forms.ChoiceField(choices=list_HOD, required=True)
    description = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Service
        fields = [
            'service_name',
            'hod',
            'service_logo',
            'price',
            'description',
        ]
        