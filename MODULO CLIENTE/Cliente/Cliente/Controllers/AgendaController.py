from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from Cliente.Models.AgendarForm import SignUpForm
from Cliente.Models.AgendarForm import Agendar
from django.contrib import auth
from App.models import *

class Agenda():
    def index(request):
        #ESTE ES DE CREAR RESERVA LA MAGIA DEL FORMULARIO
      
        return render(request)
    
    def cReserva(request):
        #ESTE ES DE CONFIRMAR RESERVA
        return render(request,'views/confirmarReserva.html')