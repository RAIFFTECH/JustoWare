from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
import re
from django.core.exceptions import ValidationError
from justo_app.opciones import CLASE_COOP, OPC_BOOL, OPC_CAMBIOS_CRE, OPC_CANALES, OPC_CLASEDOC,OPC_CRE_CATEGORIA,OPC_CRE_EST_JUR,OPC_CRE_FOR_PAG,OPC_CRE_TERMINO,OPC_EDUCACION,OPC_EST_CIV,OPC_EST_CRE,OPC_EST_CTA_AHO,OPC_ESTADO_ANTEIA,OPC_GARANTIA,OPC_LIQ_INT_AHO,OPC_MODALIDAD_CRE,OPC_NAT,OPC_NOV_CTA_AHO,OPC_PARENTESCO,OPC_PER_LIQ_INT,OPC_PRODUCTO,OPC_REFERENCIAS,OPC_REGIMEN,OPC_SEXO,OPC_TERMINO,OPC_TIP_CTA,OPC_TIP_MOV_AHO,OPC_TIPTER 

class DefaultToZeroMixin(models.Model):
    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if (isinstance(field, models.IntegerField) or isinstance(field, models.FloatField)) and field.attname != 'id':
                if getattr(self, field.name) is None or getattr(self, field.name) == '':
                    setattr(self, field.name, 0)

        super(DefaultToZeroMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True

def validate_numeric(value):
    if not re.match(r'^[0-9]+$', value):
        raise ValidationError(
            'El número de celular debe contener solo dígitos numéricos.')

# OPC_BOOL = [('S', 'Si'), ('N', 'No')]

# CLASE_COOP = (
#     ('AS', 'Asociaciones Mutuales'),
#     ('TA', 'Trabajo Asociado'),
#     ('EAYC', 'Especializada de Ahorro Y Credito'),
#     ('ESSA', 'Especializada sin Seccion de Ahorro'),
#     ('FE', 'Fondo de Empleados'),
#     ('ISSA', 'Integral Sin Seccion de Ahorro'),
#     ('MASSA', 'Multi Activa Sin Seccion de Ahorros'),
# )

# OPC_CLASEDOC = (
#     ('C', 'Cédula de Ciudadanía'),
#     ('T', 'Tarjeta de Identidad'),
#     ('N', 'Nit'),
#     ('R', 'Registro Civil'),
#     ('E', 'Cédula de Extranjería'),
#     ('P', 'Pasaporte'),
#     ('O', 'Otros'),
# )

# OPC_REGIMEN = (
#     ('48', 'Responsable'),
#     ('49', 'No Responsable'),
#     ('Comun', 'Comun'),
# )

# OPC_TIPTER = (
#     ('N', 'Persona Natural'),
#     ('J', 'Persona Jurídica'),
#     ('O', 'Otro'),
# )

# OPC_EST_CIV = (
#     ('N', 'No Aplica'),
#     ('S', 'Soltero'),
#     ('C', 'Casado'),
#     ('U', 'Union Libre'),
#     ('V', 'Viudo'),
#     ('E', 'Separado'),
#     ('D', 'Divorciado'),
# )

# OPC_PRODUCTO = (
#     ('AP', 'Aportes'),
#     ('AH', 'Ahorros'),
#     ('CR', 'Creditos'),
#     ('CC', 'Cuenta por Cobrar'),
#     ('CP', 'Cuenta por Pagar'),
#     ('CO', 'Contable'),
#     ('BA', 'Bancos'),
# )

# OPC_EDUCACION = (
#     ('0', 'No Aplica'),
#     ('1', 'Primaria'),
#     ('2', 'Bachiller'),
#     ('3', 'Tecnico'),
#     ('4', 'Tecnologo'),
#     ('5', 'Profesional'),
#     ('6', 'PosGrado'),
#     ('7', 'Maestria'),
#     ('8', 'Doctorado'),
#     ('9', 'Otros'),
# )

# OPC_PARENTESCO = (
#     ('0', 'No Aplica'),
#     ('1', 'Esposo(a)'),
#     ('2', 'Hijo(a)'),
#     ('3', 'Padre o Madre'),
#     ('4', 'Abuelo(a)'),
#     ('5', 'Nieto'),
#     ('6', 'Hermano'),
#     ('7', 'Hermana'),
#     ('8', 'Primo(a)'),
#     ('9', 'Otro Familiar'),
# )

# OPC_REFERENCIAS = (
#     ('0', 'No Aplica'),
#     ('1', 'Familiar'),
#     ('2', 'Personal'),
#     ('3', 'Bancaria'),
#     ('4', 'Comercial'),
#     ('5', 'Laboral'),
# )

# OPC_CANALES = (
#     ('ATM', 'Red de Cajeros'),
#     ('POS', 'Compras en Comercios'),
#     ('IVR', 'Audio Respuesta'),
#     ('TRA', 'Transferencia'),
#     ('CON', 'Consignacion'),
#     ('EFE', 'Efectivo'),
#     ('CHE', 'Cheque'),
#     ('GIR', 'Giro'),
#     ('WEB', 'Portal Transaccional'),
#     ('MOV', 'Banca Móvil'),
#     ('OFI', 'Oficina'),
#     ('CNB', 'Corresponsales Bancarios'),
#     ('RAL', 'Redes Aliadas')
# )

# OPC_NAT = (
#     ('D', 'Débito'),
#     ('C', 'Crédito'),
# )

# OPC_TERMINO = (
#     ('D', 'Definido'),
#     ('I', 'Indefinido'),
# )

# OPC_PER_LIQ_INT = (
#     ('D', 'Diario'),
#     ('M', 'Mensual'),
#     ('C', 'Cdat'),
#     ('V', 'Vencimiento'),
# )

# OPC_EST_CTA_AHO = (
#     ('A', 'Activa'),
#     ('I', 'Inactiva'),
#     ('C', 'Cancelada'),
#     ('E', 'Embargada'),
# )

# OPC_SEXO = (
#     ('M', 'Masculino'),
#     ('F', 'Femenino'),
#     ('N', 'No Aplica')
# )

# OPC_LIQ_INT_AHO = (
#     ('C', 'Causación Final'),
#     ('D', 'Causación Diaria'),
#     ('M', 'Causación Mensual'),
#     ('V', 'Causación Vencimiento'),
#     ('P', 'Pago'),
# )

# OPC_CRE_TERMINO = (
#     ('D', 'Definido'),
#     ('C', 'Cupo'),
#     ('R', 'Rotativo'),
# )

# OPC_CRE_FOR_PAG = (
#     ('P', 'Personal'),
#     ('L', 'Libranza'),
#     ('T', 'Transferencia'),
# )

# OPC_CRE_EST_JUR = (
#     ('N', 'Normal'),
#     ('P', 'Persuasivo'),
#     ('J', 'Cobro Jurídico'),
#     ('C', 'Condonación'),
#     ('T', 'Castigado'),
# )

# OPC_CAMBIOS_CRE = (
#     ('2', 'Ajuste'),
#     ('3', 'Des Pronto Pago'),
#     ('4', 'Castigo/Condo'),
# )

# OPC_CRE_CATEGORIA = (
#     ('A', 'Normal'),
#     ('B', 'Apreciable'),
#     ('C', 'En Peligro'),
#     ('D', 'En Mora'),
#     ('E', 'Irrecuperable'),
#     ('F', 'Castigado'),
# )

# OPC_EST_CRE = (
#     ('X', 'Por Causar'),
#     ('A', 'Activo'),
#     ('C', 'Cancelado'),
#     ('T', 'Terminado Cupo'),
# )

# OPC_MODALIDAD_CRE = (
#     ('CCCL', 'Consumo Con Libranza'),
#     ('CCSL', 'Consumo sin Libranza'),
#     ('CCPJ', 'Comercial Juridica'),
#     ('CCPN', 'Comercial Natural'),
#     ('CMIC', 'MicroCredito'),
# )

# OPC_GARANTIA = (
#     ('1', 'No Idonea'),
#     ('2', 'Hipotecaria'),
#     ('15', 'Sin Garantias'),
# )

# OPC_ESTADO_ANTEIA = (
#     ('0', 'No Anteia'),
#     ('1', 'Validar'),
#     ('2', 'Por Validar'),
#     ('3', 'Denegar')
# )

# OPC_EST_CTA_AHO = (
#     ('A', 'Activa'),
#     ('C', 'Cancelada'),
#     ('E', 'Embargada'),
# )

# OPC_NOV_CTA_AHO = (
#     ('A', 'Activada'),
#     ('I', 'Inactivada'),
#     ('C', 'Cancelada'),
#     ('E', 'Embargada'),
#     ('S', 'Inrtervenida'),
# )

# OPC_TIP_MOV_AHO = (
#     ('SalIni', 'Saldo Inicial Justo'),
#     ('Deposi', 'Deposito'),
#     ('IntCta', 'Interes Cuenta'),
#     ('IntCda', 'Interes Cdat'),
#     ('Canje', 'Canje X Confirmar'),
#     ('Can_OK', 'Canje Confirmado'),
#     ('Retiro', 'Retiro'),
#     ('RetFue', 'Rete Fuente'),
#     ('RF_CDA', 'Rete Fuente Cdat'),
#     ('CH_DEV', 'Cheque Devuelto'),
# )


# class XDOC_ZEP(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     per_con = models.IntegerField()
#     clase_zep = models.CharField(max_length=1, null=False)
#     doc_ds = models.IntegerField(null=True)
#     nombre = models.CharField(max_length=16, null=False, blank=True)
#     descripcion = models.CharField(max_length=36, null=False, blank=True)

#     class Meta:
#         unique_together = [['per_con', 'clase_zep']]
#         db_table = 'xdoc_zep'


# class XMOV_CRE(models.Model):
#     id = models.AutoField(primary_key=True)
#     cod_cre = models.CharField(max_length=10, null=False)
#     est_jur = models.CharField(max_length=1, null=False)
#     fec_ulp_pag = models.DateField(null=True)
#     min_fecha = models.DateField(null=True)
#     max_fecha = models.DateField(null=True)
#     clase = models.CharField(max_length=1, null=False)
#     docto = models.CharField(max_length=10, null=False)
#     tip_mov = models.CharField(max_length=1, null=False)
#     fecha = models.DateField(null=True)
#     capital = models.FloatField(null=True)
#     int_cor = models.FloatField(null=True)
#     int_mor = models.FloatField(null=True)
#     acreed = models.FloatField(null=True)
#     estado = models.CharField(max_length=1, null=False)

#     class Meta:
#         indexes = [
#             models.Index(fields=['tip_mov']),
#         ]
#         db_table = 'xmov_cre'


# class CLIENTES(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     codigo = models.CharField(max_length=1, null=False)
#     doc_ide = models.CharField(max_length=12,
#                                validators=[validate_numeric],
#                                help_text='el documento de identidad debe ser numerico.',
#                                null=True
#                                )
#     sigla = models.CharField(max_length=36)
#     nombre = models.CharField(max_length=120)
#     clase_coop = models.CharField(
#         max_length=8, choices=CLASE_COOP, default='EAYC')
#     celular = models.CharField(
#         max_length=10,
#         validators=[validate_numeric],
#         help_text='El número de celular debe contener exactamente 10 dígitos numéricos.',
#         null=True
#     )
#     email = models.EmailField()
#     dominio = models.URLField()

#     class Meta:
#         unique_together = [['codigo']]
#         db_table = 'clientes'


# class OFICINAS(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     codigo = models.CharField(max_length=5, null=False)

#     @property
#     def CodigoCliente(self):
#        return self.Codigo[0]
#     contabiliza = models.CharField(max_length=1, choices=OPC_BOOL)
#     nombre_oficina = models.TextField()
#     responsable = models.TextField()
#     celular = models.CharField(
#         max_length=10,
#         validators=[validate_numeric],
#         help_text='El número de celular debe contener exactamente 10 dígitos numéricos.',
#         null=True
#     )
#     email = models.EmailField()

#     class Meta:
#         unique_together = [['cliente', 'codigo']]
#         db_table = 'oficinas'


# class USUARIOS(models.Model):
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True)
#     id = models.SmallAutoField(primary_key=True)
#     login = models.CharField(max_length=16, null=False)
#     nit = models.CharField(max_length=12, null=True)
#     nombre = models.CharField(max_length=44, null=True)
#     fec_ing = models.DateField(null=True, blank=True)
#     es_cajero = models.CharField(max_length=1, choices=OPC_BOOL)
#     cod_caj = models.CharField(max_length=2, null=True)
#     fec_sal = models.DateField(null=True, blank=True)
#     cta_con_acr = models.CharField(max_length=10, null=True)
#     activo = models.CharField(max_length=1, choices=OPC_BOOL)

