"""
URL configuration for Justo_proy project.

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
from django.urls import path, include
from justo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name='Inicio'),
    # path('Registrar_Usuario/', views.Registrar_Usuario, name='Registrar_Usuario'),
    # path('Iniciar_Sesion/', views.Iniciar_Sesion, name='Iniciar_Sesion'),
    # path('Cerrar_Sesion/', views.Cerrar_Sesion, name='Cerrar_Sesion'),
    # path('JustoAdm/', views.JustoAdm, name='JustoAdm'),
    # path('num_let', views.convertir_numero_a_letras, name='Num_Let'),
    # path('dv', views.calcular_nit_dv, name='Calcula_DV'),
    path('clientes/', include('clientes_app.urls')),
    path('justo/', include('justo_app.urls')),
    path('localidades/', include('localidades_app.urls')),
    path('terceros/', include('terceros_app.urls')),
    path('oficinas/', include('oficinas_app.urls')),
    
]
