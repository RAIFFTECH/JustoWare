from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import CrearForm
from .models import TERCEROS

@login_required
def Crear_Tercero(request):
    if request.method == 'GET':
        return render(request, 'Crear_Tercero.html', {'form': CrearForm})
    else:
        try:
            form = CrearForm(request.POST)
            new = form.save(commit = False)
            new.save()
            return render(request, 'Crear_Tercero.html',{'form': CrearForm})
        except ValueError:
            return render(request, 'Crear_Tercero.html', {
                'form': CrearForm,
                'error':'Los valores ingresados ya existen o no son válidos'
                })


@login_required
def Listar_Terceros(request):
    Lista = TERCEROS.objects.all()#    filter(tercero=request.user)
    return render(request, 'Listar_Terceros.html', {'Lista': Lista})


class Lista_Terceros(ListView):
    model = TERCEROS
    template_name = 'Listar_Terceros.html'


@login_required
def Tercero_Creado(request, TERCEROS_id):
    if request.method == 'GET':
        Terceros = get_object_or_404(TERCEROS, pk=TERCEROS_id)
        form = CrearForm(instance=Terceros)
        return render(request, 'Tercero_Creado.html', {'Terceros': Terceros, 'form': form})
    else:
        try:
            Terceros = get_object_or_404(TERCEROS, pk=TERCEROS_id)
            form = CrearForm(request.POST, instance=Terceros)
            form.save()
            return redirect('Listar_Terceros')
        except ValueError:
            return render(request, 'Tercero_Creado.html', {'Terceros': Terceros, 'form': form, 'error': 'Error al actualizar'})
        

@login_required
def Eliminar_Tercero(request, TERCEROS_id):
    Tercero = get_object_or_404(TERCEROS, pk=TERCEROS_id)
    if request.method == 'POST':
        Tercero.delete()
        return redirect('Listar_Terceros')
