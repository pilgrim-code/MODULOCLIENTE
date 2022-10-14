from django import forms
from App.models import *
from django.forms import ValidationError

class confirmarForm(forms.Form):
    nombre_re = forms.models.CharField(label='Nombre')
    telefono = forms.models.CharField(label='Telefono')

    def confirmar(self,render,request):
        nombre_re = self.cleaned_data['Nombre']
        telefono = self.cleaned_data['Telefono']
        existe_nom = Reserva.objects.filter(Nombre = nombre_re).exists()
        existe_fono = Reserva.objects.filter(Telefono=telefono).exists()

        if existe_nom and existe_fono:
            raise ValidationError("Reserva confirmada")
            
        return render(request,'views/confirmarReserva.html')
                