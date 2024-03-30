from django.db import models
from oficinas_app.models import OFICINAS
from justo_app.opciones import OPC_BOOL
# Create your models here.

class USUARIOS(models.Model):
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True, verbose_name='Oficina')
    login = models.CharField(max_length=16, null=False, verbose_name='Nombre Usuario')
    nit = models.CharField(max_length=12, null=True, verbose_name='Identificación')
    nombre = models.CharField(max_length=44, null=True, verbose_name='Nombre Completo')
    fec_ing = models.DateField(null=True, blank=True, verbose_name='Fecha Ingreso')
    es_cajero = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Es Cajero?')
    cod_caj = models.CharField(max_length=2, null=True, verbose_name='Código Cajero')
    fec_sal = models.DateField(null=True, blank=True, verbose_name='Fecha Saldo')
    cta_con_acr = models.CharField(max_length=10, null=True, verbose_name='Cuenta Contable')
    activo = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Está Activo?')

    class Meta:
        unique_together = [['oficina', 'login']]
        db_table = 'usuarios'

    def __str__(self):
        return self.login