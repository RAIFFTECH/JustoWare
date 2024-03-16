from django.db import models
from asociados_app.models import ASOCIADOS

# Create your models here.
class ORIGINACION(models.Model):
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE, verbose_name='Asociado')
    lin_cre = models.CharField(max_length=80, null=False, verbose_name='Línea de Crédito')
    monto = models.FloatField(blank=True, null=True, verbose_name='Monto')
    plazo = models.IntegerField(blank=True, null=True, verbose_name='Plazo')
    gar_cre_sol = models.CharField(max_length=1, null=False, verbose_name='Garantía Crédito Solidario?')
    lin_cre_sol = models.CharField(max_length=1, null=False, verbose_name='Línea Crédito Solidario')
    mod_cre_sol = models.CharField(max_length=1, null=False, verbose_name='Modalidad Crédito Solidario')

    class Meta:
        unique_together = [['asociado']]
        db_table = 'originacion'

    def __str__(self):
        return self.asociado