#     class Meta:
#         unique_together = [['oficina', 'login']]
#         db_table = 'usuarios'


# class MOV_CAJA(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True)
#     fecha = models.DateField(null=True, blank=True)
#     cod_caj = models.CharField(max_length=2, null=False)
#     jornada = models.CharField(max_length=1, null=False)
#     saldo_ini = models.FloatField(null=True, blank=True)
#     debitos = models.FloatField(null=True, blank=True)
#     creditos = models.FloatField(null=True, blank=True)
#     val_che_dev = models.FloatField(null=True, blank=True)
#     saldo_fin = models.FloatField(null=True, blank=True)
#     diferencia = models.FloatField(null=True, blank=True)
#     val_cheques = models.FloatField(null=True, blank=True)
#     val_vales = models.FloatField(null=True, blank=True)
#     cerrado = models.CharField(max_length=1, null=False, choices=OPC_BOOL)
#     monedas = models.JSONField(null=True, blank=True)

#     class Meta:
#         unique_together = [['oficina', 'fecha', 'cod_caj', 'jornada']]
#         db_table = 'mov_caja'


# class cierre_mes(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True)
#     fecha = models.DateField(null=True, blank=True)
#     protegido = models.CharField(max_length=1, choices=OPC_BOOL)
#     tot_deb = models.FloatField(null=True, blank=True)
#     tot_cre = models.FloatField(null=True, blank=True)
#     fec_cie = models.DateTimeField(null=True, blank=True)
#     usuario = models.CharField(max_length=16, null=False)

#     class Meta:
#         unique_together = [['oficina', 'fecha']]
#         db_table = 'cierre_mes'


# class CONCEPTOS(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE, null=True)
#     cod_con = models.CharField(max_length=8, null=False)
#     con_justo = models.CharField(max_length=1, choices=OPC_BOOL)
#     descripcion = models.CharField(max_length=44, null=False)
#     tip_dev_ap = models.CharField(max_length=1, choices=OPC_BOOL)
#     tip_con = models.CharField(max_length=1, choices=OPC_BOOL)
#     tip_sis = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_con = models.CharField(max_length=10, null=False)
#     cta_con_pas = models.CharField(max_length=10, null=False)
#     debito = models.CharField(max_length=1, choices=OPC_BOOL)
#     credito = models.CharField(max_length=1, choices=OPC_BOOL)
#     por_tercero = models.CharField(max_length=1, choices=OPC_BOOL)
#     por_ret_fue = models.FloatField(null=True, blank=True)

#     class Meta:
#         unique_together = [['cliente', 'cod_con']]
#         db_table = 'conceptos'


# class LOCALIDADES(models.Model):
#     # id = models.AutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     codigo = models.CharField(max_length=8, null=False)
#     nombre = models.CharField(max_length=36, null=False)
#     cod_pos = models.CharField(max_length=12, null=True)
#     departamento = models.CharField(max_length=36, null=True)

#     class Meta:
#         unique_together = [['cliente', 'codigo']]
#         db_table = 'localidades'


