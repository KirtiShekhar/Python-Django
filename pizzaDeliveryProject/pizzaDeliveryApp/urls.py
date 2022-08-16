"""pizzaDeliveryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('simpleBlogWebsiteClone/', include('simpleBlogWebsiteClone.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import welcomepageview,adminloginview,authenticateadmin,adminhomepageview,adminlogoutview,addPizzas,\
    deletePizzas,customerhomepageview,customersignup,customersignin,authenticatecustomer,customerwelcomepageview,\
    customerlogout,placepizzasorder,customerpizzasorder,adminpizzasorder,acceptpizzasorder,declinedpizzasorder

urlpatterns = [
    path('welcome/', welcomepageview,name = "welcomepageview"),
    path('admin/', adminloginview,name = "adminloginview"),
    path('authenticateadmin/',authenticateadmin,name = "authenticateadmin"),
    path('admin/home/', adminhomepageview,name = "adminhomepageview"),
    path('adminlogout/',adminlogoutview,name = "adminlogoutview"),
    path('addPizzas/',addPizzas,name = "addPizzas"),
    path('deletePizzas/<int:pizzaspk>/',deletePizzas,name = "deletePizzas"),
    path('customer/home/',customerhomepageview,name = "customerhomepageview"),
    path('customersignup/',customersignup,name = "customersignup"),
    path('customersignin/',customersignin,name = "customersignin"),
    path('authenticatecustomer/',authenticatecustomer,name = "authenticatecustomer"),
    path('customer/welcome/',customerwelcomepageview,name = "customerwelcomepageview"),
    path('customerlogout/',customerlogout,name = "customerlogout"),
    path('placepizzasorder/',placepizzasorder,name = "placepizzasorder"),
    path('customerpizzasorder/',customerpizzasorder,name = "customerpizzasorder"),
    path('adminpizzasorder/',adminpizzasorder,name = "adminpizzasorder"),
    path('acceptpizzasorder/<int:pizzaorderpk>/',acceptpizzasorder,name = "acceptpizzasorder"),
    path('declinedpizzasorder/<int:pizzaorderpk>/',declinedpizzasorder,name = "declinedpizzasorder"),
]