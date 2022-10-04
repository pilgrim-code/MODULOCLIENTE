from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.urls import is_valid_path
from App.forms import Agendar

from django.contrib import auth

class Agenda():
    def index(request):
        #ESTE ES DE CREAR RESERVA LA MAGIA DEL FORMULARIO
        template = 'views/agenda.html'
        if request.method == 'POST':
            form = Agendar(request.POST)
            if form.is_valid():
                dataEmail = None
                email = form.cleaned_data.get('email')
                telefono = form.cleaned_data.get('telefono')
                fecha= form.cleaned_data.get('fecha')
                nombre = form.cleaned_data.get('nombre')
               
                userdb = Reserva.objects.filter(email=email)
               # userdb = User.objects.all()
                for item in userdb:
                    print(item)
                    dataEmail=item.email
                  #  dataUser = item.user
                    print(dataEmail)
                   # print(dataUser)
                    
                if dataEmail != None:
                    context = {'form':form ,'error':'El correo ya esta registrado, prueba con otro' }
                    return render(request,template,context)
                #elif dataUser == user:
               #     context = {'form':form ,'error':'El Usuario ya esta registrado, prueba con otro' }
                #    return render(request,template,context)
                    
                else:
                    nombre = form.cleaned_data.get('nombre')
                
                    email = form.cleaned_data.get('email')
                    telefono = form.cleaned_data.get('telefono')
                    
                    Reserva.objects.create_user(
                                             nombre_re=nombre,
                                             fecha = fecha,
                                             telefono= telefono,
                                             email=email,
                                             
                                            
                                             )
                    Reserva = auth.authenticate(username=email,password=telefono)
                    auth.login(request,Reserva)
                    return HttpResponseRedirect("admin/")
            else:
                context = {'form': form}
                return render(request,template,context)
            
        else:
            context = {'form': Agendar()}
        return render(request,template, context)
       #return render(request,'views/agenda.html')
    def CrearReserva(request):
        data = {
            
            'form': Agendar()
       }
        if request.method == 'POST':
            formulario = Agendar(data=request.POST)
            if formulario.is_valid():
                formulario.save()
            else:
                data['form']= formulario
        return render(request,'views/agenda.html',data)
        
    def cReserva(request):
        #ESTE ES DE CONFIRMAR RESERVA
        return render(request,'views/confirmarReserva.html')
