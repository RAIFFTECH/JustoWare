from django.shortcuts import render
from django import forms
from .models import USUARIOS
# 
class CrearForm(forms.ModelForm):
    
    class Meta:
        model = USUARIOS
        fields = "__all__"
