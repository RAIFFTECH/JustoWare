from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .models import LINEAS_AHORRO

# Para obtener todos los registros de la tabla de pagadores
class Lista(LoginRequiredMixin, ListView):
    model = LINEAS_AHORRO
    form = LINEAS_AHORRO
    template_name = 'lista.html'

# Para obtener todos los campos de un registro de la tabla pagadores
class Detalles(LoginRequiredMixin, DetailView):
    model = LINEAS_AHORRO
    form = LINEAS_AHORRO
    template_name = 'detalles1.html'

# Para crear un nuevo pagador en la tabla pagadores
class Crear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = LINEAS_AHORRO
    form = LINEAS_AHORRO
    fields = "__all__"
    template_name = 'crear.html'

    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido correctamente.'

    # Redirigimos a la página principal tras insertar el registro
    def get_success_url(self):
        return reverse('listar')

# Para modificar un pagador existente de la tabla pagadores
class Actualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = LINEAS_AHORRO
    form = LINEAS_AHORRO
    fields = "__all__"
    template_name = 'actualizar.html'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('listar')

# Para eliminar un pagador de la tabla pagadores
class Eliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = LINEAS_AHORRO
    form = LINEAS_AHORRO
    fields = "__all__"

    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('listar')
