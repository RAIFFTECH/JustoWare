from django.db import models
import re
from django.core.exceptions import ValidationError
from justo_app.models import validate_numeric, DefaultToZeroMixin
from justo_app.opciones import OPC_BOOL, OPC_REGIMEN, OPC_CLASEDOC, OPC_TIPTER
from clientes_app.models import CLIENTES
from localidades_app.models import LOCALIDADES

class TERCEROS(models.Model):
    cliente = models.ForeignKey(CLIENTES, on_delete=models.PROTECT, verbose_name='Cliente')
    cla_doc = models.CharField(max_length=1, choices=OPC_CLASEDOC, verbose_name='Tipo Documento')
    doc_ide = models.CharField(max_length=12, null=False, verbose_name='Número Documento')
    dig_ver = models.CharField(max_length=1, blank=True,  null=False, verbose_name='DV')
    nit_rap = models.CharField(max_length=12, blank=True, null=False, verbose_name='Nit Rápido')
    cod_ciu_exp = models.ForeignKey(LOCALIDADES, on_delete=models.PROTECT, related_name='ciu_exp', null=True, blank=True, verbose_name='Ciudad Expedición Documento')
    cod_ciu_res = models.ForeignKey(LOCALIDADES, on_delete=models.PROTECT, related_name='ciu_res', null=True, blank=True, verbose_name='Ciudad Residencia' )
    regimen = models.CharField(max_length=12, choices=OPC_REGIMEN, verbose_name='Tipo Régimen')
    fec_exp_ced = models.DateField(null=True, blank=True, verbose_name='Fecha Expedición Documento')
    tip_ter = models.CharField(max_length=12, choices=OPC_TIPTER, verbose_name='Tipo Tercero')
    pri_ape = models.CharField(max_length=28, null=True, verbose_name='Primer Apellido')
    seg_ape = models.CharField(max_length=28, blank=True, null=False, verbose_name='Segundo Apellido')
    pri_nom = models.CharField(max_length=28, null=True, verbose_name='Primer Nombre')
    seg_nom = models.CharField(max_length=28, blank=True, null=False, verbose_name='Segundo Nombre')
    raz_soc = models.CharField(max_length=120, blank=True, null=False, verbose_name='Razón Social')
    direccion = models.CharField(max_length=80, null=True, verbose_name='Dirección')
    cod_pos = models.CharField(max_length=8, null=True, verbose_name='Código Postal')
    tel_ofi = models.CharField(max_length=10, null=True, verbose_name='Teléfono Oficina')
    tel_res = models.CharField(max_length=10, null=True, verbose_name='Teléfono Residencia')
    id_ds = models.BigIntegerField(null=True, blank=True, db_index=True)
    celular1 = models.CharField(max_length=10,validators=[validate_numeric],help_text='El número de celular debe contener exactamente 10 dígitos numéricos.',null=True, verbose_name='Celular 1')
    celular2 = models.CharField(max_length=10, null=True, verbose_name='Celular 2')
    fax = models.CharField(max_length=10, null=True, verbose_name='Fax')
    email = models.EmailField(verbose_name='e-mail')
    nombre = models.CharField(max_length=120, blank=True, null=False, verbose_name='Nombre')
    fec_act = models.DateField(null=True, blank=True, verbose_name='Fecha Actualización')
    observacion = models.CharField(max_length=255, blank=True, null=False, verbose_name='Observación')
    per_pub_exp = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Persona Expuesta PEP')
    nit_interno = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Nit Interno')

    def save(self, *args, **kwargs):
        if self.tip_ter == "N":
            self.nombre = """%s %s %s %s""" % (
                self.pri_ape, self.seg_ape, self.pri_nom, self.seg_nom)
        else:
            self.nombre = self.raz_soc
        super().save(*args, **kwargs)

    class Meta:
        unique_together = [['cliente', 'cla_doc', 'doc_ide']]
        # indexes = ['cliente', 'nombre']
        db_table = 'terceros'

    
    def __str__(self):
        return self.nombre + ' ' + self.doc_ide
    