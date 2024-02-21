from django.db import models
from oficinas_app.models import OFICINAS
from asociados_app.models import ASOCIADOS
from lineas_ahorro_app.models import LINEAS_AHORRO
from justo_app.opciones import OPC_BOOL,OPC_EST_CTA_AHO

# Create your models here.

class CTAS_AHORRO(models.Model):
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE,verbose_name='Oficina')
    lin_aho = models.ForeignKey(LINEAS_AHORRO, on_delete=models.CASCADE,verbose_name='Línea de Ahorro')
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE,verbose_name='Nombre')
    num_cta = models.CharField(max_length=10, null=True,verbose_name='Número Cuenta')
    est_cta = models.CharField(max_length=1, choices=OPC_EST_CTA_AHO,verbose_name='Estado Cuenta')
    fec_apertura = models.DateField(null=True, blank=True,verbose_name='Fecha Apertura')
    fec_cancela = models.DateField(null=True, blank=True,verbose_name='Fecha Cancelación')
    exc_tas_mil = models.CharField(max_length=1, choices=OPC_BOOL,verbose_name='Exenta 4x1000')
    fec_ini_exc = models.DateField(null=True, blank=True,verbose_name='Fecha Exención')

    class Meta:
        unique_together = [['oficina', 'num_cta']]
        db_table = 'ctas_ahorro'

    def __str__(self):
        return self.num_cta