# class TERCEROS(models.Model):
#     id = models.AutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     cla_doc = models.CharField(max_length=1, choices=OPC_CLASEDOC)
#     doc_ide = models.CharField(max_length=12, null=False)
#     dig_ver = models.CharField(max_length=1, null=True)
#     nit_rap = models.CharField(max_length=12, null=True)
#     cod_ciu_exp = models.ForeignKey(
#         LOCALIDADES, on_delete=models.CASCADE, related_name='ciu_exp', null=True, blank=True)
#     cod_ciu_res = models.ForeignKey(
#         LOCALIDADES, on_delete=models.CASCADE, related_name='ciu_res', null=True, blank=True)
#     regimen = models.CharField(max_length=12, choices=OPC_REGIMEN)
#     fec_exp_ced = models.DateField(null=True, blank=True)
#     tip_ter = models.CharField(max_length=12, choices=OPC_TIPTER)
#     pri_ape = models.CharField(max_length=28, null=True)
#     seg_ape = models.CharField(max_length=28, null=True)
#     pri_nom = models.CharField(max_length=28, null=True)
#     seg_nom = models.CharField(max_length=28, null=True)
#     raz_soc = models.CharField(max_length=120, null=True)
#     direccion = models.CharField(max_length=80, null=True)
#     cod_pos = models.CharField(max_length=8, null=True)
#     tel_ofi = models.CharField(max_length=10, null=True)
#     tel_res = models.CharField(max_length=10, null=True)
#     id_ds = models.BigIntegerField(null=True, db_index=True)
#     celular1 = models.CharField(
#         max_length=10,
#         validators=[validate_numeric],
#         help_text='El número de celular debe contener exactamente 10 dígitos numéricos.',
#         null=True
#     )
#     celular2 = models.CharField(max_length=10, null=True)
#     fax = models.CharField(max_length=10, null=True)
#     email = models.EmailField()
#     nombre = models.CharField(max_length=120, blank=True, null=True)
#     fec_act = models.DateField(null=True, blank=True)
#     observacion = models.CharField(max_length=255, null=True)
#     per_pub_exp = models.CharField(max_length=1, choices=OPC_BOOL)
#     nit_interno = models.CharField(max_length=1, choices=OPC_BOOL)

#     def save(self, *args, **kwargs):
#         if self.tip_ter == "N":
#             self.nombre = """%s %s %s %s""" % (
#                 self.pri_ape, self.seg_ape, self.pri_nom, self.seg_nom)
#         else:
#             self.nombre = self.raz_soc
#         super().save(*args, **kwargs)

#     class Meta:
#         unique_together = [['cliente', 'cla_doc', 'doc_ide']]
#         db_table = 'terceros'


# class estados_fin(DefaultToZeroMixin):
#     id = models.AutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE, null=False)
#     tercero = models.ForeignKey(TERCEROS, on_delete=models.CASCADE, null=True)
#     fec_inf = models.DateField(null=True, blank=True)
#     ing_sal_fij = models.FloatField(blank=True, null=True)
#     ing_hon = models.FloatField(blank=True, null=True)
#     ing_pen = models.FloatField(blank=True, null=True)
#     ing_arr = models.FloatField(blank=True, null=True)
#     ing_com = models.FloatField(blank=True, null=True)
#     ing_ext = models.FloatField(blank=True, null=True)
#     ing_otr = models.CharField(max_length=1, choices=OPC_BOOL, null=True)
#     ing_tot = models.FloatField(blank=True, null=True)
#     egr_sec_fin = models.FloatField(blank=True, null=True)
#     egr_cuo_hip = models.FloatField(blank=True, null=True)
#     egr_des_nom = models.CharField(max_length=1, choices=OPC_BOOL, null=True)
#     egr_gas_fam = models.FloatField(blank=True, null=True)
#     egr_otr_cre = models.FloatField(blank=True, null=True)
#     egr_arr = models.FloatField(blank=True, null=True)
#     egr_otr_gas = models.FloatField(blank=True, null=True)
#     egr_tot = models.FloatField(blank=True, null=True)
#     act_otr_egr = models.FloatField(blank=True, null=True)
#     act_tip_bien = models.CharField(max_length=20, null=True)
#     act_vei = models.FloatField(blank=True, null=True)
#     act_otr = models.CharField(max_length=1, choices=OPC_BOOL, null=True)
#     tot_act = models.FloatField(blank=True, null=True)
#     act_fin_rai = models.FloatField(blank=True, null=True)
#     act_inv = models.FloatField(blank=True, null=True)
#     escritura = models.CharField(max_length=20, null=True)
#     pas_otr = models.CharField(max_length=1, choices=OPC_BOOL, null=True)
#     pas_tip = models.CharField(max_length=24, null=True)
#     tot_pat = models.FloatField(blank=True, null=True)
#     pas_val = models.FloatField(blank=True, null=True)
#     tot_pas = models.FloatField(blank=True, null=True)
#     pas_des = models.CharField(max_length=40, null=True)
#     dec_ren = models.CharField(max_length=1, choices=OPC_BOOL)
#     tip_pas = models.CharField(max_length=40, null=True)
#     des_pas = models.CharField(max_length=40, null=True)
#     val_pas = models.FloatField(blank=True, null=True)
#     ope_mon_ext = models.CharField(max_length=1, choices=OPC_BOOL)
#     nom_ban_ext = models.CharField(max_length=40, null=True)
#     ope_pais_ext = models.CharField(max_length=1, choices=OPC_BOOL)
#     ope_monto_ext = models.CharField(max_length=1, choices=OPC_BOOL)
#     num_cta_ext = models.CharField(max_length=20, null=True)
#     tip_ope_ext = models.CharField(max_length=20, null=True)
#     mon_ope_ext = models.CharField(max_length=1, choices=OPC_BOOL)
#     prod_mon_ext = models.CharField(max_length=1, choices=OPC_BOOL)
#     des_prod_ext = models.CharField(max_length=40, null=True)
#     mon_prod_ext = models.CharField(max_length=20, null=True)
#     pais_prod_ext = models.CharField(max_length=20, null=True)
#     ciu_prod_ext = models.CharField(max_length=20, null=True)
#     prom_prod_ext = models.FloatField(blank=True, null=True)

#     class Meta:
#         unique_together = [['cliente', 'tercero', 'fec_inf']]
#         db_table = 'estados_fin'


# class pagadores(models.Model):
#     id = models.AutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE, null=True)
#     codigo = models.CharField(max_length=5, null=True)
#     nombre = models.CharField(max_length=40, null=False)
#     ciudad = models.CharField(max_length=36, null=True)
#     pagador = models.CharField(max_length=72, null=True)
#     tel_cel = models.CharField(max_length=10, null=True)

#     class Meta:
#         unique_together = [['cliente', 'codigo']]
#         db_table = 'pagadores'


