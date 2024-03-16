from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth import password_reset, password_reset_done,password_reset_confirm, password_reset_complete
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import inflect
from num2words import num2words
from clientes_app.models import CLIENTES

CLIENTE_GLOBAL = 'este es una prueba'
OFICINA_GLOBAL = ''
PERIODO_GLOBAL = ''

# Create your views here.

def Inicio(request):
    return render(request, 'inicio.html')


def Registrar_Usuario(request):
    if request.method == 'GET':
        return render(request, 'Registrar_Usuario.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                # user = authenticate(username=usuario.clean_fields['username'],password=usuario.clean_fields['password1'])
                login(request, usuario)
                return redirect('Inicio')
            except IntegrityError:
                return render(request, 'Registrar_Usuario.html', {
                    'form': UserCreationForm,
                    'error': 'El Usuario ya existe'
                })
        return render(request, 'Registrar_Usuario.html', {
            'form': UserCreationForm,
            'error': 'Las Contraseñas no coinciden'
        })
    

@login_required
def Cerrar_Sesion(request):
    logout(request)
    return redirect('Inicio')


def Iniciar_Sesion(request):
    if request.method == 'GET':
        return render(request, 'Iniciar_Sesion.html', {
        'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'Iniciar_Sesion.html', {
            'form': AuthenticationForm,
            'error': 'El Usuario o la contraseña no es correcto'
        })
        else:
            login(request, usuario)
            print(request)
            return redirect('JustoAdm')


def JustoAdm(request):
    return render(request, 'JustoAdm.html')


def Restablecer_Contraseña(request):
    return "hola mundo"


def convertir_numero_a_letras(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        numero_en_letras = num2words(numero, lang = 'es').upper()
        return render(request, 'resultado.html', {'numero_en_letras': numero_en_letras})
    return render(request, 'formulario.html')

# def calcular_dv(nit):
#     nit = str(nit).zfill(9)  # Asegúrate de que el NIT tenga 9 dígitos
#     total = sum(int(nit[i]) * (i % 7 + 2) for i in range(9))
#     dv = (11 - total % 11) % 11
#     return dv
def calcular_dv(nit):
    nit = str(nit).zfill(9)  # Asegúrate de que el NIT tenga 9 dígitos
    total = sum(int(nit[i]) * (i % 7 + 2) for i in range(9))
    dv = (11 - total % 11) % 11
    return dv

def calcular_nit_dv(request):
    if request.method == 'POST':
        nit = request.POST.get('nit')
        try:
            nit = int(nit)
            dv = calcular_dv(nit)
            # nit_con_dv = "{}-{}".format(nit, dv)
            nit_con_dv = "{}".format(dv)
            return render(request, 'resultado.html', {'nit_con_dv': nit_con_dv})
        except ValueError:
            error_message = "Por favor, ingresa un número de identificación válido."
            return render(request, 'formulario.html', {'error_message': error_message})
    return render(request, 'formulario.html')



