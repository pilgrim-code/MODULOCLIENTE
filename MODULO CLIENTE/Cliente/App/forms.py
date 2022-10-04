from django import forms
from matplotlib import widgets
from matplotlib.widgets import Widget
from .models import Reserva
from .views import Agenda
class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class Agendar(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ["nombre","telefono","fecha"]

    '''nombre = forms.CharField(label='Nombre')
        telefono = forms.CharField(label='Telefono')
        email = forms.EmailField(label='Email')
        widgets = {'fecha': forms.DateInput(attrs={'type':'date'})}
        '''
