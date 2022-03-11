"""details URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from record import views

urlpatterns = [
    path('',views.logi,name="Login"),
    path('regi',views.regi,name="Registration"),
    path("regsave",views.regsave),
    path('log',views.log),
    path('adddata',views.adddata),
    path('add',views.add,name="AddData"),
    path('search',views.ser,name="search"),
    path('serch',views.serch),
    path('show',views.show,name="show"),
    path('dele',views.dele,name="Delete"),
    path('delete',views.deleti,name="Delete"),
    path("logo",views.logo),
    path('fp',views.fp),
    path('adserch',views.adserch),
    path('pwu',views.pwu),
    path('ditem',views.ditem),
    path('up',views.up),
]
