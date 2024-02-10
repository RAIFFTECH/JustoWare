from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.Crear_Oficina, name= 'Crear_Oficina'),
    path('listar/', views.Listar_Oficinas, name='Listar_Oficinas'),
    path('lista/<int:OFICINAS_id>/', views.Oficina_Creada, name='Oficina_Creada'),
    path('elimina/<int:OFICINAS_id>/', views.Eliminar_Oficina, name='Eliminar_Oficina'),
]