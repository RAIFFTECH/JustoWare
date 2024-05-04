from django.shortcuts import render
from django import forms
from .models import CTAS_AHORRO

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = CTAS_AHORRO
        fields = "__all__"