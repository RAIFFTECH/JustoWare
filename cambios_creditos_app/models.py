from django.db import models
from detalle_producto_app.models import DETALLE_PROD
from justo_app.opciones import OPC_CAMBIOS_CRE
# Create your models here.

class CAMBIOS_CRE(models.Model):
    det_pro = models.ForeignKey(DETALLE_PROD, on_delete=models.PROTECT,null=False,default = None, verbose_name='Detalle Producto')
    tip_cam = models.CharField(max_length=1,null = True,choices=OPC_CAMBIOS_CRE, verbose_name='Tipo de Cambio?')
    capital = models.FloatField(null=True,blank=True, verbose_name='Capital')
    int_cor = models.FloatField(null=True,blank=True, verbose_name='Interés Corriente')
    int_mor = models.FloatField(null=True,blank=True, verbose_name='Interés de Mora')
    pol_seg = models.FloatField(null=True,blank=True, verbose_name='Póliza')
    des_pp = models.FloatField(null=True,blank=True, verbose_name='Descuento Pronto Pago')
    acreedor = models.FloatField(null=True,blank=True, verbose_name='Acreedor')
    class Meta:
        unique_together = [['det_pro','tip_cam']]
        db_table = 'cambios_cre'    

    def __str__(self):
        return self.det_pro+' '+self.tip_cam