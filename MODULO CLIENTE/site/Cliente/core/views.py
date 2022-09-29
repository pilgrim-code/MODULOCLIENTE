from msilib.schema import Class
from django.shortcuts import redirect, render,HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

class Template():
    def toHome(request):
        return render(request,"C:/Users/jorge/Desktop/Modulo_Django/MODULOCLIENTE/MODULO CLIENTE/site/templates/views/index.html")




