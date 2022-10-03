from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect

class Agenda():
    def index(request):
       return render(request,'views/agenda.html')
    def cReserva(request):
        return render(request,'views/confirmarReserva.html')