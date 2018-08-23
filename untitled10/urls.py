"""untitled10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
#from .views import driverlist
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # define the url getdata that we have written inside form
    #url(r'^getdata/', views.index, name='index'),
    url(r'^cars/', views.cars, name='cars'),
    url(r'^carlist/', views.carlist, name='carlist'),
    url(r'^drivers/', views.drivers, name='drivers'),
    url(r'^postDrivers/', views.post_drivers, name='post_drivers'),
    url(r'^postReservation/', views.post_reservation, name='post_reservation'),
    url(r'^driverlist/', views.driverlist, name='driverlist'),
    # defining the view for root URL
    url(r'^$', views.index, name='index'),
    #path(r'^drivers/driverlist/', views.driverlist, name='driverlist'),
]
