from django.shortcuts import render
from django import forms
from .models import LOCALIDADES

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = LOCALIDADES
        fields = ['cliente','codigo','nombre','cod_pos','departamento']
        # widgets = {
        #             'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
        #             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        #             'cod_pos': forms.NumberInput(attrs={'class': 'form-control'}),
        #             'departamento': forms.TextInput(attrs={'class': 'form-control'}),
        # }
