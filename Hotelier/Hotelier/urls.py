from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name = 'index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('booking/', TemplateView.as_view(template_name='booking.html'), name='booking'),

]