# class ASOCIADOS(DefaultToZeroMixin):
#     id = models.AutoField(primary_key=True)
#     cod_aso = models.CharField(max_length=12, null=False)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True)
#     tercero = models.ForeignKey(TERCEROS, on_delete=models.CASCADE, null=True)
#     sexo = models.CharField(max_length=1, null=True, blank=True)
#     est_civ = models.CharField(max_length=1, choices=OPC_EST_CIV)
#     fec_nac = models.DateField(null=True, blank=True)
#     ciu_res = models.CharField(max_length=48, null=True, blank=True)
#     zona = models.CharField(max_length=16, null=True, blank=True)
#     profesion = models.CharField(max_length=48, null=True, blank=True)
#     ocupacion = models.CharField(max_length=40, null=True, blank=True)
#     ocupacion_cod = models.CharField(max_length=3, null=True, blank=True)
#     estrato = models.CharField(max_length=1, null=True, blank=True)
#     niv_est = models.CharField(max_length=1, choices=OPC_EDUCACION)
#     cab_fam = models.CharField(max_length=1, choices=OPC_BOOL)
#     id_pag = models.ForeignKey(pagadores, on_delete=models.CASCADE, null=True)
#     fec_afi = models.DateField(null=True, blank=True)
#     cargo_emp = models.CharField(max_length=36, null=True)
#     per_a_cargo = models.IntegerField(null=True, blank=True)
#     num_hij_men = models.IntegerField(blank=True, null=True)
#     num_hij_may = models.IntegerField(blank=True, null=True)
#     tip_viv = models.CharField(max_length=24, null=True)
#     tie_en_ciu = models.IntegerField(blank=True, null=True)
#     med_con = models.CharField(max_length=48, null=True)
#     fec_ing_tra = models.DateField(null=True, blank=True)
#     tel_tra = models.CharField(max_length=10, null=True)
#     tip_sal = models.CharField(max_length=18, null=True)
#     ciu_tra = models.CharField(max_length=30, null=True)
#     act_eco = models.CharField(max_length=24, null=True)
#     cod_ciiu = models.CharField(max_length=12, null=True)
#     tip_con = models.CharField(max_length=18, null=True)
#     nom_emp = models.CharField(max_length=40, null=True)
#     nit_emp = models.CharField(max_length=12, null=True)
#     dir_emp = models.CharField(max_length=50, null=True)
#     email_emp = models.EmailField(blank=True, null=True)
#     sector_emp = models.CharField(max_length=12, null=True)
#     empresa_ant = models.IntegerField(blank=True, null=True)
#     emp_num_emp = models.IntegerField(blank=True, null=True)
#     negocio_pro = models.CharField(max_length=1, choices=OPC_BOOL)
#     negocio_nom = models.CharField(max_length=48, null=True)
#     negocio_tel = models.CharField(max_length=10, null=True)
#     negocio_loc_pro = models.CharField(max_length=1, choices=OPC_BOOL)
#     negocio_cam_com = models.CharField(max_length=1, choices=OPC_BOOL)
#     negocio_ant = models.IntegerField(blank=True, null=True)
#     pension_ent = models.CharField(max_length=36, null=True)
#     pension_tie = models.IntegerField(blank=True, null=True)
#     pension_otr = models.CharField(max_length=1, choices=OPC_BOOL)
#     pension_ent_otr = models.CharField(max_length=36, null=True)
#     pep_es_fam = models.CharField(max_length=1, choices=OPC_BOOL)
#     pep_fam_par = models.CharField(max_length=1, choices=OPC_PARENTESCO)
#     pep_fam_nom = models.CharField(max_length=36, null=True)
#     pep_car_pub = models.CharField(max_length=1, choices=OPC_BOOL)
#     pep_cargo = models.CharField(max_length=36, null=True)
#     pep_eje_pod = models.CharField(max_length=1, choices=OPC_BOOL)
#     pep_adm_rec_est = models.CharField(max_length=1, choices=OPC_BOOL)
#     tie_gre_car = models.CharField(max_length=1, choices=OPC_BOOL)
#     recibe_pag_ext = models.CharField(max_length=1, choices=OPC_BOOL)
#     recide_ext_mas_186 = models.CharField(max_length=1, choices=OPC_BOOL)
#     recibe_ing_ext = models.CharField(max_length=1, choices=OPC_BOOL)
#     estado_anteia = models.CharField(
#         max_length=1, choices=OPC_ESTADO_ANTEIA, null=False, default=2)

#     class Meta:
#         unique_together = [['oficina', 'cod_aso']]
#         db_table = 'asociados'


# class ASO_BENEF(models.Model):
#     id = models.AutoField(primary_key=True)
#     asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
#     cla_doc = models.CharField(max_length=1, choices=OPC_CLASEDOC)
#     doc_ide = models.CharField(max_length=12, null=False)
#     nombre = models.CharField(max_length=64, null=False)
#     agno_nac = models.IntegerField(blank=True, null=True)
#     parentesco = models.CharField(max_length=1, choices=OPC_PARENTESCO)
#     porcentaje = models.FloatField(blank=True, null=True)

#     class Meta:
#         unique_together = [['asociado', 'doc_ide']]
#         db_table = 'aso_banef'


# class PLAN_APORTES(models.Model):
#     id = models.AutoField(primary_key=True)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
#     agno = models.IntegerField(blank=True, null=True)
#     meses = models.IntegerField(blank=True, null=True)
#     iniadu = models.FloatField(blank=True, null=True)
#     totadu = models.FloatField(blank=True, null=True)
#     inichi1 = models.FloatField(blank=True, null=True)
#     totchi1 = models.FloatField(blank=True, null=True)
#     inichi2 = models.FloatField(blank=True, null=True)
#     totchi2 = models.FloatField(blank=True, null=True)
#     inijur = models.FloatField(blank=True, null=True)
#     totjur = models.FloatField(blank=True, null=True)

#     class Meta:
#         unique_together = [['oficina', 'agno']]
#         db_table = 'plan_aportes'


# class ASO_REFERENCIAS(models.Model):
#     id = models.AutoField(primary_key=True)
#     asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
#     tipo_ref = models.CharField(max_length=1, choices=OPC_REFERENCIAS)
#     parentesco = models.CharField(max_length=1, choices=OPC_PARENTESCO)
#     nombre = models.CharField(max_length=64, null=False)
#     ocupacion = models.CharField(max_length=32, null=False)
#     empresa = models.CharField(max_length=40, null=False)
#     direccion = models.CharField(max_length=64, null=False)
#     tel_fijo = models.CharField(max_length=10, null=False)
#     tel_cel = models.CharField(max_length=10, null=False)
#     tel_emp = models.CharField(max_length=10, null=False)

#     class Meta:
#         unique_together = [['asociado', 'nombre']]
#         db_table = 'aso_referencias'


# class ORIGINACION(models.Model):
#     asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
#     lin_cre = models.CharField(max_length=80, null=False)
#     monto = models.FloatField(blank=True, null=True)
#     plazo = models.IntegerField(blank=True, null=True)
#     gar_cre_sol = models.CharField(max_length=1, null=False)
#     lin_cre_sol = models.CharField(max_length=1, null=False)
#     mod_cre_sol = models.CharField(max_length=1, null=False)

#     class Meta:
#         unique_together = [['asociado']]
#         db_table = 'originacion'


# class PLAN_CTAS(models.Model):
#     id = models.AutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     per_con = models.IntegerField(blank=True, null=True)
#     cod_cta = models.CharField(max_length=10, null=True)
#     nom_cta = models.CharField(max_length=64, null=True)
#     tip_cta = models.CharField(max_length=1, null=True)
#     dinamica = models.TextField()
#     naturaleza = models.CharField(max_length=1, choices=OPC_NAT)
#     activa = models.CharField(max_length=1, choices=OPC_BOOL)
#     por_tercero = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_act_fij = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_pre = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_bal = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_res = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_ord = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_ban = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_gan_per = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_per_gan = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_dep = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_ing_ret = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_ret_iva = models.CharField(max_length=1, choices=OPC_BOOL)
#     cta_rec = models.CharField(max_length=1, choices=OPC_BOOL)
#     id_ds = models.BigIntegerField(null=True, db_index=True)

#     class Meta:
#         unique_together = [['cliente', 'per_con', 'cod_cta']]
#         db_table = 'plan_ctas'


# class CENTROCOSTOS(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     codigo = models.CharField(max_length=5, null=False)

#     class Meta:
#         unique_together = [['cliente', 'codigo']]
#         db_table = 'centro_costos'


# class DOCTO_CONTA(models.Model):
#     id = models.AutoField(primary_key=True)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
#     per_con = models.IntegerField(blank=True, null=True)
#     codigo = models.IntegerField(blank=False, null=False)
#     nom_cto = models.CharField(max_length=12, null=False)
#     nombre = models.CharField(max_length=44, null=False)
#     doc_admin = models.CharField(
#         max_length=1, blank=True, null=True, choices=OPC_BOOL)
#     doc_caja = models.CharField(
#         max_length=1, blank=True, null=True, choices=OPC_BOOL)
#     inicio_nuevo_per = models.CharField(max_length=1, choices=OPC_BOOL)
#     consecutivo = models.IntegerField(blank=True, null=True)
#     id_ds = models.BigIntegerField(null=True, db_index=True)

#     class Meta:
#         unique_together = [['oficina', 'per_con', 'codigo']]
#         db_table = 'docto_conta'


# class HECHO_ECONO(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     docto_conta = models.ForeignKey(DOCTO_CONTA, on_delete=models.CASCADE)
#     numero = models.IntegerField(blank=True, null=True)
#     fecha = models.DateField(null=True, blank=True)
#     descripcion = models.CharField(max_length=64, null=True)
#     anulado = models.CharField(max_length=1, choices=OPC_BOOL)
#     protegido = models.CharField(max_length=1, choices=OPC_BOOL)
#     fecha_prot = models.DateTimeField(auto_now=True)
#     usuario = models.CharField(max_length=16, null=True)
#     canal = models.CharField(max_length=3, choices=OPC_CANALES)
#     id_ds = models.BigIntegerField(null=True, db_index=True)

#     class Meta:
#         unique_together = [['docto_conta', 'numero']]
#         db_table = 'hecho_econo'


