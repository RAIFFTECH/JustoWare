from django.db import models
from justo_app.opciones import OPC_EDUCACION,OPC_BOOL,OPC_EST_CIV,OPC_ESTADO_ANTEIA,OPC_SEXO,OPC_PARENTESCO,OPC_CLASEDOC,OPC_REFERENCIAS
from clientes_app.models import CLIENTES
from oficinas_app.models import OFICINAS
from terceros_app.models import TERCEROS
from localidades_app.models import LOCALIDADES
from pagadores_app.models import PAGADORES 
from justo_app.models import DefaultToZeroMixin
# Create your models here.


class ASOCIADOS(DefaultToZeroMixin):
    cod_aso = models.CharField(max_length=12, null=False, verbose_name='Código Asociado')
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE, null=True, verbose_name='Oficina')
    tercero = models.ForeignKey(TERCEROS, on_delete=models.CASCADE, null=True, verbose_name='Tercero')
    sexo = models.CharField(max_length=1, choices=OPC_SEXO, verbose_name='Sexo')
    est_civ = models.CharField(max_length=1, choices=OPC_EST_CIV, verbose_name='Estado Civil')
    fec_nac = models.DateField(null=True, blank=True, verbose_name='Fecha Nacimiento')
    ciu_res = models.ForeignKey(LOCALIDADES, on_delete=models.CASCADE, null=True, verbose_name='Ciudad de Residencia')
    zona = models.CharField(max_length=16, null=True, blank=True, verbose_name='Zona')
    profesion = models.CharField(max_length=48, null=True, blank=True, verbose_name='Profesión')
    ocupacion = models.CharField(max_length=40, null=True, blank=True, verbose_name='Ocupación')
    ocupacion_cod = models.CharField(max_length=3, null=True, blank=True, verbose_name='Código Ocupación')
    estrato = models.CharField(max_length=1, null=True, blank=True, verbose_name='Estrato')
    niv_est = models.CharField(max_length=1, choices=OPC_EDUCACION, verbose_name='Nivel de Estudio')
    cab_fam = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Cabeza de Familia?')
    id_pag = models.ForeignKey(PAGADORES, on_delete=models.CASCADE, null=True, verbose_name='Empresa Nominadora')
    fec_afi = models.DateField(null=True, blank=True, verbose_name='Fecha Afiliación')
    cargo_emp = models.CharField(max_length=36, null=True, verbose_name='Cargo en la Empresa')
    per_a_cargo = models.IntegerField(null=True, blank=True, verbose_name='Personas a Cargo')
    num_hij_men = models.IntegerField(blank=True, null=True, verbose_name='Número Hijos Menores')
    num_hij_may = models.IntegerField(blank=True, null=True, verbose_name='Número Hijos Mayores')
    tip_viv = models.CharField(max_length=24, null=True, verbose_name='Tipo de Vivienda')
    tie_en_ciu = models.IntegerField(blank=True, null=True, verbose_name='Tiempo en la Ciudad')
    med_con = models.CharField(max_length=48, null=True)
    fec_ing_tra = models.DateField(null=True, blank=True, verbose_name='Fecha Ingreso Trabajo')
    tel_tra = models.CharField(max_length=10, null=True, verbose_name='Teléfono Trabajo')
    tip_sal = models.CharField(max_length=18, null=True, verbose_name='Tipo de Salario')
    ciu_tra = models.ForeignKey(LOCALIDADES, on_delete=models.CASCADE, null=True, verbose_name='Ciudad de Trabajo')
    act_eco = models.CharField(max_length=24, null=True, verbose_name='Actividad Económica')
    cod_ciiu = models.CharField(max_length=12, null=True)
    tip_con = models.CharField(max_length=18, null=True, verbose_name='Tipo Contrato')
    nom_emp = models.CharField(max_length=40, null=True, verbose_name='Nombre Empresa')
    nit_emp = models.CharField(max_length=12, null=True, verbose_name='Nit Empresa')
    dir_emp = models.CharField(max_length=50, null=True, verbose_name='Dirección Empresa')
    email_emp = models.EmailField(blank=True, null=True, verbose_name='e-mail Empresa')
    sector_emp = models.CharField(max_length=12, null=True, verbose_name='Sector Empresa')
    empresa_ant = models.IntegerField(blank=True, null=True, verbose_name='Empresa Anterior')
    emp_num_emp = models.IntegerField(blank=True, null=True)
    negocio_pro = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Negocio Propio?')
    negocio_nom = models.CharField(max_length=48, null=True, verbose_name='Nombre Negocio')
    negocio_tel = models.CharField(max_length=10, null=True, verbose_name='Teléfono Negocio')
    negocio_loc_pro = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Local Propio?')
    negocio_cam_com = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Tiene Cámara Comercio?')
    negocio_ant = models.IntegerField(blank=True, null=True)
    pension_ent = models.CharField(max_length=36, null=True, verbose_name='Entidad de Pensión')
    pension_tie = models.IntegerField(blank=True, null=True)
    pension_otr = models.CharField(max_length=1, choices=OPC_BOOL)
    pension_ent_otr = models.CharField(max_length=36, null=True)
    pep_es_fam = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Tiene Familiar PEP?')
    pep_fam_par = models.CharField(max_length=1, choices=OPC_PARENTESCO, verbose_name='Parentesco Familiar PEP')
    pep_fam_nom = models.CharField(max_length=36, null=True, verbose_name='Nombre Familiar PEP')
    pep_car_pub = models.CharField(max_length=1, choices=OPC_BOOL)
    pep_cargo = models.CharField(max_length=36, null=True)
    pep_eje_pod = models.CharField(max_length=1, choices=OPC_BOOL)
    pep_adm_rec_est = models.CharField(max_length=1, choices=OPC_BOOL)
    tie_gre_car = models.CharField(max_length=1, choices=OPC_BOOL)
    recibe_pag_ext = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Recibe Pagos del Extranjero?')
    recide_ext_mas_186 = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Recibe Extranjero +186?')
    recibe_ing_ext = models.CharField(max_length=1, choices=OPC_BOOL, verbose_name='Recibe Ingresos Extranjeros?')
    estado_anteia = models.CharField(max_length=1, choices=OPC_ESTADO_ANTEIA, null=False, default=2, verbose_name='Estado Anteia')

    class Meta:
        unique_together = [['oficina', 'cod_aso']]
        db_table = 'asociados'

    def __str__(self):
        return self.cod_aso+' '+self.tercero


