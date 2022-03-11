"""example URL Configuration

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
from pro import views

urlpatterns = [
    path('',views.login),
    path('regi',views.regi),
    path('fp',views.fp),
    path('dele',views.dele),
    path('add',views.add),
    path('search',views.search),
    path('show',views.show),
    path('logo',views.logo),
    path('adding',views.adding),
    path('dele',views.dele,name="Delete"),
    path('serh',views.serh),
    path('newdata',views.newdata),
    path('add',views.add,name="AddData"),
    path('logg',views.logg),
    path('adserch',views.adserch),
    path('paswd',views.paswd),
    path('deltem',views.deltem),
]