# @receiver(post_save, sender=HECHO_ECONO)
# def asignar_numero_HECHO_ECONO(sender, instance, created, **kwargs):
#     if created and instance.numero is None:
#         ultimo_numero = HECHO_ECONO.objects.filter(
#             docto_conta=instance.docto_conta).order_by('-numero').first()
#         print(f"Ultimo número: {ultimo_numero}")
#         nuevo_numero = 1 if ultimo_numero.numero is None else ultimo_numero.numero + 1
#         instance.numero = nuevo_numero
#         instance.save()


# class DETALLE_PROD(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True)
#     hecho_econo = models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE)
#     centro_costo = models.ForeignKey(
#         CENTROCOSTOS, on_delete=models.CASCADE, null=True)
#     producto = models.CharField(max_length=2, choices=OPC_PRODUCTO)
#     subcuenta = models.CharField(max_length=12, null=True)
#     concepto = models.CharField(max_length=8, null=True)
#     valor = models.FloatField(null=True)
#     usuario = models.CharField(max_length=12, null=True)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(auto_now=True)

#     class Meta:
#         unique_together = [
#             ['hecho_econo', 'producto', 'subcuenta', 'concepto']]
#         indexes = [
#             models.Index(fields=['oficina', 'producto', 'subcuenta']),
#         ]
#         db_table = 'detalle_prod'


# class DETALLE_ECONO(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     hecho_econo = models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE)
#     detalle_prod = models.ForeignKey(
#         DETALLE_PROD, on_delete=models.CASCADE, null=True)
#     cuenta = models.ForeignKey(PLAN_CTAS, on_delete=models.CASCADE)
#     tercero = models.ForeignKey(TERCEROS, on_delete=models.CASCADE)
#     item_concepto = models.CharField(max_length=6, null=True)
#     detalle = models.TextField(null=True)
#     debito = models.FloatField(null=True)
#     credito = models.FloatField(null=True)
#     valor_1 = models.FloatField(null=True)
#     valor_2 = models.FloatField(null=True)
#     id_ds = models.BigIntegerField(null=True)

#     class Meta:
#         #    unique_together = [['hecho_econo','cuenta','tercero','detalle_prod']]
#         indexes = [
#             models.Index(fields=['hecho_econo', 'cuenta',
#                          'tercero', 'detalle_prod']),
#         ]
#         db_table = 'detalle_econo'


# class LINEAS_AHORRO(models.Model):
#     id = models.SmallAutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE, null=True)
#     cod_lin_aho = models.CharField(max_length=2, null=True)
#     nombre = models.CharField(max_length=30, null=True)
#     termino = models.CharField(max_length=1, choices=OPC_TERMINO)
#     per_liq_int = models.CharField(max_length=1, choices=OPC_PER_LIQ_INT)
#     cta_por_pas = models.CharField(max_length=10, null=True)
#     fec_ult_liq_int = models.DateField(null=True, blank=True)
#     saldo_minimo = models.FloatField(null=True, blank=True)

#     class Meta:
#         unique_together = [['cliente', 'cod_lin_aho']]
#         db_table = 'lineas_ahorro'


# class IMP_CON_LIN_AHO(models.Model):
#     id = models.AutoField(primary_key=True)
#     linea_ahorro = models.ForeignKey(
#         LINEAS_AHORRO, on_delete=models.CASCADE, null=True)
#     cod_imp = models.CharField(max_length=2, null=True)
#     descripcion = models.CharField(max_length=40, null=True)
#     ctaafeact = models.CharField(max_length=10, null=True)
#     ctaafeina = models.CharField(max_length=10, null=True)
#     ctaafeint = models.CharField(max_length=10, null=True)
#     ctaretfue = models.CharField(max_length=10, null=True)

#     class Meta:
#         unique_together = [['linea_ahorro', 'cod_imp']]
#         db_table = 'imp_con_lin_aho'


# class TAS_LIN_AHO(models.Model):
#     id = models.AutoField(primary_key=True)
#     lin_aho = models.ForeignKey(LINEAS_AHORRO, on_delete=models.CASCADE)
#     fecha_inicial = models.DateField(null=True, blank=True)
#     fecha_final = models.DateField(null=True, blank=True)
#     tiae = models.FloatField()

#     class Meta:
#         unique_together = [['lin_aho', 'fecha_inicial']]
#         db_table = 'tas_lin_aho'


# class RET_FUE_AHO(models.Model):
#     id = models.AutoField(primary_key=True)
#     lin_aho = models.ForeignKey(LINEAS_AHORRO, on_delete=models.CASCADE)
#     fecha_inicial = models.DateField(null=True, blank=True)
#     fecha_final = models.DateField(null=True, blank=True)
#     bas_liq_int = models.FloatField(null=True, blank=True)
#     tas_liq_rf = models.FloatField(null=True, blank=True)

#     class Meta:
#         unique_together = [['lin_aho', 'fecha_inicial']]
#         db_table = 'RET_FUE_AHO'


# class CTAS_AHORRO(models.Model):
#     id = models.AutoField(primary_key=True)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
#     lin_aho = models.ForeignKey(LINEAS_AHORRO, on_delete=models.CASCADE)
#     cod_imp = models.CharField(max_length=2, null=True)
#     asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
#     num_cta = models.CharField(max_length=10, null=True)
#     est_cta = models.CharField(max_length=1, choices=OPC_EST_CTA_AHO)
#     fec_apertura = models.DateField(null=True, blank=True)
#     fec_cancela = models.DateField(null=True, blank=True)
#     exc_tas_mil = models.CharField(max_length=1, choices=OPC_BOOL)
#     fec_ini_exc = models.DateField(null=True, blank=True)

#     class Meta:
#         unique_together = [['oficina', 'num_cta']]
#         db_table = 'ctas_ahorro'


# class CTA_AHO_EST_HIS(models.Model):
#     id = models.AutoField(primary_key=True)
#     cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
#     fecha = models.DateField(null=True, blank=True)
#     est_cta_ant = models.CharField(max_length=1, choices=OPC_EST_CTA_AHO)

#     class Meta:
#         unique_together = [['cta_aho', 'fecha']]
#         db_table = 'cta_aho_est_his'


# class CTA_CDAT(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
#     ampliacion = models.IntegerField()
#     valor = models.FloatField(null=True, blank=True)
#     fecha = models.DateField(null=True, blank=True)
#     plazo_mes = models.IntegerField(null=True, blank=True)
#     tiae = models.FloatField(null=True, blank=True)
#     Periodicidad = models.IntegerField(null=True, blank=True)
#     cta_int_ret = models.CharField(max_length=10, null=True)
#     aplicado = models.CharField(max_length=1, choices=OPC_BOOL)

#     class Meta:
#         unique_together = [['cta_aho', 'ampliacion']]
#         db_table = 'cta_cdat'


# class CTA_CDAT_AMP(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
#     cta_amp = models.ForeignKey(CTA_CDAT, on_delete=models.CASCADE)
#     fecha = models.DateField(null=True, blank=True)
#     num_liq = models.IntegerField(null=True, blank=True)
#     valor = models.FloatField(null=True, blank=True)
#     cta_aho_afe = models.CharField(max_length=10, null=True)
#     docto = models.ForeignKey(
#         HECHO_ECONO, on_delete=models.CASCADE, null=True, blank=True)
#     clase = models.CharField(max_length=1)
#     documento = models.CharField(max_length=10, null=True)
#     aplicado = models.CharField(max_length=1, choices=OPC_BOOL)

#     class Meta:
#         unique_together = [['cta_aho', 'cta_amp', 'fecha']]
#         indexes = [
#             models.Index(fields=['fecha']),
#         ]
#         db_table = 'cta_cdat_amp'


# class CTA_CDAT_LIQ(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
#     cta_amp = models.ForeignKey(CTA_CDAT_AMP, on_delete=models.CASCADE)
#     fecha = models.DateField(null=True, blank=True)
#     tip_liq = models.CharField(max_length=1, choices=OPC_LIQ_INT_AHO)
#     Val_int = models.FloatField(null=True, blank=True)
#     Val_ret = models.FloatField(null=True, blank=True)
#     Val_ret_nue = models.FloatField(null=True, blank=True)
#     aplicado = models.CharField(max_length=1, choices=OPC_BOOL)
#     docto = models.ForeignKey(
#         HECHO_ECONO, on_delete=models.CASCADE, null=True, blank=True)
#     aplicado = models.CharField(max_length=1, choices=OPC_BOOL)

