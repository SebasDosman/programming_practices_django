"""
URL configuration for parcial_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from parcialDjago.views import (CursoActualizar, CursoCrear, CursoDetalle,
                                 CursoEliminar, CursoListado,
                                 DepartamentoActualizar, DepartamentoCrear,
                                 DepartamentoDetalle, DepartamentoEliminar,
                                 DepartamentoListado, ProfesorActualizar,
                                 ProfesorCrear, ProfesorDetalle,
                                 ProfesorEliminar, ProfesorListado, inicio)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', inicio, name = 'inicio'),
    
    path('cursos/', CursoListado.as_view(template_name = "models/curso/index.html"), name = 'leer_curso'),
    path('cursos/detalle/<int:pk>', CursoDetalle.as_view(template_name = "models/curso/detalles.html"), name = 'detalles_curso'),
    path('cursos/crear', CursoCrear.as_view(template_name = "models/curso/crear.html"), name = 'crear_curso'),
    path('cursos/editar/<int:pk>', CursoActualizar.as_view(template_name = "models/curso/actualizar.html"), name = 'actualizar_curso'), 
    path('cursos/eliminar/<int:pk>', CursoEliminar.as_view(), name = 'eliminar_curso'), 
    
    path('departamentos/', DepartamentoListado.as_view(template_name = "models/departamento/index.html"), name = 'leer_departamento'),
    path('departamentos/detalle/<int:pk>', DepartamentoDetalle.as_view(template_name = "models/departamento/detalles.html"), name = 'detalles_departamento'),
    path('departamentos/crear', DepartamentoCrear.as_view(template_name = "models/departamento/crear.html"), name = 'crear_departamento'),
    path('departamentos/editar/<int:pk>', DepartamentoActualizar.as_view(template_name = "models/departamento/actualizar.html"), name = 'actualizar_departamento'), 
    path('departamentos/eliminar/<int:pk>', DepartamentoEliminar.as_view(), name = 'eliminar_departamento'), 
    
    path('profesores/', ProfesorListado.as_view(template_name = "models/profesor/index.html"), name = 'leer_profesor'),
    path('profesores/detalle/<int:pk>', ProfesorDetalle.as_view(template_name = "models/profesor/detalles.html"), name = 'detalles_profesor'),
    path('profesores/crear', ProfesorCrear.as_view(template_name = "models/profesor/crear.html"), name = 'crear_departamento'),
    path('profesores/editar/<int:pk>', ProfesorActualizar.as_view(template_name = "models/profesor/actualizar.html"), name = 'actualizar_profesor'), 
    path('profesores/eliminar/<int:pk>', ProfesorEliminar.as_view(), name = 'eliminar_profesor'), 
]
