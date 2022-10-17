from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404, HttpResponseRedirect
import datetime
from django.shortcuts import redirect, render
from .models import *
from django.forms import ValidationError

# Create your views here.
def confirmarReserva(request):
    
    return render(request,'confirmarReserva.html')

def sesion(request, idsesion):
    cli = Cliente.objects.get(id_cliente=idsesion)
    
    data = {
    'cliente': cli
    }
    
    return render (request, 'Bienvenida.html', data)

def verMenu(request):
    comida = Carta.objects.all()
    data = {'comida': comida}
    return render(request,'comida.html',data)

def elegirMesa(request):
    mesa = Mesa.objects.filter(estado='d')
    data = {'mesa': mesa}
    
    
    return render(request,'mesas.html',data)

def probando(request):
    return render (request, 'probando.html')

def recibircliente(request):
    nombre = request.POST['name']
    telefono = request.POST['tel']
    correo = request.POST['correo']
    fecha = request.POST['fecha']
    
    #import pdb
    #pdb.set_trace()        

    
    add = Cliente.objects.create(id_cliente=14,nombre=nombre,telefono=telefono,correo=correo,fecha=fecha)
    
    add.save()
   
    return redirect(to='elegirMesa')

def recibecliente(request):
    clientes = Cliente.objects.get(id_cliente=10)
    
    data = {
    'clientes': clientes
    }
    
    return render (request, 'recibe.html', data)

def vertodoclient(request):
    clientes = Cliente.objects.all()
    
    data = {
    'clientes': clientes
    }
    
    return render (request, 'dinamiclient.html', data)

def editarclient(request, id):
    clientes = Cliente.objects.get(id_cliente=id)
    
    data = {
    'clientes': clientes
    }
    
    return render (request, 'recibe.html', data)
# el get es para solo 1
# el filter es para varios es un filtro
# all trae todo...


def editarclientepost(request):
    id = request.POST['id']
    nombre = request.POST['name']
    telefono = request.POST['tel']
    correo = request.POST['correo']
    fecha = request.POST['fecha']    

    add = Cliente.objects.get(pk=id)
    add.nombre = nombre
    add.telefono = telefono
    add.correo = correo
    add.fecha = fecha
    add.save()
    return redirect(to='index')

def confirmar(request, id):
    c_reserva = Reserva.objects.get(id_reserva=id)

    datos = {
    'reserva': c_reserva,
    }
    return render (request, 'confirmarReserva.html', datos)

def listar_reserva(request):
    reserva = Reserva.objects.all()
    return render (request, 'listar_reserva.html', {'reserva': reserva})

def validar(request):
    reserva = Reserva.objects.all()
    if request.method == "POST":
        nombre_re = request.POST['nombre']
        telefono = request.POST['telefono']
        if Reserva.objects.filter(nombre_re=nombre_re).exists():
            return render(request, 'listar_reserva.html',{'reserva': reserva})
        else:
            return render (request, 'listar_reserva.html')
