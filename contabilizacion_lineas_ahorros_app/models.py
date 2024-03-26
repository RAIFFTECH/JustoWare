from django.db import models
from lineas_ahorro_app.models import LINEAS_AHORRO
# Create your models here.

class IMP_CON_LIN_AHO(models.Model):
    linea_ahorro = models.ForeignKey(LINEAS_AHORRO, on_delete=models.CASCADE, null=True)
    cod_imp = models.CharField(max_length=2, null=True)
    descripcion = models.CharField(max_length=40, null=True)
    ctaafeact = models.CharField(max_length=10, null=True)
    ctaafeina = models.CharField(max_length=10, null=True)
    ctaafeint = models.CharField(max_length=10, null=True)
    ctaretfue = models.CharField(max_length=10, null=True)

    class Meta:
        unique_together = [['linea_ahorro', 'cod_imp']]
        db_table = 'imp_con_lin_aho'

    def __str__(self):
        return self.linea_ahorro+' '+self.descripcion
