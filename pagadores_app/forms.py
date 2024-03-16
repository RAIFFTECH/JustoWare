from django.shortcuts import render
from django import forms
from .models import PAGADORES

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = PAGADORES
        # fields = ['cliente','codigo','nombre','ciudad','pagador','tel_cel']
        fields = "__all__"
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select rounded-pill'}), 
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-select rounded-pill'}),
            'pagador': forms.TextInput(attrs={'class': 'form-control'}),
            'tel_cel': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
        }
