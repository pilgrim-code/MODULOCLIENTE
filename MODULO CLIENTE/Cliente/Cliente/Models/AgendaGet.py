from django import forms
from App.models import *
from django.forms import ValidationError

class agendaForm(forms.Form):
    telefono = forms.CharField(label='Telefono')
    email = forms.EmailField(label='Email')
    
    
    
    
    def mi_reserva(self,render,request):
        email = self.cleaned_data['email']
        #Textbox del html 
        telefono = self.cleaned_data['telefono']
        existe_t = Cliente.objects.filter(telefono=telefono).exists()
        #Aqui se hace la query a la bd en especifico si existe el telefono
        existe_e = Cliente.objects.filter(correo=email).exists()
        if existe_e and existe_t:
            raise ValidationError("ESTE USUARIOS EXISTE :D")
            
        return render(request,'views/confirmarReserva.html')
                