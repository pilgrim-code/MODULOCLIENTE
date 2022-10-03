from django.shortcuts import render,HttpResponse

class IndexController():
    def index(request):
       return render(request,'views/index/index.html')
    def about(request):
       return render(request,'views/index/about.html')
    def menu(request):
       return render(request,'views/index/menu.html')