from django.shortcuts import render
from django.http import HttpResponse
from aplicacion1.models import Webs
from . import forms

# Create your views here.

def vista1(request):
    return HttpResponse("Hola Mundo")

def vista2(request):
    return HttpResponse("Adios Mundo")

def vista3(request):
    diccionario = {'etiqueta': 'Este es un NUEVO ejemplo'}
    return render(request, "aplicacion1/pagina1.html", context = diccionario)

def vista4(request):
    diccionario = {}
    return render(request, "aplicacion1/pagina2.html", context = diccionario)

def vista5(request):
    lista_webs = Webs.objects.order_by('nombre')
    diccionario = {'Lista Webs': lista_webs}
    return render(request, "aplicacion1/portada.html", context = diccionario)

def vista6(request):
    formulario = forms.Formulario()
    diccionario = {'formulario': formulario}
    
    if request.method == 'POST':
        formulario1 = forms.Formulario(request.POST)
        if formulario1.is_valid():
            nombre = formulario1.cleaned_data['nombre']
            correo = formulario1.cleaned_data['email']
            print("Nombre = " + nombre)
            print("Correo = " + correo)
    
    return render(request, "aplicacion1/formulario.html", context = diccionario)

def pagina4(request):
    diccionario = {}
    return render(request, "aplicacion1/pagina4.html", context = diccionario)

def pagina5(request):
    diccionario = {}
    return render(request, "aplicacion1/pagina5.html", context = diccionario)