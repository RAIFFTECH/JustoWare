from django.db import models
from ctas_ahorros_app.models import CTAS_AHORRO, OPC_BOOL
# Create your models here.

class CTA_CDAT(models.Model):
    cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE, verbose_name='Cuenta de Ahorro')
    ampliacion = models.IntegerField(verbose_name='Ampliación')
    valor = models.FloatField(null=True, blank=True, verbose_name='Valor')
    fecha = models.DateField(null=True, blank=True, verbose_name='Fecha')
    plazo_mes = models.IntegerField(null=True, blank=True, verbose_name='Plazo en Meses')
    tiae = models.FloatField(null=True, blank=True, verbose_name='Tasa Interes Anual Efectiva')
    Periodicidad = models.IntegerField(null=True, blank=True, verbose_name='Periodicidad')
    cta_int_ret = models.CharField(max_length=10, null=True, verbose_name='Cuenta Contable Intereses')
    aplicado = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Aplicado?')

    class Meta:
        unique_together = [['cta_aho', 'ampliacion']]
        db_table = 'cta_cdat'

    def __str__(self):
        return self.cta_aho