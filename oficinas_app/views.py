from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import CrearForm
from .models import OFICINAS

@login_required
def Crear_Oficina(request):
    if request.method == 'GET':
        return render(request, 'Crear_Oficina.html', {'form': CrearForm})
    else:
        try:
            form = CrearForm(request.POST)
            new = form.save(commit = False)
            new.save()
            return render(request, 'Crear_Oficina.html',{'form': CrearForm})
        except ValueError:
            return render(request, 'Crear_Oficina.html', {
                'form': CrearForm,
                'error':'Los valores ingresados ya existen o no son válidos'
                })


@login_required
def Listar_Oficinas(request):
    Lista = OFICINAS.objects.all()
    return render(request, 'Lista_Oficinas.html', {'Lista': Lista})

class Lista_Oficinas(ListView):
    model = OFICINAS
    template_name = 'Lista_Oficinas.html'


@login_required
def Oficina_Creada(request, OFICINAS_id):
    if request.method == 'GET':
        Oficinas = get_object_or_404(OFICINAS, pk=OFICINAS_id)
        form = CrearForm(instance=Oficinas)
        return render(request, 'Oficina_Creada.html',{'Oficinas': Oficinas, 'form':form})
    else:
        try:
            Localidades = get_object_or_404(OFICINAS, pk=OFICINAS_id)
            form = CrearForm(request.POST, instance = Oficinas)
            form.save()
            return redirect('Listar_Oficinas')
        except ValueError:
            return render(request, 'Oficina_Creada.html',{'Oficinas': Oficinas, 'form': form,'error':'Error al actualizar'})
        

@login_required
def Eliminar_Oficina(request, OFICINAS_id):
    Oficina = get_object_or_404(OFICINAS, pk=OFICINAS_id)
    if request.method == 'POST':
        Oficina.delete()
        return redirect('Listar_Oficinas')
