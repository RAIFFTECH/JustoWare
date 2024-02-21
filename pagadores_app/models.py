from django.db import models
from clientes_app.models import CLIENTES
from localidades_app.models import LOCALIDADES
# Create your models here.

class PAGADORES(models.Model):
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE, verbose_name="Cliente",null=True)
    codigo = models.CharField(max_length=5,verbose_name="Código",null = True)
    nombre = models.CharField(max_length=40,verbose_name="Nombre", null=False)
    ciudad = models.ForeignKey(LOCALIDADES, on_delete=models.CASCADE, verbose_name="Ciudad",null=True)
    pagador = models.CharField(max_length=72, verbose_name="Pagador", null=True)
    tel_cel = models.CharField(max_length=10, verbose_name="Teléfono Celular", null=True)

    class Meta:
        unique_together = [['cliente','codigo']]
        db_table = 'pagadores'

    def __str__(self):
        return self.codigo + ' ' + self.nombre
