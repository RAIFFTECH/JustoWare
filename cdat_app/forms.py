from django.shortcuts import render
from django import forms
from .models import CTA_CDAT

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = CTA_CDAT
        fields = "__all__"
