from django import forms
from App.models import *
from django.forms import ValidationError

class confirmarForm(forms.Form):
    nombre_re = forms.models.CharField(label='Nombre')

    def confirmacion(self,render,request):
        nombre_re = self.cleaned_data['Nombre']
        existe_t = Reserva.objects.filter(Nombre=nombre_re).exists()
        if existe_t:
            raise ValidationError("ESTE USUARIOS EXISTE :D")
            
        return render(request,'views/confirmarReserva.html')
                