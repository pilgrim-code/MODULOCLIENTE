from django import forms
#from App.models import Reserva,Cliente

class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class SignUpForm(forms.Form):
    '''nombre = forms.CharField(label='Nombre')
    telefono = forms.CharField(label='Telefono')
    email = forms.EmailField(label='Email')
    '''
class Agendar(forms.Form):
    nombre = forms.CharField(label='Nombre')
    telefono = forms.CharField(label='Telefono')
    email = forms.EmailField(label='Email')
    fecha = forms.DateField()


    