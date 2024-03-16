from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .forms import CrearForm
from .models import LINEAS_AHORRO

# Para obtener todos los registros
class Lista(LoginRequiredMixin, ListView):
    model = LINEAS_AHORRO
    form = CrearForm
    template_name = 'lista_lin_aho.html'

# Para obtener todos los detalles de un registro 
class Detalles(LoginRequiredMixin, DetailView):
    model = LINEAS_AHORRO
    form = CrearForm
    template_name = 'detalles_lin_aho.html'

# Para crear un nuevo registro
class Crear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = LINEAS_AHORRO
    form = CrearForm
    fields = "__all__"
    template_name = 'crear_lin_aho.html'

    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido correctamente.'

    # Redirigimos a la página principal tras insertar el registro
    def get_success_url(self):
        return reverse('listar')

# Para modificar un registro
class Actualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = LINEAS_AHORRO
    form = CrearForm
    fields = "__all__"
    template_name = 'actualizar_lin_aho.html'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('listar')

# Para eliminar un registro
class Eliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = LINEAS_AHORRO
    form = CrearForm
    fields = "__all__"

    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('listar')
