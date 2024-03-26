from django.db import models
from clientes_app.models import CLIENTES
from justo_app.opciones import OPC_CRE_CATEGORIA
# Create your models here.
class IMP_CON_CRE_INT(models.Model):
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    cod_imp = models.CharField(max_length=2, null=True)
    categoria = models.CharField(max_length=1, choices=OPC_CRE_CATEGORIA)
    kcta_con = models.CharField(max_length=10, null=True)
    kcta_pro_ind = models.CharField(max_length=10, null=True)
    kporcentaje = models.FloatField(null=True, blank=True)
    cta_int = models.CharField(max_length=10, null=True)
    cta_ord_int = models.CharField(max_length=10, null=True)

    class Meta:
        unique_together = [['cliente', 'cod_imp', 'categoria']]
        db_table = 'imp_con_cre_int'

    def __str__(self):
        return self.cliente+' '+self.categoria