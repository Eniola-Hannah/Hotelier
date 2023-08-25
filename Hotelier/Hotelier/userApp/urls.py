from django.urls import re_path
from Hotelier.userApp import views as vw


urlpatterns = [
    re_path(r'^my_account/(?P<_id>\d+)/', vw.my_account, name="my_account"),
    re_path(r'^editAdmin_account/(?P<_id>\d+)/', vw.editAdmin_account, name="editAdmin_account"),
    re_path(r'^editUser_account/(?P<_id>\d+)/', vw.editUser_account, name="editUser_account"),
    re_path(r'^deactivate_account/(?P<_id>\d+)/', vw.deactivate_account, name='deactivate_account'),
    re_path(r'^all_staff/(?P<user>\w+)/', vw.allUser, name="all_staff"),
    re_path(r'^all_guest/(?P<user>\w+)/', vw.allUser, name="all_guest"),
]