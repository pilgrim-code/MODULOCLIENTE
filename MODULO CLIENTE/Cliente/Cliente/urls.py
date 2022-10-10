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
    path('confirmarReserva', Agenda.cReserva, name='confirmarReserva'),
    path('menu', IndexController.menu, name='menu'),
    path('probando', views.probando, name='probando'),
    path('addcliente', views.recibircliente, name='addcliente'),
    path('vercliente', views.recibecliente, name='vercliente'),
    path('dinamiclient', views.vertodoclient, name='dinamiclient'),
    path('editarclient/<int:id>',views.editarclient, name='editarclient'),
    path('editarclientepost',views.editarclientepost, name='editarclientepost'),



]
