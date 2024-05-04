from django.shortcuts import render
from django import forms
from .models import ASOCIADOS, ASO_BENEF, ASO_REFERENCIAS

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = ASOCIADOS,ASO_BENEF,ASO_REFERENCIAS
        fields = "__all__"
