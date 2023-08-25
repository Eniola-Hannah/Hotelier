from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from Hotelier.userApp.views import SignUpView
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name = 'index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('booking/', TemplateView.as_view(template_name='booking.html'), name='booking'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('room/', TemplateView.as_view(template_name='room.html'), name='room'),
    path('service/', TemplateView.as_view(template_name='service.html'), name='service'),
    path('team/', TemplateView.as_view(template_name='team.html'), name='team'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name="signup"),
    re_path(r'^userApp/', include('Hotelier.userApp.urls')),
    re_path(r'^servicesApp/',include("Hotelier.servicesApp.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)