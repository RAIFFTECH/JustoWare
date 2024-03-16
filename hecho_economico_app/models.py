from django.db import models
from documentos_app.models import DOCTO_CONTA, OPC_BOOL
from justo_app.opciones import OPC_CANALES
# Create your models here.

class HECHO_ECONO(models.Model):
    docto_conta = models.ForeignKey(DOCTO_CONTA, on_delete=models.CASCADE, verbose_name='Documento')
    numero = models.IntegerField(blank=True, null=True, verbose_name='Número')
    fecha = models.DateField(null=True, blank=True, verbose_name='Fecha')
    descripcion = models.CharField(max_length=64, null=True, verbose_name='Descripción')
    anulado = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Anulado?')
    protegido = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Protegido?')
    fecha_prot = models.DateTimeField(auto_now=True, verbose_name='Fecha Protegido')
    usuario = models.CharField(max_length=16, null=True, verbose_name='Usuario')
    canal = models.CharField(max_length=3, choices=OPC_CANALES, verbose_name='Canal')
    id_ds = models.BigIntegerField(null=True, db_index=True, verbose_name='id_ds')

    class Meta:
        unique_together = [['docto_conta', 'numero']]
        db_table = 'hecho_econo'

    def __str__(self):
        return self.docto_conta+' '+self.numero