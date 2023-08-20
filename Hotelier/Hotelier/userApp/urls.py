from django.urls import re_path
from Hotelier.userApp import views as vw


urlpatterns = [
    re_path(r'^my_account/(?P<_id>\d+)/', vw.my_account, name="my_account"),
]