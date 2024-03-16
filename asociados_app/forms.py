from django.shortcuts import render
from django import forms
from .models import ASOCIADOS

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = ASOCIADOS
        fields = "__all__"
        
