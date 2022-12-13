from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

#def index(request):
#    return HttpResponse("Hello, world!")

def brian(request):
    return HttpResponse("Hi, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

#create a new function that dynamically changes 
#def greet(request, name):
#    return HttpResponse(f"Hello, {name.capitalize()}!")

#use Django templates 
def index(request):
    return render(request, "myapp/index.html")

def greet(request, name):
    return render(request, "myapp/greet.html", {
        "name": name.capitalize()
    })
