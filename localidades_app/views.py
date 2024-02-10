from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import CrearForm
from .models import LOCALIDADES

@login_required
def Crear_Localidad(request):
    if request.method == 'GET':
        return render(request, 'Crear_Localidad.html', {'form': CrearForm})
    else:
        try:
            form = CrearForm(request.POST)
            new = form.save(commit = False)
            new.save()
            return render(request, 'Crear_Localidad.html',{'form': CrearForm})
        except ValueError:
            return render(request, 'Crear_Localidad.html', {
                'form': CrearForm,
                'error':'Los valores ingresados ya existen o no son válidos'
                })


@login_required
def Listar_Localidades(request):
    Lista = LOCALIDADES.objects.all()
    return render(request, 'Listar_Localidades.html', {'Lista': Lista})

class Lista_Localidades(ListView):
    model = LOCALIDADES
    template_name = 'Listar_Localidades.html'


@login_required
def Localidad_Creada(request, LOCALIDADES_id):
    if request.method == 'GET':
        Localidades = get_object_or_404(LOCALIDADES, pk=LOCALIDADES_id)
        form = CrearForm(instance=Localidades)
        return render(request, 'Localidad_Creada.html',{'Localidades': Localidades, 'form':form})
    else:
        try:
            Localidades = get_object_or_404(LOCALIDADES, pk=LOCALIDADES_id)
            form = CrearForm(request.POST, instance = Localidades)
            form.save()
            return redirect('Listar_Localidades')
        except ValueError:
            return render(request, 'Localidad_Creada.html',{'Localidades': Localidades, 'form': form,'error':'Error al actualizar'})
        

@login_required
def Eliminar_Localidad(request, LOCALIDADES_id):
    Localidad = get_object_or_404(LOCALIDADES, pk=LOCALIDADES_id)
    if request.method == 'POST':
        Localidad.delete()
        return redirect('Listar_Localidades')