#     class Meta:
#         unique_together = [['cta_aho', 'cta_amp', 'fecha', 'tip_liq']]
#         db_table = 'cta_cdat_liq'


# class LINEAS_CREDITO(models.Model):
#     id = models.AutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     cod_lin_cre = models.IntegerField()
#     descripcion = models.CharField(max_length=44, null=True)
#     tas_int_anu = models.FloatField(null=True)
#     tas_int_mor = models.FloatField(null=True)
#     por_pol = models.FloatField(null=True)
#     por_des_pp = models.FloatField(null=True)
#     dia_con_int_mor = models.IntegerField(null=True)

#     class Meta:
#         unique_together = [['cliente', 'cod_lin_cre']]
#         db_table = 'lineas_credito'


# class IMP_CON_CRE(models.Model):
#     id = models.AutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     cod_imp = models.CharField(max_length=2, null=True)
#     descripcion = models.CharField(max_length=40, null=True)
#     kpte_cap = models.CharField(max_length=10, null=True)
#     kdet_gen_adi = models.CharField(max_length=10, null=True)
#     kdet_gen = models.CharField(max_length=10, null=True)
#     kdet_gen_gas = models.CharField(max_length=10, null=True)
#     kdet_gen_rec = models.CharField(max_length=10, null=True)
#     kdet_ind_gas = models.CharField(max_length=10, null=True)
#     kdet_ind_rec = models.CharField(max_length=10, null=True)
#     kdpp_ic = models.CharField(max_length=10, null=True)
#     kpte_ic = models.CharField(max_length=10, null=True)
#     cta_val = models.CharField(max_length=10, null=True)
#     kcta_ingreso = models.CharField(max_length=10, null=True)
#     kic_orden_i = models.CharField(max_length=10, null=True)

#     class Meta:
#         unique_together = [['cliente', 'cod_imp']]
#         db_table = 'imp_con_cre'


# class IMP_CON_CRE_INT(models.Model):
#     id = models.AutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     cod_imp = models.CharField(max_length=2, null=True)
#     categoria = models.CharField(max_length=1, choices=OPC_CRE_CATEGORIA)
#     kcapital = models.CharField(max_length=10, null=True)
#     kdet_ind = models.CharField(max_length=10, null=True)
#     porcen_det = models.FloatField(null=True, blank=True)
#     kcxc_ic = models.CharField(max_length=10, null=True)
#     kord_ic = models.CharField(max_length=10, null=True)

#     class Meta:
#         unique_together = [['cliente', 'cod_imp', 'categoria']]
#         db_table = 'imp_con_cre_int'


# class CREDITOS(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
#     imputacion = models.ForeignKey(
#         IMP_CON_CRE, on_delete=models.CASCADE, null=True)
#     cod_lin_cre = models.IntegerField(null=True)
#     socio = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE, null=True)
#     com_des = models.ForeignKey(
#         DETALLE_PROD, on_delete=models.CASCADE, null=True)
#     cod_cre = models.CharField(max_length=10, null=True)
#     libranza = models.CharField(max_length=10, null=True)
#     pagare = models.CharField(max_length=16, null=True)
#     termino = models.CharField(max_length=1, choices=OPC_CRE_TERMINO)
#     for_pag = models.CharField(
#         max_length=1, choices=OPC_CRE_FOR_PAG, null=True)
#     tip_gar = models.CharField(
#         max_length=2, choices=OPC_GARANTIA, default='15')
#     cap_ini = models.FloatField(null=True, blank=True)
#     fec_des = models.DateField(null=True, blank=True)
#     fec_pag_ini = models.DateField(null=True, blank=True)
#     fec_ree = models.DateField(null=True, blank=True)
#     fec_ven = models.DateField(null=True, blank=True)
#     fec_ult_pag = models.DateField(null=True, blank=True)
#     val_cuo_ini = models.FloatField(null=True, blank=True)
#     val_cuo_act = models.FloatField(null=True, blank=True)
#     num_cuo_ini = models.IntegerField(null=True, blank=True)
#     num_cuo_act = models.IntegerField(null=True, blank=True)
#     num_cuo_gra = models.IntegerField(null=True, blank=True)
#     per_ano = models.IntegerField(null=True, blank=True)
#     tian_ic_ini = models.FloatField(null=True, blank=True)
#     tian_ic_act = models.FloatField(null=True, blank=True)
#     tian_im = models.FloatField(null=True, blank=True)
#     tian_pol_seg = models.FloatField(null=True, blank=True)
#     por_des_pro_pag = models.FloatField(null=True, blank=True)
#     decreciente = models.CharField(max_length=1, choices=OPC_BOOL)
#     estado = models.CharField(max_length=1, choices=OPC_EST_CRE)
#     est_jur = models.CharField(max_length=1, choices=OPC_CRE_EST_JUR)
#     cat_nue = models.CharField(max_length=1, choices=OPC_CRE_CATEGORIA)
#     rep_cen_rie = models.CharField(max_length=1, choices=OPC_BOOL)
#     val_gar_hip = models.FloatField(null=True, blank=True)
#     mat_inm_gar = models.CharField(max_length=12, null=True)
#     num_pol_gar_hip = models.CharField(max_length=16, null=True)
#     figarantias = models.CharField(max_length=1, choices=OPC_BOOL)

#     class Meta:
#         unique_together = [['oficina', 'cod_cre']]
#         db_table = 'creditos'


# class CAMBIOS_CRE(models.Model):
#     id = models.AutoField(primary_key=True)
#     det_pro = models.ForeignKey(
#         DETALLE_PROD, on_delete=models.CASCADE, null=False, default=None)
#     tip_cam = models.CharField(
#         max_length=1, null=True, choices=OPC_CAMBIOS_CRE)
#     fecha = models.DateField(null=True, blank=True)
#     capital = models.FloatField(null=True, blank=True)
#     int_cor = models.FloatField(null=True, blank=True)
#     int_mor = models.FloatField(null=True, blank=True)
#     pol_seg = models.FloatField(null=True, blank=True)
#     des_pp = models.FloatField(null=True, blank=True)
#     acreedor = models.FloatField(null=True, blank=True)

#     class Meta:
#         unique_together = [['det_pro', 'tip_cam']]
#         db_table = 'cambios_cre'


# class CREDITOS_CAUSA(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     oficina = models.ForeignKey(
#         OFICINAS, on_delete=models.CASCADE, default=None)
#     cod_cre = models.CharField(max_length=10, null=True)
#     comprobante = models.ForeignKey(
#         DETALLE_PROD, on_delete=models.CASCADE, null=True, default=None)
#     cuota = models.IntegerField(null=False, blank=False, default=0)
#     fecha = models.DateField(null=True, blank=True)
#     capital = models.FloatField(null=True, blank=True)
#     int_cor = models.FloatField(null=True, blank=True)

#     class Meta:
#         unique_together = [['oficina', 'cod_cre', 'comprobante', 'cuota']]
#         db_table = 'creditos_causa'


# class DESTINO_CRE(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     codigo = models.IntegerField()
#     descripcion = models.CharField(max_length=50, null=True)

#     class Meta:
#         unique_together = [['cliente', 'codigo']]
#         db_table = 'destino_cre'


# class CAT_DES_DIA_CRE(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     codigo = models.IntegerField()
#     categoria = models.CharField(
#         max_length=1, null=False, choices=OPC_CRE_CATEGORIA)
#     minimo_dias = models.IntegerField(null=True)
#     maximo_dias = models.IntegerField(null=True)

#     class Meta:
#         unique_together = [['cliente', 'codigo', 'categoria']]
#         db_table = 'cat_des_dia_cre'


# class GAR_NO_IDONEA(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
#     credito = models.ForeignKey(CREDITOS, on_delete=models.CASCADE)
#     tipo = models.CharField(max_length=1, null=False, default='C')
#     doc_ide = models.CharField(max_length=12, null=False, default='')

#     class Meta:
#         unique_together = [['oficina', 'credito', 'doc_ide']]
#         db_table = 'gar_no_idonea'


