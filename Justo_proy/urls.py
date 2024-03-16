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
    path('clientes/', include('clientes_app.urls')),
    path('justo/', include('justo_app.urls')),
    path('localidades/', include('localidades_app.urls')),
    path('terceros/', include('terceros_app.urls')),
    path('oficinas/', include('oficinas_app.urls')), 
    path('pagadores/', include('pagadores_app.urls')),
    path('cta_ahorro/', include('ctas_ahorros_app.urls')),
    path('linea_ahorro/', include('lineas_ahorro_app.urls')),
    path('cuentas/', include('cuentas_app.urls')),
    path('centrocostos/', include('centrocostos_app.urls')),
    path('documentos/', include('documentos_app.urls')),
    path('destino_creditos/', include('destino_credito_app.urls')),
    path('linea_creditos/', include('lineas_credito_app.urls')),
    path('tasa_lin_aho/', include('tasas_lin_aho_app.urls')),
    path('retefuente_ahorros/', include('retefuente_ahorros_app.urls')),

]
