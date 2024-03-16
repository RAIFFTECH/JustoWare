from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name= 'inicio'),
    path('Registrar_Usuario/', views.Registrar_Usuario, name='Registrar_Usuario'),
    path('Iniciar_Sesion/', views.Iniciar_Sesion, name='Iniciar_Sesion'),
    path('Cerrar_Sesion/', views.Cerrar_Sesion, name='Cerrar_Sesion'),
    path('Restablecer_Contraseña/', views.Restablecer_Contraseña, name='Restablecer_Contraseña'),
    path('JustoAdm/', views.JustoAdm, name='JustoAdm'),
    path('convertir/', views.convertir_numero_a_letras, name='convertir_numero_a_letras'),
    path('dv/', views.calcular_dv, name='Calcula_DV'),
    

]
