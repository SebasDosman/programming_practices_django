from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render

from django.urls import reverse

from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from parcialDjago.models import Departamento, Profesor, Curso


# Inicio
def inicio(request):
    return render(request, 'pages/inicio/index.html')

# Departamento 
class DepartamentoListado(ListView):
    model = Departamento 

class DepartamentoCrear(SuccessMessageMixin, CreateView):
    model = Departamento 
    form = Departamento 
    fields = "__all__" 
    success_message = 'Departamento creado correctamente!' 
    
    def get_success_url(self):
        return reverse('leer_departamento') 

class DepartamentoDetalle(DetailView): 
    model = Departamento 

class DepartamentoActualizar(SuccessMessageMixin, UpdateView): 
    model = Departamento 
    form = Departamento 
    fields = "__all__" 
    success_message = 'Departamento actualizada correctamente!' 
    
    def get_success_url(self):               
        return reverse('leer_departamento') 

class DepartamentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Departamento 
    form = Departamento
    fields = "__all__"     
    
    def get_success_url(self): 
        success_message = 'Departamento eliminado correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer_departamento')


# Profesor 
class ProfesorListado(ListView):
    model = Profesor 

class ProfesorCrear(SuccessMessageMixin, CreateView):
    model = Profesor 
    form = Profesor 
    fields = "__all__" 
    success_message = 'Profesor creado correctamente!' 
    
    def get_success_url(self):
        return reverse('leer_profesor') 

class ProfesorDetalle(DetailView): 
    model = Profesor 

class ProfesorActualizar(SuccessMessageMixin, UpdateView): 
    model = Profesor 
    form = Profesor 
    fields = "__all__" 
    success_message = 'Profesor actualizado correctamente!' 
    
    def get_success_url(self):               
        return reverse('leer_profesor') 

class ProfesorEliminar(SuccessMessageMixin, DeleteView): 
    model = Profesor 
    form = Profesor
    fields = "__all__"     
    
    def get_success_url(self): 
        success_message = 'Profesor eliminado correctamente!' 
        messages.success (self.request, (success_message))       
        return reverse('leer_profesor')


# Curso 
class CursoListado(ListView):
    model = Curso 

class CursoCrear(SuccessMessageMixin, CreateView):
    model = Curso 
    form = Curso 
    fields = "__all__" 
    success_message = 'Curso creado correctamente!' 
    
    def get_success_url(self):
        return reverse('leer_curso') 

class CursoDetalle(DetailView): 
    model = Curso 

class CursoActualizar(SuccessMessageMixin, UpdateView): 
    model = Curso 
    form = Curso 
    fields = "__all__" 
    success_message = 'Curso actualizado correctamente!' 
    
    def get_success_url(self):               
        return reverse('leer_curso') 

class CursoEliminar(SuccessMessageMixin, DeleteView): 
    model = Curso 
    form = Curso
    fields = "__all__"     
    
    def get_success_url(self): 
        success_message = 'Curso eliminado correctamente!' 
        messages.success (self.request, (success_message))       
        return reverse('leer_curso')
