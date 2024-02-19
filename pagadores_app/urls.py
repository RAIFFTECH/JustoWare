from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from .views import Crear,Lista,Detalles,Actualizar,Eliminar
from django.conf.urls.static import static

urlpatterns = [
    # Para mostrar formulario de alta de nuevo registro
    path('crear/', Crear.as_view(), name='crear'),

    # Para mostrar todos los registros en una tabla
    path('lista/', Lista.as_view(), name='lista'),

    # Para mostrar una página con el detalle del registro
    path('lista/detalles/<int:pk>', Detalles.as_view(), name='detalles'),
    
    path('lista/actualizar/<int:pk>', Actualizar.as_view(), name='actualizar'),

    path('eliminar/<int:pk>', Eliminar.as_view(), name='eliminar'),

]