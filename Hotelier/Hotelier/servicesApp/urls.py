from django.urls import re_path
from Hotelier.servicesApp import views as sw

urlpatterns = [
    re_path(r'^create_service/', sw.createService, name="create_service"),
    re_path(r'^display_service/(?P<display>\w+)/', sw.displayServices, name="display_service"),
    re_path(r'^edit_service/(?P<serv_id>\d+)/', sw.editServices, name="edit_service"),
    re_path(r'^create_room/', sw.createRoom, name="create_room"),
    re_path(r'^display_room/(?P<display>\w+)/', sw.displayRooms, name='display_room'),
    re_path(r'^edit_room/(?P<room_id>\d+)/', sw.editRooms, name="edit_room"),
    # re_path(r'^service_details/(?P<serv_id>\d+)/', sw.serviceDetails, name='service_details'),
    # re_path(r'^room_details/(?P<serv_id>\d+)/', sw.roomDetails, name='room_details'),

]