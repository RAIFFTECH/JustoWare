from django.shortcuts import render
from django import forms
from .models import TERCEROS

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = TERCEROS
        # fields = ['cliente','cla_doc','doc_ide','dig_ver','nit_rap','cod_ciu_exp','cod_ciu_res','regimen','fec_exp_ced','tip_ter','pri_ape','seg_ape','pri_nom','seg_nom','raz_soc','direccion','cod_pos','tel_ofi','tel_res','id_ds','celular1','celular2','fax','email','fec_act','observacion','per_pub_exp','nit_interno']

        fields = "__all__"