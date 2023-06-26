"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from aplicacion1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplicacion1/', views.vista1, name = 'vista1'),
    path('ruta2/', include('aplicacion1.ruta2')),
    path('ruta3/', views.vista3, name = 'vista3'),
    path('ruta4/', views.vista4, name = 'vista4'),
    path('', views.vista5, name = 'vista5'),
    path('formulario/', views.vista6, name = 'vista6'),
    path('paginas/', include('aplicacion1.urls')),
]