from django.db import models
from oficinas_app.models import OFICINAS
from justo_app.opciones import OPC_BOOL
# Create your models here.

class USUARIOS(models.Model):
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True)
    login = models.CharField(max_length=16, null=False)
    nit = models.CharField(max_length=12, null=True)
    nombre = models.CharField(max_length=44, null=True)
    fec_ing = models.DateField(null=True, blank=True)
    es_cajero = models.CharField(max_length=1, choices=OPC_BOOL)
    cod_caj = models.CharField(max_length=2, null=True)
    fec_sal = models.DateField(null=True, blank=True)
    cta_con_acr = models.CharField(max_length=10, null=True)
    activo = models.CharField(max_length=1, choices=OPC_BOOL)

    class Meta:
        unique_together = [['oficina', 'login']]
        db_table = 'usuarios'

    def __str__(self):
        return self.login