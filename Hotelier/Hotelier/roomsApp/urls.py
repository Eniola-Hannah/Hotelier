from django.urls import re_path
from Hotelier.roomsApp import views as rv

urlpatterns = [
    re_path(r'^add_room/', rv.addRoom, name="add_room"),
    re_path(r'^display_rooms/(?P<display>\w+)/', rv.displayRooms, name="display_rooms"),

]