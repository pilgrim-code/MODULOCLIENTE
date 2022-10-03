from django import forms

class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class SignUpForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    telefono = forms.CharField(label='Telefono')
    email = forms.EmailField(label='Email')
   
  
    