from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404, HttpResponseRedirect
import datetime
from django.shortcuts import redirect, render
from .models import *
from django.forms import ValidationError
import json
from django.template import loader

# Create your views here.
def confirmarReserva(request):
    
    return render(request,'confirmarReserva.html')

def sesion(request, idsesion):
    cli = Cliente.objects.get(id_cliente=idsesion)
    
    data = {
    'cliente': cli
    }
    
    return render (request, 'Bienvenida.html', data)
def CrearPedido(request):
    mesa = Mesa.objects.get(id_mesa=id)
    pedido = Pedido.objects.get(mesa_id_mesa=mesa)
    pedido_nuevo = Pedido.objects.all().count()
    fecha = Reserva.objects.get(fecha)
    pedido_nuevo = int(pedido_nuevo) + 1
    add = Pedido.objects.create(id_pedido=pedido_nuevo,fecha=fecha,estado='p',mesa_id_mesa=pedido)
    add.save()
    
    return render(request,'pedido.html')
def verMenu(request):
    comida = Carta.objects.all()
    mesa = Mesa.objects.all()
   
   
    
    data = {'comida': comida,
            'mesa':mesa}
    return render(request,'comida.html',data)

def elegirMesa(request):
    mesas = Mesa.objects.filter(estado='d')
    
    mesas = {'mesas': mesas}
    
    
    return render(request,'mesas.html',mesas)

def probando(request):
    return render (request, 'probando.html')

def recibircliente(request):
    nombre = request.POST['name']
    telefono = request.POST['tel']
    correo = request.POST['correo']
    fecha = request.POST['fecha']
    
    #import pdb
    #pdb.set_trace()        

    cliente = Cliente.objects.all().count()
    
    cliente = int(cliente) + 1
    add = Cliente.objects.create(id_cliente=cliente,nombre=nombre,telefono=telefono,correo=correo,fecha=fecha)
    
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
    # 'id':id
    }
    return render (request, 'confirmarReserva.html', datos)

def listar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id_reserva=id)
        estado = 'a'
        mesa = Mesa.objects.get(reserva_id_reserva=id)
        estado_mesa = 'o'
        mesa.estado = estado_mesa
        mesa.save()
        reserva.sesion = estado
        reserva.save()
        id_mesa = Mesa.objects.get(id_mesa=id)
    except:
        reserva = ''
        
    data = {
        'reserva': reserva,
        'mesa': mesa,
        'id_mesa':id_mesa,
    }
    return render (request, 'listar_reserva.html', data)

def validar(request):
    reserva = Reserva.objects.all()
    
    if request.method == "POST":
        nombre_re = request.POST['nombre']
        telefono = request.POST['telefono']
        if Reserva.objects.filter(nombre_re=nombre_re).exists():
          
            return render(request, 'listar_reserva.html',{'reserva': reserva})
        else:
            return render (request, 'listar_reserva.html')



def filter_idsito(request):
    if request.method == 'POST':
        telefono = request.POST.get('telefono')
        nombre = request.POST.get('nombre')

        try:
            reserva = Reserva.objects.get(nombre_re=nombre,telefono=telefono)
        except:
            reserva = None
            
        # import pdb
        # pdb.set_trace()
        
        filteridsito_html = loader.render_to_string(
            'includes/filter_id.html', {
                'reserva':reserva,
            }
        )

        data = {
            'filteridsito_html':filteridsito_html,
        }
    else:
        data = {
            'error':'no funcione',
        }
    return HttpResponse(
            json.dumps(data),
            content_type="aplication/json"
        )
def foranea_mesa(request):
    
    return render(request, 'listar_reserva.html')