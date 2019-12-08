"""Aayursaukhyam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, re_path

from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    re_path(r'^hospital/$', views.hospital_list, name='hospital_list'),
    re_path(r'^hospital/create$', views.hospital_create, name='hospital_create'),
    re_path(r'^hospital/(?P<id>\d+)/update$', views.hospital_update, name='hospital_update'),
    re_path(r'^hospital/(?P<id>\d+)/delete$', views.hospital_delete, name='hospital_delete'),

    re_path(r'^building/$', views.building_list, name='building_list'),
    re_path(r'^building/create$', views.building_create, name='building_create'),
    re_path(r'^building/(?P<id>\d+)/update$', views.building_update, name='building_update'),
    re_path(r'^building/(?P<id>\d+)/delete$', views.building_delete, name='building_delete'),

    re_path(r'^wardorroomtype/$', views.wardorroomtype_list, name='wardorroomtype_list'),
    re_path(r'^wardorroomtype/create$', views.wardorroomtype_create, name='wardorroomtype_create'),
    re_path(r'^wardorroomtype/(?P<id>\d+)/update$', views.wardorroomtype_update, name='wardorroomtype_update'),
    re_path(r'^wardorroomtype/(?P<id>\d+)/delete$', views.wardorroomtype_delete, name='wardorroomtype_delete'),


]
