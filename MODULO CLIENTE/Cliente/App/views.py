from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404, HttpResponseRedirect
import datetime
from .models import *

# Create your views here.


def probando(request):
    return render (request, 'probando.html')

def recibircliente(request):
    nombre = request.POST['name']
    telefono = request.POST['tel']
    correo = request.POST['correo']
    fecha = request.POST['fecha']
    
    import pdb
    pdb.set_trace()        

    
    add = Cliente.objects.create(id_cliente=10,nombre=nombre,telefono=telefono,correo=correo,fecha=fecha)
    add.save()
    return redirect(to='index')

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