from django.shortcuts import render
from django import forms
from .models import CREDITOS

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = CREDITOS
        fields = "__all__"
        