class ASO_BENEF(models.Model):
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
    cla_doc = models.CharField(max_length=1, choices=OPC_CLASEDOC)
    doc_ide = models.CharField(max_length=12, null=False)
    nombre = models.CharField(max_length=64, null=False)
    agno_nac = models.IntegerField(blank=True, null=True)
    parentesco = models.CharField(max_length=1, choices=OPC_PARENTESCO)
    porcentaje = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = [['asociado', 'doc_ide']]
        db_table = 'aso_benef'
    
    def __str__(self):
        return self.nombre


class ASO_REFERENCIAS(models.Model):
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
    tipo_ref = models.CharField(max_length=1, choices=OPC_REFERENCIAS)
    parentesco = models.CharField(max_length=1, choices=OPC_PARENTESCO)
    nombre = models.CharField(max_length=64, null=False)
    ocupacion = models.CharField(max_length=32, null=False)
    empresa = models.CharField(max_length=40, null=False)
    direccion = models.CharField(max_length=64, null=False)
    tel_fijo = models.CharField(max_length=10, null=False)
    tel_cel = models.CharField(max_length=10, null=False)
    tel_emp = models.CharField(max_length=10, null=False)

    class Meta:
        unique_together = [['asociado', 'nombre']]
        db_table = 'aso_referencias'
    
    def __str__(self):
        return self.nombre
