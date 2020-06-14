"""reynaldev_services path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path(r'^$', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.conf.paths import path, include
    2. Add a path to pathpatterns:  path(r'^blog/', include('blog.paths'))
"""
from django.urls import path

from .views import *

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('servicios/', Servicios.as_view(), name='servicios'),
    path('cv/', CV.as_view(), name='cv'),
    path('donacion/', Donacion.as_view(), name='donacion'),
    path('locacion/', Locacion.as_view(), name='locacion'),
    path('comentarios/', Comentarios.as_view(), name='comentarios'),
    path('foro/', Foro.as_view(), name='foro'),
    path('faqs/', Faqs.as_view(), name='faqs'),
]
