"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portafolio_views
from django.conf import settings


urlpatterns = [
    path('',core_views.home,name ="Home"),
    path('about',core_views.about,name ="About"),
    path('contact',core_views.contact,name ="contact"),
    path('portafolio',portafolio_views.portafolio,name ="portafolio"),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)