# class CARTE_CAT_HIS(models.Model):
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
#     credito = models.ForeignKey(CREDITOS, on_delete=models.CASCADE, null=True)
#     fecha = models.DateField(null=True, blank=True)
#     cod_cre = models.CharField(max_length=10, null=True)
#     nit = models.CharField(max_length=12, null=True)
#     cod_lin_cre = models.CharField(max_length=2, null=True)
#     cod_imp_con = models.CharField(max_length=2, null=True)
#     for_pag = models.CharField(max_length=1, null=True)
#     plazo = models.SmallIntegerField(null=True, default=0)
#     dias_mor = models.SmallIntegerField(null=True, default=0)
#     cap_ini = models.FloatField(null=True, blank=True, default=0.0)
#     sal_cap = models.FloatField(null=True, blank=True, default=0.0)
#     sal_cap_dia = models.FloatField(null=True, blank=True, default=0.0)
#     sal_int_dia = models.FloatField(null=True, blank=True, default=0.0)
#     int_cau_res_per = models.FloatField(null=True, blank=True, default=0.0)
#     int_pag_per = models.FloatField(null=True, blank=True, default=0.0)
#     int_conkas_per = models.FloatField(null=True, blank=True, default=0.0)
#     categoria = models.CharField(max_length=1, null=True, default=' ')
#     arrastre = models.CharField(max_length=1, null=True, default=' ')
#     aporte = models.FloatField(null=True, blank=True, default=0.0)
#     pro_ind = models.FloatField(null=True, blank=True, default=0.0)
#     saldo_1 = models.FloatField(null=True, blank=True, default=0.0)
#     saldo_2 = models.FloatField(null=True, blank=True, default=0.0)
#     vr_gar_hip = models.FloatField(null=True, blank=True, default=0.0)
#     cat_int_mes = models.CharField(max_length=1, null=True, default=' ')
#     sal_cat_int = models.FloatField(null=True, blank=True, default=0.0)
#     castigo = models.CharField(max_length=1, null=True, default=' ')
#     gas_pro_ind = models.FloatField(null=True, blank=True, default=0.0)
#     gas_pro_gen = models.FloatField(null=True, blank=True, default=0.0)
#     int_cor_per = models.FloatField(null=True, blank=True, default=0.0)
#     cat_mod = models.CharField(max_length=1, null=True, default=' ')
#     cat_eva = models.CharField(max_length=1, null=True, default=' ')
#     cat_ree = models.CharField(max_length=1, null=True, default=' ')
#     cat_sel = models.CharField(max_length=1, null=True, default=' ')
#     zeta = models.FloatField(null=True, blank=True, default=0.0)
#     puntaje = models.FloatField(null=True, blank=True, default=0.0)
#     pro_inc = models.FloatField(null=True, blank=True, default=0.0)
#     pdi = models.FloatField(null=True, blank=True, default=0.0)
#     vea = models.FloatField(null=True, blank=True, default=0.0)
#     per_esp = models.FloatField(null=True, blank=True, default=0.0)
#     conta_per = models.SmallIntegerField(null=True, default=0)
#     ali_cuota = models.FloatField(null=True, default=0.0)
#     det_ind_gas_acu = models.FloatField(null=False, blank=True, default=0.0)

#     class Meta:
#         unique_together = [['oficina', 'fecha', 'cod_cre']]
#         indexes = [
#             models.Index(fields=['oficina', 'fecha', 'nit']),
#         ]
#         db_table = 'carte_cat_his'


# class CARTERA_CXC(models.Model):
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
#     credito = models.ForeignKey(CREDITOS, on_delete=models.CASCADE, null=True)
#     cod_cre = models.CharField(max_length=10, null=False)
#     fecha = models.DateField(null=False, blank=True)
#     fec_ref = models.DateField(null=True, blank=True)
#     categoria = models.CharField(max_length=1, null=True)
#     valor = models.FloatField(null=True, blank=True)
#     val_det = models.FloatField(null=True, blank=True)
#     clave = models.SmallIntegerField(null=True)

#     class Meta:
#         unique_together = [['oficina', 'fecha',
#                             'cod_cre', 'fec_ref', 'categoria']]
#         db_table = 'cartera_cxc'


# class CATE_INTE(models.Model):
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
#     fecha = models.DateField(null=True, blank=True)
#     cod_cre = models.CharField(max_length=10, null=True)
#     tipo = models.CharField(max_length=1, null=True)
#     nit = models.CharField(max_length=12, null=True)
#     fec_des = models.DateField(null=True, blank=True)
#     cod_imp = models.CharField(max_length=2, null=True)
#     cat_ini = models.CharField(max_length=1, null=True, default=' ')
#     cat_fin = models.CharField(max_length=1, null=True, default=' ')
#     arr_ini = models.CharField(max_length=1, null=True, default=' ')
#     arr_fin = models.CharField(max_length=1, null=True, default=' ')
#     sal_cap_ini = models.FloatField(null=False, blank=True, default=0.0)
#     sal_cap_fin = models.FloatField(null=False, blank=True, default=0.0)
#     int_dia_ini = models.FloatField(null=False, blank=True, default=0.0)
#     int_cau_ini = models.FloatField(null=False, blank=True, default=0.0)
#     inicio = models.FloatField(null=False, blank=True, default=0.0)
#     int_pag = models.FloatField(null=False, blank=True, default=0.0)
#     int_dia_fin = models.FloatField(null=False, blank=True, default=0.0)
#     int_cau_fin = models.FloatField(null=False, blank=True, default=0.0)
#     final = models.FloatField(null=False, blank=True, default=0.0)
#     int_cau_mes = models.FloatField(null=False, blank=True, default=0.0)
#     int_pag_ant = models.FloatField(null=False, blank=True, default=0.0)
#     int_pag_act = models.FloatField(null=False, blank=True, default=0.0)
#     int_pag_ade = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_A = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_B = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_C = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_D = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_E = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_Z = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_ZC = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_ZD = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_ZE = models.FloatField(null=False, blank=True, default=0.0)
#     ip_ant_ZF = models.FloatField(null=False, blank=True, default=0.0)
#     cue_pr_cob_A = models.FloatField(null=False, blank=True, default=0.0)
#     cue_pr_cob_B = models.FloatField(null=False, blank=True, default=0.0)
#     cue_pr_cob_C = models.FloatField(null=False, blank=True, default=0.0)
#     cue_pr_cob_D = models.FloatField(null=False, blank=True, default=0.0)
#     cue_pr_cob_E = models.FloatField(null=False, blank=True, default=0.0)
#     cue_pr_cob_F = models.FloatField(null=False, blank=True, default=0.0)
#     cau_ZC = models.FloatField(null=False, blank=True, default=0.0)
#     cau_ZD = models.FloatField(null=False, blank=True, default=0.0)
#     cau_ZE = models.FloatField(null=False, blank=True, default=0.0)
#     cau_ZF = models.FloatField(null=False, blank=True, default=0.0)
#     cau_ZET = models.FloatField(null=False, blank=True, default=0.0)
#     ingreso = models.FloatField(null=False, blank=True, default=0.0)
#     cue_por_pag = models.FloatField(null=False, blank=True, default=0.0)
#     cre_con_cas = models.CharField(max_length=1, choices=OPC_BOOL, default=' ')
#     int_con = models.FloatField(null=False, blank=True, default=0.0)
#     pro_ind_ini = models.FloatField(null=False, blank=True, default=0.0)
#     pro_ind_fin = models.FloatField(null=False, blank=True, default=0.0)
#     gas_pro_ind_ini = models.FloatField(null=True, blank=True, default=0.0)
#     gas_pro_ind_fin = models.FloatField(null=False, blank=True, default=0.0)
#     pro_gen_ini = models.FloatField(null=False, blank=True, default=0.0)
#     pro_gen_fin = models.FloatField(null=False, blank=True, default=0.0)
#     gas_gen_ini = models.FloatField(null=False, blank=True, default=0.0)
#     gas_gen_fin = models.FloatField(null=False, blank=True, default=0.0)
#     det_ind_gas_acu = models.FloatField(null=False, blank=True, default=0.0)

#     class Meta:
#         unique_together = [['oficina', 'fecha', 'cod_cre']]
#         db_table = 'cate_inte'


