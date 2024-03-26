from django.db import models
from oficinas_app.models import OFICINAS
from justo_app.opciones import OPC_BOOL
# Create your models here.

class MOV_CAJA(models.Model):
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null=True, blank=True)
    cod_caj = models.CharField(max_length=2, null=False)
    jornada = models.CharField(max_length=1, null=False)
    saldo_ini = models.FloatField(null=True, blank=True)
    debitos = models.FloatField(null=True, blank=True)
    creditos = models.FloatField(null=True, blank=True)
    val_che_dev = models.FloatField(null=True, blank=True)
    saldo_fin = models.FloatField(null=True, blank=True)
    diferencia = models.FloatField(null=True, blank=True)
    val_cheques = models.FloatField(null=True, blank=True)
    val_vales = models.FloatField(null=True, blank=True)
    cerrado = models.CharField(max_length=1, null=False, choices=OPC_BOOL)
    monedas = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = [['oficina', 'fecha', 'cod_caj', 'jornada']]
        db_table = 'mov_caja'

    def __str__(self) -> str:
        return self.oficina+' '+self.fecha