from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import SignUpForm
from .models import Profile
from django.contrib.auth.decorators import login_required



# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# every function that is coming from urls must take 'request' as the first parameter
@login_required
def my_account(request, _id):
    profile = Profile.objects.all().filter(user_id=_id) 
    print(profile)
    # every render must return, add return and request as a parameter
    return render(request=request, template_name="userApp/my_account.html", context={"my_profile":profile})  
