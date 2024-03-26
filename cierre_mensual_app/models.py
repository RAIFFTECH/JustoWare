from django.db import models
from oficinas_app.models import OFICINAS,OPC_BOOL
# Create your models here.
class cierre_mes(models.Model):
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null = True,blank = True)
    protegido = models.CharField(max_length=1, choices=OPC_BOOL)
    tot_deb = models.FloatField(null = True,blank = True)
    tot_cre = models.FloatField(null = True,blank = True)
    fec_cie = models.DateTimeField(null = True,blank = True)
    usuario = models.CharField(max_length=16, null=False)
    class Meta:
        unique_together = [['oficina','fecha']]
        db_table = 'cierre_mes'

    def __str__(self):
        return self.oficina+' '+self.fecha