"""Cliente URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from Cliente.Controllers.indexController import IndexController
from Cliente.Controllers.AgendaController import Agenda
from App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexController.index, name='index'),
    path('agenda', Agenda.index, name='agenda'),
    path('confirmarReserva', views.confirmarReserva, name='confirmarReserva'),
    path('confirmar/<int:id>', views.confirmar, name='confirmar'),
    path('validar', views.validar, name='validar'),
    path('listar_reserva', views.listar_reserva, name='Listado'),
    path('sesion/<int:id>', views.sesion, name='sesion'),
    path('sesion/<int:id>', views.sesion, name='sesion'),
    path('menu', IndexController.menu, name='menu'),
    path('probando', views.probando, name='probando'),
    #guia
    path('addcliente', views.recibircliente, name='addcliente'),
    path('vercliente', views.recibecliente, name='vercliente'),
    path('dinamiclient', views.vertodoclient, name='dinamiclient'),
    #guia
    path('editarclient/<int:id>',views.editarclient, name='editarclient'),
    #guia
    path('editarclientepost',views.editarclientepost, name='editarclientepost'),
    path('comida', views.verMenu, name='comida'),
    path('elegirMesa/<int:id>', views.elegirMesa, name='elegirMesa'),
    
]
