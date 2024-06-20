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
    path('ampliacion_cdats/', include('ampliacion_cdat_app.urls')),
    path('aportes/', include('aportes_app.urls')),
    path('asociados/', include('asociados_app.urls')),
    path('backup/', include('backup_bd.urls')),
    path('cambios_creditos/', include('cambios_creditos_app.urls')), 
    path('categorias/', include('categorias_creditos_app.urls')),
    path('causacion/', include('causacion_creditos_app.urls')),
    path('cdats/', include('cdat_app.urls')),
    path('centrocostos/', include('centrocostos_app.urls')),
    path('cierre_mes/', include('cierre_mensual_app.urls')),
    path('clientes/', include('clientes_app.urls')),
    path('conceptos/', include('conceptos_app.urls')),  
    path('concapcre/', include('contabilizacion_capital_creditos_app.urls')),
    path('conintcre/', include('contabilizacion_intereses_creditos_app.urls')),
    path('conlinaho/', include('contabilizacion_lineas_ahorros_app.urls')),
    path('creditos/', include('creditos_app.urls')),
    path('cta_ahorro/', include('ctas_ahorros_app.urls')),
    path('cuentas/', include('cuentas_app.urls')),
    path('destino_creditos/', include('destino_credito_app.urls')),
    # 'detalle_economico_app',
    # 'detalle_producto_app',
    path('documentos/', include('documentos_app.urls')),
    # 'estados_financieros_app',
    path('comprobantes/', include('hecho_economico_app.urls')),
    # 'historico_ctas_ahorros_app',
    path('justo/', include('justo_app.urls')),
    path('linea_ahorro/', include('lineas_ahorro_app.urls')),
    path('linea_creditos/', include('lineas_credito_app.urls')),
    # 'liquidacion_cdat_app',
    path('localidades/', include('localidades_app.urls')),
    path('movimientos/', include('movimiento_caja_app.urls')),
    path('oficinas/', include('oficinas_app.urls')),
    path('originacion/', include('originacion_app.urls')),
    path('pagadores/', include('pagadores_app.urls')),
    path('retefuente_ahorros/', include('retefuente_ahorros_app.urls')),
    path('tasa_lin_aho/', include('tasas_lin_aho_app.urls')),
    path('terceros/', include('terceros_app.urls')),
    # 'usuarios_app',
    
]
