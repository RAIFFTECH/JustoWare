from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .models import PAGADORES
from django.contrib.auth.decorators import login_required

# Para obtener todos los registros de la tabla de pagadores
# @login_required
class Lista(ListView):
    model = PAGADORES
    template_name = 'lista.html'

# Para obtener todos los campos de un registro de la tabla pagadores
# @login_required
class Detalles(DetailView):
    model = PAGADORES
    template_name = 'detalles.html'
 
# Para crear un nuevo pagador en la tabla pagadores
# @login_required
class Crear(SuccessMessageMixin,CreateView):
    model = PAGADORES
    form = PAGADORES
    fields = "__all__"
    template_name = 'crear.html'

    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido correctamente.'

    # Redirigimos a la página principal tras insertar el registro
    def get_success_url(self):
        return reverse('Lista')

# Para modificar un pagador existente de la tabla pagadores
# @login_required
class Actualizar(SuccessMessageMixin, UpdateView):
    model = PAGADORES
    form = PAGADORES
    fields = "__all__"
    template_name = 'actualizar.html'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return render(self, template_name='lista.html')

# Para eliminar un pagador de la tabla pagadores
# @login_required
class Eliminar(SuccessMessageMixin, DeleteView):
    model = PAGADORES
    form = PAGADORES
    fields = "__all__"

    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return render('Lista')
