from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    # if you want to use django signup form, then put pass
    # you might decide to override the django signup form with these below code
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=50, help_text='Enter a valid email address')
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class AdminProfile_form(forms.ModelForm):
    gend = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("LGBTQ+", "LGBTQ+"),
    ]
    

    user_status = [
        ("Active", "Active"),
        ("Check in", "Check in"),
        ("Check out", "Check out"),
        ("Retired", "Retired"),
        ("Resigned", "Resigned"),
        ("Fired", "Fired"),
    ]

    means_of_identity = forms.ImageField(required=False, label='means of identity')
    particulars = forms.FileField(required=False, label='particulars')
    profile_passport = forms.ImageField(required=False, label='profile passport')
    status = forms.ChoiceField(choices=user_status, required=True)
    gender = forms.ChoiceField(choices=gend, required=True, widget=forms.RadioSelect)
    
    class Meta: 
        model = Profile
        fields = [
                    "address",
                    "phone",
                    "occupation",
                    "date_of_birth",
                    "gender",
                    "nationality",
                    "state",
                    "profile_passport",
                    "means_of_identity",
                    "particulars",
                    "position",
                    "department",
                    "marital_status",
                    "next_of_kin",
                    "status",
                    "staff",
                ]
        
        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type': 'date'}),
        }

class UserProfile_form(forms.ModelForm):
    gend = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("LGBTQ+", "LGBTQ+"),
    ]
    

    means_of_identity = forms.ImageField(required=False, label='means of identity')
    profile_passport = forms.ImageField(required=False, label='profile passport')
    gender = forms.ChoiceField(choices=gend, required=True, widget=forms.RadioSelect)
    
    class Meta: 
        model = Profile
        fields = [
                    "address",
                    "phone",
                    "occupation",
                    "date_of_birth",
                    "gender",
                    "nationality",
                    "state",
                    "profile_passport",
                    "means_of_identity",
                    "marital_status",
                    "next_of_kin",
                ]
        
        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type': 'date'}),
        }