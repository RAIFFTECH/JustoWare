from django.shortcuts import render
from django import forms
from .models import CENTROCOSTOS

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = CENTROCOSTOS
        fields = "__all__"
        
