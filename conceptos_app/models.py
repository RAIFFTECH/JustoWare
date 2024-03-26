from django.db import models
from clientes_app.models import CLIENTES
from justo_app.opciones import OPC_BOOL
# Create your models here.

class CONCEPTOS(models.Model):
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE, null=True)
    cod_con = models.CharField(max_length=8, null=False)
    con_justo = models.CharField(max_length=1, choices=OPC_BOOL)
    descripcion = models.CharField(max_length=44, null=False)
    tip_dev_ap = models.CharField(max_length=1, choices=OPC_BOOL)
    tip_con = models.CharField(max_length=1, choices=OPC_BOOL)
    tip_sis = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_con = models.CharField(max_length=10, null=False)
    cta_con_pas = models.CharField(max_length=10, null=False)
    debito = models.CharField(max_length=1, choices=OPC_BOOL)
    credito = models.CharField(max_length=1, choices=OPC_BOOL)
    por_tercero = models.CharField(max_length=1, choices=OPC_BOOL)
    por_ret_fue = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = [['cliente', 'cod_con']]
        db_table = 'conceptos'

    def __str__(self):
        return self.cod_con
