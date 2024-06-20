from django.db import models
from clientes_app.models import CLIENTES
from justo_app.models import DefaultToZeroMixin
from justo_app.opciones import OPC_BOOL
from terceros_app.models import TERCEROS

# Create your models here.
class ESTADOS_FIN(DefaultToZeroMixin):
    cliente = models.ForeignKey(CLIENTES, on_delete=models.PROTECT, null=False, verbose_name='Cliente')
    tercero = models.ForeignKey(TERCEROS, on_delete=models.PROTECT, null=True, verbose_name='Tercero')
    fec_inf = models.DateField(null=True, blank=True, verbose_name='Fecha Información')
    ing_sal_fij = models.FloatField(blank=True, null=True, verbose_name='Ingresos por Salario Fijo')
    ing_hon = models.FloatField(blank=True, null=True, verbose_name='Ingresos por Honorarios')
    ing_pen = models.FloatField(blank=True, null=True, verbose_name='Ingresos por Pensión')
    ing_arr = models.FloatField(blank=True, null=True, verbose_name='Ingresos por Arrendamientos')
    ing_com = models.FloatField(blank=True, null=True, verbose_name='Ingresos por Comisiones')
    ing_ext = models.FloatField(blank=True, null=True, verbose_name='Ingresos Extraordinarios')
    ing_otr = models.CharField(max_length=1, choices=OPC_BOOL,null=True, verbose_name='Otros Ingresos')
    ing_tot = models.FloatField(blank=True, null=True, verbose_name='Total Ingresos')
    egr_sec_fin = models.FloatField(blank=True, null=True, verbose_name='Egresos Sector Financiero')
    egr_cuo_hip = models.FloatField(blank=True, null=True, verbose_name='Egresos Cuota Hipotecaria')
    egr_des_nom = models.CharField(max_length=1, choices=OPC_BOOL, null=True, verbose_name='Egresos Descuentos Nómina')
    egr_gas_fam = models.FloatField(blank=True, null=True, verbose_name='Egresos Gastos Familiares')
    egr_otr_cre = models.FloatField(blank=True, null=True, verbose_name='Egresos Otros Créditos')
    egr_arr = models.FloatField(blank=True, null=True, verbose_name='Egresos por Arriendo')
    egr_otr_gas = models.FloatField(blank=True, null=True, verbose_name='Egresos Otros Gastos')
    egr_tot = models.FloatField(blank=True, null=True, verbose_name='Total Egresos')
    act_otr_egr = models.FloatField(blank=True, null=True, verbose_name='Actividad Otros Egresos')
    act_tip_bien = models.CharField(max_length=20, null=True, verbose_name='Activos Tipo de Bien')
    act_vei = models.FloatField(blank=True, null=True, verbose_name='Activos Vehículo')
    act_otr = models.CharField(max_length=1, choices=OPC_BOOL, null=True, verbose_name='Otros Activos')
    tot_act = models.FloatField(blank=True, null=True, verbose_name='Total Activos')
    act_fin_rai = models.FloatField(blank=True, null=True, verbose_name='Activos Finca Raíz')
    act_inv = models.FloatField(blank=True, null=True, verbose_name='Activos Inversiones')
    escritura = models.CharField(max_length=20,null = True, verbose_name='Matrícula Escritura')
    pas_otr = models.CharField(max_length=1, choices=OPC_BOOL,null=True, verbose_name='Otros Pasivos')
    pas_tip = models.CharField(max_length=24,null = True, verbose_name='Pasivo Tipo')
    tot_pat = models.FloatField(blank=True, null=True, verbose_name='Total Patrimonio')
    pas_val = models.FloatField(blank=True, null=True, verbose_name='Valor Pasivos')
    tot_pas = models.FloatField(blank=True, null=True, verbose_name='Total Pasivos')
    pas_des = models.CharField(max_length=40,null = True, verbose_name='Pasivos Descuentos')
    dec_ren = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Declara Renta?')
    tip_pas = models.CharField(max_length=40, null=True, verbose_name='Tipo Pasivo')
    des_pas = models.CharField(max_length=40, null=True, verbose_name='Descripción Pasivo')
    val_pas = models.FloatField(blank=True, null=True, verbose_name='Valor Pasivo')
    ope_mon_ext = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Oper. Moneda Extranjera?')
    nom_ban_ext = models.CharField(max_length=40,null = True, verbose_name='Nombre Banco Extranjero')
    ope_pais_ext = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Oper. País Extranjero?')
    ope_monto_ext = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Oper. Monto Extranjero?')
    num_cta_ext = models.CharField(max_length=20,null = True, verbose_name='Núm. Cuenta Extranjero')
    tip_ope_ext = models.CharField(max_length=20,null = True, verbose_name='Tipo Oper. Extranjero')
    mon_ope_ext = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Monto Oper. Extranjera?')
    prod_mon_ext = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Producto Moneda Extranjera?')
    des_prod_ext = models.CharField(max_length=40,null = True, verbose_name='Descripción Producto Extranjero')
    mon_prod_ext = models.CharField(max_length=20,null = True, verbose_name='Monto Producto Extranjero')
    pais_prod_ext = models.CharField(max_length=20,null = True, verbose_name='País Producto Extranjero')
    ciu_prod_ext = models.CharField(max_length=20,null = True, verbose_name='Ciudad Producto Extranjero')
    prom_prod_ext = models.FloatField(blank=True, null=True, verbose_name='Promedio producto Extranjero')
    
    class Meta:
        unique_together = [['cliente','tercero','fec_inf']]
        db_table = 'estados_fin'
    
    def __str__(self):
        return self.tercero
