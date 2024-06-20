from django.shortcuts import render
from django import forms
from .models import HECHO_ECONO

class HechoEconoForm(forms.ModelForm):
    
    class Meta:
        model = HECHO_ECONO
        fields = ['docto_conta', 'numero', 'fecha', 'descripcion','anulado', 'protegido', 'usuario', 'canal']

