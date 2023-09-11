from django.urls import re_path
from Hotelier.servicesApp import views as sw

urlpatterns = [
    re_path(r'^create_service/', sw.createService, name="create_service"),
    re_path(r'^display_service/(?P<display>\w+)/', sw.displayServices, name="display_service"),
    re_path(r'^edit_service/(?P<serv_id>\d+)/', sw.editServices, name="edit_service"),
    re_path(r'^service_details/(?P<serv_id>\d+)/', sw.serviceDetails, name="service_details"),
    re_path(r'^my_booking/(?P<user>\d+)/', sw.myBooking, name='my_booking'),
    re_path(r'^book_payment/(?P<book_id>\d+)/', sw.bookingPayment, name='book_payment'),
    re_path(r'^guest_booking/(?P<user>\d+)/', sw.guestBooking, name='guest_booking'),
    re_path(r'^view_booking_detail/(?P<book_id>\d+)/', sw.viewBookingDetail, name='view_booking_detail'),


]