from django.db import models
from clientes_app.models import CLIENTES
# Create your models here.

class IMP_CON_CRE(models.Model):
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    cod_imp = models.CharField(max_length=2, null=True)
    descripcion = models.CharField(max_length=40, null=True)
    kcta_pte_cap = models.CharField(max_length=10, null=True)
    kcta_pro_gen_adi = models.CharField(max_length=10, null=True)
    kcta_pro_gen = models.CharField(max_length=10, null=True)
    kcta_gas_pro_gen = models.CharField(max_length=10, null=True)
    kcta_rec_pro_gen = models.CharField(max_length=10, null=True)
    kcta_gas_pro_ind = models.CharField(max_length=10, null=True)
    kcta_rec_pro_ind = models.CharField(max_length=10, null=True)
    icta_des_int_pp = models.CharField(max_length=10, null=True)
    kcta_pte_int = models.CharField(max_length=10, null=True)
    cta_val = models.CharField(max_length=10, null=True)
    kcta_ingreso = models.CharField(max_length=10, null=True)
    orden_i = models.CharField(max_length=10, null=True)

    class Meta:
        unique_together = [['cliente', 'cod_imp']]
        db_table = 'imp_con_cre'

    def __str__(self):
        return self.cliente+' '+self.descripcion
