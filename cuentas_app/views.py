from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .models import PLAN_CTAS

# Para obtener todos los registros de la tabla de pagadores
class Lista(LoginRequiredMixin, ListView):
    model = PLAN_CTAS
    template_name = 'lista_cuentas.html'

# Para obtener todos los campos de un registro de la tabla pagadores
class Detalles(LoginRequiredMixin, DetailView):
    model = PLAN_CTAS
    template_name = 'detalles_cuenta.html'

# Para crear un nuevo pagador en la tabla pagadores
class Crear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PLAN_CTAS
    form = PLAN_CTAS
    fields = "__all__"
    template_name = 'crear_cuenta.html'

    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido correctamente.'

    # Redirigimos a la página principal tras insertar el registro
    def get_success_url(self):
        return reverse('listar')

# Para modificar un pagador existente de la tabla pagadores
class Actualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PLAN_CTAS
    form = PLAN_CTAS
    fields = "__all__"
    template_name = 'actualizar_cuenta.html'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('listar')

# Para eliminar un pagador de la tabla pagadores
class Eliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PLAN_CTAS
    form = PLAN_CTAS
    fields = "__all__"

    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('listar')
