from django.shortcuts import render
from django import forms
from .models import MOV_CAJA

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = MOV_CAJA
        fields = "__all__"
        