# # Entrega la Calificacion a Partir de un Puntaje por rANGOS
# class PE_CALIF_RANGO(models.Model):
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     clase_coop = models.CharField(max_length=8, choices=CLASE_COOP)
#     modalidad = models.CharField(
#         max_length=6, choices=OPC_MODALIDAD_CRE, default='CCSL')
#     calificacion = models.CharField(max_length=1, blank=False)
#     pi_puntaje = models.FloatField(null=False, blank=True, default=0.0)

#     class Meta:
#         unique_together = [
#             ['cliente', 'clase_coop', 'modalidad', 'calificacion']]
#         db_table = 'pe_calif_rango'


# class PE_PI_CALIF(models.Model):  # Recibe la Calificacion y Entrega PI o porcentaje de
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     clase_coop = models.CharField(max_length=8, choices=CLASE_COOP)
#     modalidad = models.CharField(
#         max_length=6, choices=OPC_MODALIDAD_CRE, default='CCSL')
#     calificacion = models.CharField(max_length=1, blank=False)
#     pi_porcent = models.FloatField(null=False, blank=True, default=0.0)

#     class Meta:
#         unique_together = [
#             ['cliente', 'clase_coop', 'modalidad', 'calificacion']]
#         db_table = 'pe_pi_calif'


# class PE_PDI_RANGO(models.Model):
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     garantia = models.CharField(max_length=2, choices=OPC_GARANTIA, default='15')
#     pdi_0 = models.FloatField(null=False, blank=True, default=0.0)
#     dias_inc_1 = models.SmallIntegerField(default=0)
#     pdi_1 = models.FloatField(null=False, blank=True, default=0.0)
#     dias_inc_2 = models.SmallIntegerField(default=0)
#     pdi_2 = models.FloatField(null=False, blank=True, default=0.0)

#     class Meta:
#         unique_together = [['cliente', 'garantia']]
#         db_table = 'pe_pdi_rango'


# class PE_MODE_REFE(models.Model):
#     cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
#     modalidad = models.CharField(max_length=6, choices=OPC_MODALIDAD_CRE)
#     constante = models.FloatField(null=False, blank=True, default=0.0)
#     coe_ea = models.FloatField(null=False, blank=True, default=0.0)
#     coe_ap = models.FloatField(null=False, blank=True, default=0.0)
#     coe_tc = models.FloatField(null=False, blank=True, default=0.0)
#     coe_fe = models.FloatField(null=False, blank=True, default=0.0)
#     coe_esim = models.FloatField(null=False, blank=True, default=0.0)
#     coe_famor = models.FloatField(null=False, blank=True, default=0.0)
#     coe_valcuota = models.FloatField(null=False, blank=True, default=0.0)
#     coe_valpres = models.FloatField(null=False, blank=True, default=0.0)
#     coe_ocoop = models.FloatField(null=False, blank=True, default=0.0)
#     coe_fonaho = models.FloatField(null=False, blank=True, default=0.0)
#     coe_coopcdat = models.FloatField(null=False, blank=True, default=0.0)
#     coe_fondplazo = models.FloatField(null=False, blank=True, default=0.0)
#     coe_antipre1 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_mora15 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_mora1230 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_mora1260 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_mora2430 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_mora2460 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_sinmora = models.FloatField(null=False, blank=True, default=0.0)
#     coe_mortrim = models.FloatField(null=False, blank=True, default=0.0)
#     coe_reest = models.FloatField(null=False, blank=True, default=0.0)
#     coe_cuenaho = models.FloatField(null=False, blank=True, default=0.0)
#     coe_cdat = models.FloatField(null=False, blank=True, default=0.0)
#     coe_per = models.FloatField(null=False, blank=True, default=0.0)
#     coe_entidad1 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_antipre2 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_vin2 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_mora3615 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_entidad2 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_plazol = models.FloatField(null=False, blank=True, default=0.0)
#     coe_salpres = models.FloatField(null=False, blank=True, default=0.0)
#     coe_m1mora30 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_m2mora30 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_m1mora30m3 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_amor = models.FloatField(null=False, blank=True, default=0.0)
#     coe_nodo4 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_nodo5 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_nodo7 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_nodo8 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_nodo9 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_nodo1 = models.FloatField(null=False, blank=True, default=0.0)
#     coe_mora3660 = models.FloatField(null=False, blank=True, default=0.0)

#     class Meta:
#         unique_together = [['cliente', 'modalidad']]
#         db_table = 'pe_mode_refe'


# class PE_CARTE_HIS(models.Model):
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, default=None)
#     fecha = models.DateField(null=False, blank=True)
#     cod_cre = models.CharField(max_length=10, null=True)
#     modalidad = models.CharField(max_length=6, choices=OPC_MODALIDAD_CRE)
#     calificacion = models.CharField(max_length=1, null=True)
#     pe = models.FloatField(null=False, blank=True, default=0.0)
#     pi = models.FloatField(null=False, blank=True, default=0.0)
#     vea = models.FloatField(null=False, blank=True, default=0.0)
#     pdi = models.FloatField(null=False, blank=True, default=0.0)
#     puntaje = models.FloatField(null=False, blank=True, default=0.0)
#     z = models.FloatField(null=False, blank=True, default=0.0)
#     val_ea = models.SmallIntegerField(default=0)
#     val_ap = models.SmallIntegerField(default=0)
#     val_tc = models.SmallIntegerField(default=0)
#     val_fe = models.SmallIntegerField(default=0)
#     val_esim = models.SmallIntegerField(default=0)
#     val_famor = models.SmallIntegerField(default=0)
#     val_valcuota = models.SmallIntegerField(default=0)
#     val_valpres = models.SmallIntegerField(default=0)
#     val_ocoop = models.SmallIntegerField(default=0)
#     val_fonaho = models.SmallIntegerField(default=0)
#     val_coopcdat = models.SmallIntegerField(default=0)
#     val_fondplazo = models.SmallIntegerField(default=0)
#     val_antipre1 = models.SmallIntegerField(default=0)
#     val_mora15 = models.SmallIntegerField(default=0)
#     val_mora1230 = models.SmallIntegerField(default=0)
#     val_mora1260 = models.SmallIntegerField(default=0)
#     val_mora2430 = models.SmallIntegerField(default=0)
#     val_mora2460 = models.SmallIntegerField(default=0)
#     val_simmora = models.SmallIntegerField(default=0)
#     val_mortrim = models.SmallIntegerField(default=0)
#     val_reest = models.SmallIntegerField(default=0)
#     val_cuenaho = models.SmallIntegerField(default=0)
#     val_cdat = models.SmallIntegerField(default=0)
#     val_per = models.SmallIntegerField(default=0)
#     val_entidad1 = models.SmallIntegerField(default=0)
#     val_antipre2 = models.SmallIntegerField(default=0)
#     val_vin2 = models.SmallIntegerField(default=0)
#     val_mora3615 = models.SmallIntegerField(default=0)
#     val_entidad2 = models.SmallIntegerField(default=0)
#     val_plazol = models.SmallIntegerField(default=0)
#     val_salpres = models.SmallIntegerField(default=0)
#     val_m1mora30 = models.SmallIntegerField(default=0)
#     val_m2mora30 = models.SmallIntegerField(default=0)
#     val_m1mora30m3 = models.SmallIntegerField(default=0)
#     val_amor = models.SmallIntegerField(default=0)
#     val_nodo4 = models.SmallIntegerField(default=0)
#     val_nodo5 = models.SmallIntegerField(default=0)
#     val_nodo7 = models.SmallIntegerField(default=0)
#     val_nodo8 = models.SmallIntegerField(default=0)
#     val_nodo9 = models.SmallIntegerField(default=0)
#     val_nodo1 = models.SmallIntegerField(default=0)
#     val_mora3660 = models.SmallIntegerField(default=0)

#     class Meta:
#         unique_together = [['oficina', 'fecha', 'cod_cre']]
#         db_table = 'pe_carte_his'


# class INT_DIA_AHO(models.Model):
#     oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, default=None)
#     cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
#     num_cta = models.CharField(max_length=10, null=True)
#     dia_mes = models.IntegerField()
#     fecha = models.DateField(null=True, blank=True)
#     int_dia = models.BigIntegerField(null=True)
#     ret_fue = models.BigIntegerField(null=True)
#     aplicado = models.CharField(max_length=1, choices=OPC_BOOL)

#     class Meta:
#         unique_together = [['oficina', 'cta_aho','dia_mes']]
#         db_table = 'int_dia_aho'
