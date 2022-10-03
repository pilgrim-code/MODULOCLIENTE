from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from ..Models.AgendarForm import SignUpForm

from django.contrib import auth

class Agenda():
    def index(request):
        #ESTE ES DE CREAR RESERVA LA MAGIA DEL FORMULARIO
        template = 'views/agenda.html'
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                dataEmail = None
                email = form.cleaned_data.get('email')
                telefono = form.cleaned_data.get('telefono')
                fecha= form.cleaned_data.get('fecha')
               # user = form.cleaned_data.get('usuario')
               
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
            context = {'form': SignUpForm()}
        return render(request,template, context)
       #return render(request,'views/agenda.html')
    def cReserva(request):
        #ESTE ES DE CONFIRMAR RESERVA
        return render(request,'views/confirmarReserva.html')