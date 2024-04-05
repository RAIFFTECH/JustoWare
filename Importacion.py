import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Justo_proy.settings')
import django
django.setup()
import csv
from django.shortcuts import render
from django.http import HttpResponse
import justo_app.models as justo
from datetime import datetime
from django.db.models.query import QuerySet
from django.db.models import F, Sum, Case, When, Value, FloatField, CharField, IntegerField
from django.db.models.functions import Coalesce
from operator import itemgetter
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from datetime import timedelta
from decimal import Decimal, ROUND_HALF_UP

def gomonth(fecha, meses):
    return fecha + relativedelta(months=meses)

def asignar_fecha(fecha_str, formato='%m/%d/%Y'):
    try:
        fecha = datetime.strptime(fecha_str, formato)
        fecha_validada = fecha.strftime('%Y-%m-%d')
        return fecha_validada
    except ValueError:
        return None

def inicio():
    print('Inicial  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo = 'A').first()
    if Cliente == None:
        Cliente = justo.CLIENTES.objects.create(codigo = 'A')
    Cliente.doc_ide = '8947111111'
    Cliente.sigla = 'CORNOQUIA'
    Cliente.nombre = 'COOPERATIVA ESPECIALIZADA DE AHORRO Y CREDITO DE LA ORINOQUIA'
    Cliente.celular = '3153275734'
    Cliente.email = 'COORINOQUIA@HOTMAIL.COM'
    Cliente.dominio = 'COORINOQUIA.COOP'
    Cliente.save()
    Oficina = justo.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    if Oficina == None:
        Oficina=justo.OFICINAS.objects.create(cliente = Cliente,codigo = "A0001",
        contabiliza = 'S',
        nombre_oficina = 'Oficina Principal',
        responsable = 'Jose Guillermo Prieto López',
        celular = '3153263722',
    )
    CentroCosto = justo.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    if CentroCosto==None:
        CentroCosto = justo.CENTROCOSTOS.objects.create(cliente=Cliente,codigo = 'A001')
    with open('c:/ajusto/csv/localidades.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Localidad = justo.LOCALIDADES.objects.filter(cliente = Cliente,codigo = row['codigo']).first()
            if Localidad == None:
                Localidad = justo.LOCALIDADES.objects.create(cliente = Cliente,
                    codigo = row['codigo'])
            Localidad.nombre = row['nombre']
            Localidad.cod_pos = row['codpos']
            Localidad.departamento = row['dpto']
            Localidad.save()
    with open('c:/ajusto/csv/c00documentos.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            DocZep = justo.XDOC_ZEP.objects.filter(per_con=int(row['c00agno']),clase_zep=row['c00clase']).first()
            if DocZep == None:
                DocZep = justo.XDOC_ZEP.objects.create(per_con=int(row['c00agno']),clase_zep=row['c00clase'])
            DocZep.doc_ds =row['c00docds']
            DocZep.nombre =row['c00nombre']
            DocZep.descripcion =row['c00descrip']
            DocZep.save()
    print('         ',datetime.now())

def tablas_de_referencia():
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    justo.PE_CALIF_RANGO.objects.filter(cliente = Cliente).delete()
    justo.PE_PI_CALIF.objects.filter(cliente = Cliente).delete()
    justo.PE_PDI_RANGO.objects.filter(cliente = Cliente).delete()
    justo.PE_MODE_REFE.objects.filter(cliente = Cliente).delete()
#  se busca la Calificacion a partir de un Puntaje Cartera de Consumo Con Libranza Entra el Puntaje y sale la Calificacion
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='A',pi_puntaje = 0.0174)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='B',pi_puntaje = 0.0337)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='C',pi_puntaje = 0.0479)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='D',pi_puntaje = 0.0812)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='E',pi_puntaje = 1.0)
#  se busca la Calificacion a partir de un Puntaje Cartera de Consumo Sin Libranza  Entra el Puntaje y sale la Calificacion
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='A',pi_puntaje = 0.0559)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='B',pi_puntaje = 0.1066)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='C',pi_puntaje = 0.2199)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='D',pi_puntaje = 0.3690)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='E',pi_puntaje = 1)
#  se busca la Calificacion a partir de un Puntaje Cartera Comercial Persona Natural Entra el Puntaje y sale la Calificacion
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPN',calificacion='A',pi_puntaje = 0.2340)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPN',calificacion='B',pi_puntaje = 0.4291)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPN',calificacion='C',pi_puntaje = 0.5905)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPN',calificacion='D',pi_puntaje = 0.7571)
    justo.PE_CALIF_RANGO.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPN',calificacion='E',pi_puntaje = 1)

#  Cartera de Consumo Con Libranza Entra le Calificacion y sale la Porbabilidad de Incumplimieno PI en porcentaje
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='A',pi_porcent = 0.50)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='B',pi_porcent = 0.60)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='C',pi_porcent = 4.41)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='D',pi_porcent = 4.48)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='E',pi_porcent = 22.73)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCCL',calificacion='F',pi_porcent = 100.0)
#  Calificacion segun Puntaje  Cartera de Consumo Sin Libranza
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='A',pi_porcent = 1.50)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='B',pi_porcent = 5.95)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='C',pi_porcent = 13.82)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='D',pi_porcent = 32.77)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='E',pi_porcent= 41.71)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCSL',calificacion='F',pi_porcent = 100.0)
#  Calificacion segun Puntaje  Cartera Comercial Persona Natural
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPJ',calificacion='A',pi_porcent = 0.37)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPJ',calificacion='B',pi_porcent = 6.21)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPJ',calificacion='C',pi_porcent = 12.43)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPJ',calificacion='D',pi_porcent = 21.05)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPJ',calificacion='E',pi_porcent = 58.97)
    justo.PE_PI_CALIF.objects.create(cliente=Cliente,clase_coop='EAYC',modalidad = 'CCPJ',calificacion='F',pi_porcent = 100.0)

#  Determina la PDI a partir de el tipo de garantia y los dias de incumplimiento
    justo.PE_PDI_RANGO.objects.create(cliente=Cliente,garantia='1',pdi_0=60.0,dias_inc_1=210,pdi_1=70.0,dias_inc_2=420,pdi_2=100)
    justo.PE_PDI_RANGO.objects.create(cliente=Cliente,garantia='2',pdi_0=40.0,dias_inc_1=360,pdi_1=70.0,dias_inc_2=720,pdi_2=100)
    justo.PE_PDI_RANGO.objects.create(cliente=Cliente,garantia='15',pdi_0=75.0,dias_inc_1=30,pdi_1=85.0,dias_inc_2=90,pdi_2=100)

#  Se introducen los coeficientes de los modelos
    justo.PE_MODE_REFE.objects.create(cliente = Cliente,modalidad = 'CCCL',constante = -2.250040,coe_ea = -0.84440,coe_ap = -1.05730,coe_tc = 1.07150,coe_fe = 0.01390,
        coe_esim = 0.41870,coe_famor = 0.53130, coe_valcuota = -0.5536,coe_valpres = -0.3662,coe_ocoop = 0.0586,coe_fonaho = -0.5981,coe_coopcdat = -1.3854,
        coe_fondplazo = -0.5893,coe_antipre1 = 0.7833,coe_mora15 = 0.8526,coe_mora1230 = 1.4445,coe_mora1260 = 1.3892,coe_mora2430 = 0.2823,
        coe_mora2460 = 0.7515,coe_sinmora = -0.6632,coe_mortrim = 1.2362,coe_reest = 0.0,coe_cuenaho = 0.0,coe_cdat = 0.0,coe_per = 0,coe_entidad1 = 0.0,coe_antipre2 = 0.0,
        coe_vin2 = 0.0,coe_mora3615 = 0.0,coe_entidad2 = 0.0,coe_plazol = 0.0,coe_salpres = 0.0,coe_m1mora30 = 0.0,coe_m2mora30 = 0.0,coe_m1mora30m3 = 0.0,coe_amor = 0.0,
        coe_nodo4 = 0.0,coe_nodo5 = 0.0,coe_nodo7 = 0.0,coe_nodo8 = 0.0,coe_nodo9 = 0.0,coe_nodo1 = 0.0,coe_mora3660 = 0)
    justo.PE_MODE_REFE.objects.create(cliente = Cliente,modalidad = 'CCSL',constante = -1.8017,coe_ea = -0.3758,coe_ap = 0.0,coe_tc = 0.0,coe_fe = 0.0,
        coe_esim = 0.0,coe_famor = 0.0, coe_valcuota = -0.0,coe_valpres = -0.0,coe_ocoop = 0.0,coe_fonaho = -0.0,coe_coopcdat = -0.0,
        coe_fondplazo = -0.0,coe_antipre1 = 0.1271,coe_mora15 = 0.0,coe_mora1230 = 0.7877,coe_mora1260 = 2.5651,coe_mora2430 = 0.696,
        coe_mora2460 = 0.696,coe_sinmora = -0.0,coe_mortrim = 0.0,coe_reest = 0.4934,coe_cuenaho = -0.387,coe_cdat = 1.0786,coe_per = -0.0167,coe_entidad1 = 0.3204,coe_antipre2 = -0.3912,
        coe_vin2 = -0.4892,coe_mora3615 = 0.81140,coe_entidad2 = 0.0,coe_plazol = 0.0,coe_salpres = -0.8419,coe_m1mora30 = 0.0,coe_m2mora30 = 0.0,coe_m1mora30m3 = 0.0,coe_amor = 0.0,
        coe_nodo4 = 0.0,coe_nodo5 = 0.0,coe_nodo7 = 0.0,coe_nodo8 = 0.0,coe_nodo9 = 0.0,coe_nodo1 = 0.0,coe_mora3660 = 0)


    return

def terceros():
    print('Terceros....  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/Terceros.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Tercero = justo.TERCEROS.objects.filter(cliente=Cliente,
            cla_doc = row['LL_TIP_DOC'][0],
            doc_ide = row['NIT']).first()
            if Tercero == None:
                print('Nuevo Ter',row['NIT'])
                Tercero = justo.TERCEROS.objects.create(
                    cliente = Cliente,
                    cla_doc = row['LL_TIP_DOC'][0],
                    doc_ide = row['NIT']
                )
            Tercero.dig_ver = row['DV']
            Tercero.nit_rap = row['NIT_RAP']
            Tercero.cod_ciu_exp = justo.LOCALIDADES.objects.filter(cliente=Cliente,
                        codigo=row['CO_CIU_EXP']).first()
            Tercero.cod_ciu_res = justo.LOCALIDADES.objects.filter(cliente=Cliente,
                        codigo=row['CO_CIU_RES']).first()
            Tercero.regimen = row['LL_REGIMEN']
            Tercero.fec_exp_ced = asignar_fecha(row['FEC_EXP_CED'])
            Tercero.tip_ter = row['LL_TIP_TER']
            Tercero.pri_ape = row['PRI_APE'][:10]
            Tercero.seg_ape = row['SEG_APE'][:10]
            Tercero.pri_nom = row['PRI_NOM'][:10]
            Tercero.seg_nom  = row['SEG_NOM'][:10]
            Tercero.raz_soc  = row['RAZ_SOC']
            Tercero.direccion = row['DIRECCION']
            Tercero.cod_pos = row['CO_CODPOS']
            Tercero.tel_ofi  = row['TEL_OFI'][:10]
            Tercero.tel_res = row['TEL_RES'][:10]
            Tercero.celular1 = row['CELULAR1'][:10]
            Tercero.celular2 = row['CELULAR2'][:10]
            Tercero.fax = row['FAX']
            Tercero.email = row['EMAIL']
            #   fec_act = datetime.strptime("1900-01-1", "%Y-%m-%d")
            #   asignar_fecha(anteia1['flows'][idsocio]['form.date'])
            Tercero.observacion = row['OBSERVACION']
            Tercero.per_pub_exp = row['PER_PUB_EXP']
            Tercero.nit_interno = row['NIT_INTERNO']
            Tercero.id_ds = row['ID']
            Tercero.save()
    print('Fin Terceros  ',datetime.now())

def pagadores():
    print('Pagadores..  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s07entidades.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')    
        for row in csv_reader:
            pagador = justo.pagadores.objects.filter(
                    cliente=Cliente,
                    codigo=row['s07codent']).first()
            if pagador == None:
                pagador=justo.pagadores.objects.create(cliente = Cliente,
                        codigo = row['s07codent'])
            pagador.nombre = row['s07nombre']
            pagador.ciudad = row['s07ciudad']
            pagador.pagador = row['s07nompag']
            pagador.tel_cel = row['s07telpag']
            pagador.save()
    print('Fin pagadores ',datetime.now())

def socios():
    print('Socios....  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s01socios.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Tercero = justo.TERCEROS.objects.filter(cliente=Cliente,doc_ide = row['s01nit']).first()
            if Tercero == None:
                print('No Hay Tercero ',row['s01nit'])
                continue
            Socio = justo.ASOCIADOS.objects.filter(oficina=Oficina,cod_aso = row['s01codsoc']).first()
            if Socio == None:
                Socio = justo.ASOCIADOS.objects.create(
                        oficina = Oficina,
                        cod_aso = row['s01codsoc']
                    )    
            pagador = justo.pagadores.objects.filter(
                    cliente=Cliente,
                    codigo=row['s01codent']).first()
            Socio.tercero = Tercero
            Socio.sexo = row['s01sexo'][:1]
            Socio.est_civ = row['s01estciv']
            Socio.fec_nac = asignar_fecha(row['s01fecnac'])
            Socio.ciu_res = ''
            Socio.zona  = ''
            Socio.profesion = ''
            Socio.ocupacion =''
            Socio.ocupacion_cod = ''
            Socio.estrato = row['s01estrato']
            Socio.niv_est  = row['s01nivest'][:1]
            Socio.cab_fam = row['s01mujcabfam']
            Socio.id_pag = pagador
            Socio.fec_afi = asignar_fecha(row['s01fecingc'])
            Socio.cargo_emp = row['s01cargo']
            Socio.per_a_cargo = row['s01peracar']
            Socio.num_hij_men = 0
            Socio.num_hij_may = row['s01peracar']
            Socio.tip_viv = ''
            Socio.tie_en_ciu = '' 
            Socio.med_con = ''
            Socio.fec_ing_tra = asignar_fecha(row['s01fecinge'])
            Socio.tel_tra = ''
            Socio.tip_sal= ''
            Socio.ciu_tra = ''
            Socio.act_eco = ''
            Socio.cod_ciiu = ''
            Socio.tip_con = ''
            Socio.nom_emp = ''
            Socio.nit_emp = ''
            Socio.dir_emp = ''
            Socio.email_emp = ''
            Socio.sector_emp = ''
            Socio.empresa_ant = ''
            Socio.emp_num_emp = ''
            Socio.negocio_pro = ''
            Socio.negocio_nom = ''
            Socio.negocio_tel = ''
            Socio.negocio_loc_pro = '' 
            Socio.negocio_cam_com = ''
            Socio.negocio_ant = ''
            Socio.pension_ent = ''
            Socio.pension_tie = ''
            Socio.pension_otr = ''
            Socio.pension_ent_otr = '' 
            Socio.pep_es_fam = ''
            Socio.pep_fam_par = ''
            Socio.pep_fam_nom = ''
            Socio.pep_car_pub = ''
            Socio.pep_cargo = ''
            Socio.pep_eje_pod = '' 
            Socio.pep_adm_rec_est = '' 
            Socio.tie_gre_car = ''
            Socio.recibe_pag_ext = '' 
            Socio.recide_ext_mas_186 = '' 
            Socio.recibe_ing_ext = ''
            Socio.estado_anteia = ''
            Socio.save()
    print('Fin socios  ',datetime.now())

def conceptos():
    print('Conceptos Justo ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo = 'A').first()
    with open('c:/ajusto/csv/c02concepto.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            Concepto = justo.CONCEPTOS.objects.filter(cliente=Cliente,cod_con=row['c02codcon']).first()
            if Concepto == None:
                Concepto = justo.CONCEPTOS.objects.create(cliente=Cliente,cod_con=row['c02codcon'])
            Concepto.con_justo = 'S' if row['c02noborra']=='T' else 'N'
            Concepto.descripcion = row['c02descripcion']
            Concepto.tip_dev_ap = 'N' if row['c02tipdevapo'] else (row['c02tipdevapo'] if len(row['c02tipdevapo']) == 1 else ('N'))       
            Concepto.tip_con = 'S' if row['c02tipcon']=='T' else 'N'
            Concepto.tip_sis = row['c02tipsis']
            Concepto.cta_con = row['c02ctacon']
            Concepto.cta_con_pas = row['c02ctapas']
            Concepto.debito = 'S' if row['c02debito'] == 'T' else 'N'
            Concepto.credito = 'S' if row['c02credito'] == 'T' else 'N'
            Concepto.por_tercero =  'S' if row['c02conporter'] == 'T' else 'N'
            Concepto.por_ret_fue =  row['c02por_ret']
            Concepto.save()
    print('                ',datetime.now())    

def plan_ctas():
    #  Tener cuidado con puntos decimales quitar ,00 no usar foxpro
    print('Plan Ctas  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo = 'A').first()
    with open('c:/ajusto/csv/Planctas.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            if row['TIP_CON'] == '1':
                PlanCta = justo.PLAN_CTAS.objects.filter(cliente=Cliente,per_con=row['PER_CON'],
                    cod_cta=row['COD_CTA']).first()
                if PlanCta == None:
                    PlanCta = justo.PLAN_CTAS.objects.create(cliente=Cliente,per_con=row['PER_CON'],
                cod_cta=row['COD_CTA'])
                PlanCta.nom_cta = row['NOMBRE'][:64]
                PlanCta.tip_cta = row['TIP_CTA']
                PlanCta.dinamica = row['DINAMICA']
                PlanCta.naturaleza = row['NATURALEZA']
                PlanCta.activa = row['ACTIVA']
                PlanCta.por_tercero  = row['POR_TER']
                PlanCta.cta_act_fij  = row['CTA_ACT_FIJ']
                PlanCta.cta_pre  = row['CTA_PRE']
                PlanCta.cta_bal  = row['CTA_BAL']
                PlanCta.cta_res = row['CTA_RES']
                PlanCta.cta_ord = row['CTA_ORD']
                PlanCta.cta_ban  = row['CTA_BAN']
                PlanCta.cta_gan_per = row['CTA_GANPER']
                PlanCta.cta_per_gan = row['CTA_PERGAN']  
                PlanCta.cta_dep  = row['CTA_DEP']
                PlanCta.cta_ing_ret = row['CTA_INGRET']
                PlanCta.cta_ret_iva  = row['CTA_RETIVA']
                PlanCta.cta_rec  = row['CTA_REC']
                PlanCta.id_ds  = row['ID']
                PlanCta.save()
    print('           ',datetime.now())

def docto_conta():    
    print('Documentos  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo = 'A').first()
    Oficina = justo.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    with open('c:/ajusto/csv/documentos.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            DoctoConta = justo.DOCTO_CONTA.objects.filter(oficina=Oficina,per_con=int(float(row['PER_CON'])),
                codigo=int(float(row['COD_DOC']))).first()
            if DoctoConta == None:
                DoctoConta = justo.DOCTO_CONTA.objects.create(oficina=Oficina,per_con=int(float(row['PER_CON'])),
                    codigo=int(float(row['COD_DOC'])))
            DoctoConta.nom_cto = row['NOM_CTO']
            DoctoConta.nombre = row['NOMBRE']
            DoctoConta.doc_admin = row['DOC_ADM']
            DoctoConta.doc_caja = row['DE_CAJA']
            DoctoConta.inicio_nuevo_per = row['INI_NUE_VIG']
            DoctoConta.consecutivo = int(float(row['CONSECUTIVO']))
            DoctoConta.id_ds = row['ID']
            DoctoConta.save()

    print('            ',datetime.now())

def comprobantes():
    print('Comprobantes .... ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/comprobantes.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Documento = justo.DOCTO_CONTA.objects.filter(id_ds = row['ID_DOC']).first()
            if Documento == None:
                continue
            Comprobante = justo.HECHO_ECONO.objects.filter(docto_conta=Documento,numero=int(float(row['NUMERO']))).first()
            if Comprobante == None:
                Comprobante = justo.HECHO_ECONO.objects.create(docto_conta=Documento,numero=int(float(row['NUMERO'])))
            Comprobante.fecha = asignar_fecha(row['FECHA'],'%d/%m/%Y')
            Comprobante.descripcion = row['CONCEPTO'][:64]
            Comprobante.anulado =  row['ANULADO']
            Comprobante.protegido = row['PROTEGIDO']
            Comprobante.fecha_prot = asignar_fecha(row['FEC_GRA'],'%d/%m/%Y')
            Comprobante.usuario = row['CUENTA'][:16]
            Comprobante.canal = row['LL_FUENTE']
            Comprobante.id_ds = row['ID']
            Comprobante.save()
    print('             .... ',datetime.now())

def detalle_econo():
    print('Detalles Comp ... ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    CentroCosto = justo.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    with open('c:/ajusto/csv/doctos_23.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Comprobante = justo.HECHO_ECONO.objects.filter(id_ds = row['ID_COM']).first()
            if Comprobante == None:
                print('No Comprob. ID_COM ',row['ID_COM'],'  Compr.',row['COD_DOC'],'-',row['NUMERO'])
                continue
            Tercero = justo.TERCEROS.objects.filter(id_ds = row['ID_TER']).first()
            if Tercero == None:
                print('No Tercero  ID_TER ',row['ID_TER'],'  Compr.',row['COD_DOC'],'-',row['NUMERO'])
                continue
            Cuenta = justo.PLAN_CTAS.objects.filter(id_ds = row['ID_CTA']).first()
            if Cuenta == None:
                print('No Cuenta  ID_CTA  ',row['ID_CTA'],'  Compr.',row['COD_DOC'],'-',row['NUMERO'])
                continue
            #DetalleEcono = justo.DETALLE_ECONO.objects.filter(hecho_econo=Comprobante,cuenta=Cuenta,tercero=Tercero).first()
            #if DetalleEcono == None:
            DetalleEcono = justo.DETALLE_ECONO.objects.create(hecho_econo=Comprobante,cuenta=Cuenta,tercero=Tercero)
            DetalleEcono.item_concepto = row['ID_DC']
            DetalleEcono.detalle = row['DETALLE']
            DetalleEcono.debito = row['DEBITO']
            DetalleEcono.credito = row['CREDITO']
            DetalleEcono.id_ds = row['ID']
            DetalleEcono.save()
    print('              ... ',datetime.now())

def deta_eco_aho():
    print('Detalles Comp ... ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    CentroCosto = justo.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    with open('c:/ajusto/csv/s06movaho.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            fecha = datetime.strptime(row['s06fecha'],'%m/%d/%Y')
            DocZep = justo.XDOC_ZEP.objects.filter(per_con = fecha.year,clase_zep = row['s06clase']).first()
            if DocZep == None:     # No Hay Doc Zep
                continue
            Doc = justo.DOCTO_CONTA.objects.filter(oficina = Oficina,per_con = fecha.year,codigo = DocZep.doc_ds).first()
            if Doc == None:         # No Hay Documento
                continue
            Com = justo.HECHO_ECONO.objects.filter(docto_conta = Doc,numero = int(row['s06documen'])).first()
            if Com == None:         # No Hay Comprobante
                print('Mal ',row)
                continue 
            Prod = justo.DETALLE_PROD.objects.filter(oficina = Oficina,hecho_econo = Com,concepto = 'AHO',subcuenta = row['s06numcta']).first()
            if Prod == None:        # No Hay Detalle Prod
                print('No Prod ',row)
                continue
            CtaAho = justo.CTAS_AHORRO.objects.filter(oficina=Oficina,num_cta = row['s06numcta']).first()
            Ter = CtaAho.asociado.tercero
            ImpCon = justo.IMP_CON_LIN_AHO.objects.filter(linea_ahorro = CtaAho.lin_aho,cod_imp = CtaAho.cod_imp,).first()
            CtaCon1 = justo.PLAN_CTAS.objects.filter(cliente = Cliente,per_con = fecha.year,cod_cta =ImpCon.ctaafeact).first()
            CtaCon2 = justo.PLAN_CTAS.objects.filter(cliente = Cliente,per_con = fecha.year,cod_cta =ImpCon.ctaafeina).first()
            Ctas = [CtaCon1,CtaCon2]
            DetComs = justo.DETALLE_ECONO.objects.filter(hecho_econo = Com,tercero = Ter,cuenta__in = Ctas)
            xMov = ''
            if row['s06tipmov'] == '0':
                xMov = 'SalIni'
            elif row['s06tipmov'] == '1':
                xMov = 'Deposi'
            elif row['s06tipmov'] == '2':
                xMov = 'IntCta'
            elif row['s06tipmov'] == '3':
                xMov = 'IntCda'
            elif row['s06tipmov'] == '4':
                xMov = 'Canje'
            elif row['s06tipmov'] == '5':
                xMov = 'Can_OK'
            elif row['s06tipmov'] == '6':
                xMov = 'Retiro'
            elif row['s06tipmov'] == '7':
                xMov = 'RetFue'
            elif row['s06tipmov'] == '8':
                xMov = 'RF_CDA'
            elif row['s06tipmov'] == '9':
                xMov = 'CH_DEV'
            for DetCom in DetComs:
                DetCom.detalle_prod = Prod
                DetCom.item_concepto = xMov
                DetCom.save()
    print('Fin   Detalles ... ',datetime.now())
    return

def linaho():
    print('Lineas Ahorros  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s04linaho.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            LinAho = justo.LINEAS_AHORRO.objects.filter(cliente = Cliente,
                cod_lin_aho = row['s04tipcta']).first()
            if LinAho == None:
                LinAho = justo.LINEAS_AHORRO.objects.create(cliente = Cliente,
                cod_lin_aho = row['s04tipcta'])
            LinAho.nombre = row['s04nombre']    
            LinAho.termino = row['s04termino']
            LinAho.per_liq_int = row['s04perliqint']
            LinAho.cta_por_pas = row['s04ctaporpag']
            LinAho.fec_ult_liq_int =  asignar_fecha(row['s04fecultliqint'],'%m/%d/%Y')
            LinAho.saldo_minimo = row['s04monminliqint']
            LinAho.save()
    print('Fin Lin Ahorros ',datetime.now())

def imp_con_lin_aho():
    print('Imp Lin Aho     ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/S22IMPCONLINAHO.CSV', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            LinAho = justo.LINEAS_AHORRO.objects.filter(cliente=Cliente,cod_lin_aho=row['s22tipcta']).first()
            if LinAho == None:
                continue
            Impconlinaho = justo.IMP_CON_LIN_AHO.objects.filter(linea_ahorro=LinAho,cod_imp = row['s22codimp']).first()
            if Impconlinaho == None:
                Impconlinaho = justo.IMP_CON_LIN_AHO.objects.create(linea_ahorro=LinAho,cod_imp = row['s22codimp'])
            Impconlinaho.descripcion = row['s22descripcion']
            Impconlinaho.ctaafeact = row['s22ctaafecap'] 
            Impconlinaho.ctaafeina = row['s22ctaafeina']
            Impconlinaho.ctaafeint = row['s22ctaafeint']
            Impconlinaho.ctaretfue = row['s22ctaaferetfue']
            Impconlinaho.save()
    print('Fin Imp Lin Aho ',datetime.now())        

def int_lin_aho():
    print('int_lin_aho  ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s08intlinaho.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            LinAho = justo.LINEAS_AHORRO.objects.filter(cliente=Cliente,cod_lin_aho=row['s08tipcta']).first()
            if LinAho == None:
                continue
            TasLinAho = justo.TAS_LIN_AHO.objects.filter(lin_aho=LinAho,
                    fecha_inicial=asignar_fecha(row['s08fecini'],'%m/%d/%Y')).first()
            if TasLinAho == None:
                TasLinAho = justo.TAS_LIN_AHO.objects.create(lin_aho=LinAho,
                    fecha_inicial=asignar_fecha(row['s08fecini'],'%m/%d/%Y'),tiae=0)
            TasLinAho.fecha_final = asignar_fecha(row['s08fecfin'],'%m/%d/%Y')
            TasLinAho.tiae = row['s08tasintanu']
            TasLinAho.save()
    print('          ',datetime.now())    

def ret_fue_aho():
    print('ret_fue_aho  ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s11parretfue.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            LinAho = justo.LINEAS_AHORRO.objects.filter(cliente=Cliente,cod_lin_aho=row['s11tipcta']).first()
            if LinAho == None:
                continue
            RetFueAho = justo.RET_FUE_AHO.objects.filter(lin_aho=LinAho,
                    fecha_inicial=asignar_fecha(row['s11fecini'],'%m/%d/%Y')).first()
            if RetFueAho == None:
                RetFueAho = justo.RET_FUE_AHO.objects.create(lin_aho=LinAho,
                    fecha_inicial=asignar_fecha(row['s11fecini'],'%m/%d/%Y'))
            RetFueAho.fecha_final = asignar_fecha(row['s11fecfin'],'%m/%d/%Y')
            RetFueAho.bas_liq_int = row['s11basliqdia'] 
            RetFueAho.tas_liq_rf = row['s11tasintretfue']
            RetFueAho.save()
    print('              ',datetime.now())    

def ctas_aho():
    print('Ctas Aho     ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/S05CTAAHO.CSV', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            Socio = justo.ASOCIADOS.objects.filter(
                oficina = Oficina,cod_aso = row['s05codsoc']).first()
            if Socio == None:
                continue
            LinAho = justo.LINEAS_AHORRO.objects.filter(cliente = Cliente,cod_lin_aho = row['s05tipcta']).first()
            if LinAho == None:
                continue
            CtaAho = justo.CTAS_AHORRO.objects.filter(
                oficina = Oficina,num_cta = row['s05numcta']).first()
            if CtaAho == None:
                print('Nueva Cta Aho ',row['s05numcta'])
                CtaAho = justo.CTAS_AHORRO.objects.create(
                        oficina = Oficina,num_cta = row['s05numcta'],lin_aho = LinAho,asociado = Socio)
            CtaAho.est_cta = row['s05estado']
            CtaAho.cod_imp = row['s05codimpcon']
            CtaAho.fec_apertura = asignar_fecha(row['s05fecape'],'%m/%d/%Y')
            CtaAho.fec_cancela = asignar_fecha('01/01/1900','%m/%d/%Y')
            CtaAho.exc_tas_mil = row['s05exegmf']
            CtaAho.fec_ini_exc = asignar_fecha(row['s05feciniexc'],'%m/%d/%Y')
            CtaAho.save()
    print('Fin ctas aho  ',datetime.now())    

def cta_cdat():
    print('CDAT    ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s20cdat.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            CtaAho = justo.CTAS_AHORRO.objects.filter(
                oficina = Oficina,num_cta = row['s20numcta']).first()
            if CtaAho == None:
                continue
            CtaCdat = justo.CTA_CDAT.objects.filter(cta_aho = CtaAho,ampliacion=row['s20ampliacion']).first()
            if CtaCdat == None:
                CtaCdat = justo.CTA_CDAT.objects.create(cta_aho = CtaAho,ampliacion=row['s20ampliacion']) 
            CtaCdat.valor = row['s20monto']
            CtaCdat.fecha = asignar_fecha(row['s20fecha'],'%m/%d/%Y')
            CtaCdat.plazo_mes = row['s20plazomes']
            CtaCdat.tiae = row['s20tasintanuefe']
            CtaCdat.Periodicidad = row['s20periodicidad']
            CtaCdat.cta_int_ret = row['s20ctaafeint']
            CtaCdat.aplicado = row['s20aplicado']
            CtaCdat.save()
    print('              ',datetime.now())    

def cta_cdat_amp():
    print('CDAT AMP  ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s21liqintcda.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            CtaAho = justo.CTAS_AHORRO.objects.filter(
                oficina = Oficina,num_cta = row['s21numcta']).first()
            if CtaAho == None:
                continue
            CtaCda = justo.CTA_CDAT.objects.filter(cta_aho = CtaAho,ampliacion=row['s21ampliacion']).first()
            if CtaCda == None:
                CtaCda = justo.CTA_CDAT.objects.create(cta_aho = CtaAho,ampliacion=row['s21ampliacion']) 
            if CtaCda == None:
                continue
            CtaCdaAmp = justo.CTA_CDAT_AMP.objects.filter(cta_aho = CtaAho,cta_amp = CtaCda,fecha = asignar_fecha(row['s21fecha'],'%m/%d/%Y')).first()
            if CtaCdaAmp == None:
                CtaCdaAmp = justo.CTA_CDAT_AMP.objects.create(cta_aho = CtaAho,cta_amp = CtaCda,fecha = asignar_fecha(row['s21fecha'],'%m/%d/%Y'))
            CtaCdaAmp.num_liq = row['s21numliqint']
            CtaCdaAmp.valor = row['s21valor']
            CtaCdaAmp.cta_aho_afe = row['s21ctaafe']
            CtaCdaAmp.clase = row['s21clase']
            CtaCdaAmp.documento = row['s21documento']
            CtaCdaAmp.aplicado = row['s21aplicado'][:1]
            CtaCdaAmp.save()
    print('            ',datetime.now())    

def cta_cda_liq():
    print('CDAT liq   ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s39histcdat.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            CtaAho = justo.CTAS_AHORRO.objects.filter(
                oficina = Oficina,num_cta = row['s39numcta']).first()
            if CtaAho == None:
                continue
            CtaCda = justo.CTA_CDAT.objects.filter(cta_aho = CtaAho,ampliacion=row['s39ampliacion']).first()
            if CtaCda == None:
                continue
            CtaCdatAmp = justo.CTA_CDAT_AMP.objects.filter(cta_aho = CtaAho,cta_amp =CtaCda).first()
            if CtaCdatAmp == None:
                continue 
            CtaCdatLiq = justo.CTA_CDAT_LIQ.objects.filter(cta_aho = CtaAho,cta_amp = CtaCdatAmp,
                fecha = asignar_fecha(row['s39fecha'],'%m/%d/%Y'),tip_liq = row['s39tipo']).first()
            if CtaCdatLiq == None:
                CtaCdatLiq = justo.CTA_CDAT_LIQ.objects.create(cta_aho = CtaAho,cta_amp = CtaCdatAmp,
                    fecha = asignar_fecha(row['s39fecha'],'%m/%d/%Y'),tip_liq = row['s39tipo'])
            CtaCdatLiq.Val_int = row['s39interes']
            CtaCdatLiq.Val_ret = row['s39retfue']
            CtaCdatLiq.Val_ret_nue = row['s39retfuenue']
            CtaCdatLiq.aplicado = row['s39aplicado']
            CtaCdatLiq.save()
    print('              ',datetime.now())    

def ImpIntDiaAho():
    print('IntCtaAho ... ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    CentroCosto = justo.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    with open('c:/ajusto/csv/xMovIntCtaAho.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            if int(row['per_con']) < 2017:
                continue
            Tercero = justo.TERCEROS.objects.filter(cliente=Cliente,doc_ide=row['nit']).first()
            if Tercero == None:
                print('Tercero No Existe  ',row['nit'])
                continue
            Socio = justo.ASOCIADOS.objects.filter(oficina=Oficina,tercero=Tercero).first()
            if Socio == None:
                print('Asociado No Existe  ',row['nit'])
                continue
            CtaCon = justo.PLAN_CTAS.objects.filter(cliente = Cliente,per_con=row['per_con'],cod_cta=row['cod_cta']).first()
            if CtaCon == None:
                print('No Existe Cta Con ',row['cod_cta'],'  en el Periodo  ',row['per_con'])
                continue
            Docto = justo.DOCTO_CONTA.objects.filter(oficina = Oficina,per_con = row['per_con'],codigo = 131).first()
            HecEco = justo.HECHO_ECONO.objects.filter(docto_conta = Docto,numero = row['numero']).first()
            if HecEco == None:
                continue
            if row['cod_cta'][:1] != '2':
                DetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = CtaCon,tercero = Socio.tercero).first()
                if DetEco == None:
                    DetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = CtaCon,tercero = Socio.tercero)
                DetEco.detalle = 'Anexo IntCta '    
                DetEco.debito = row['debito']
                DetEco.credito = row['credito']
                DetEco.item_concepto = 'AhoAne'
                DetEco.save()
            else:
                ImpCon = justo.IMP_CON_LIN_AHO.objects.filter(Q(ctaafeact=row['cod_cta']) | Q(ctaafeina=row['cod_cta'])).first()
                if ImpCon == None:
                    continue
                CtaAho = justo.CTAS_AHORRO.objects.filter(oficina = Oficina,asociado = Socio,lin_aho = ImpCon.linea_ahorro,cod_imp = ImpCon.cod_imp).first()
                if CtaAho == None:
                    continue
                DetPro = justo.DETALLE_PROD.objects.filter(hecho_econo = HecEco,producto = 'AH',concepto = 'AHO',subcuenta = CtaAho.num_cta,centro_costo = CentroCosto).first()
                if DetPro == None:
                    DetPro = justo.DETALLE_PROD.objects.create(hecho_econo = HecEco,producto = 'AH',concepto = 'AHO',subcuenta = CtaAho.num_cta,centro_costo = CentroCosto)
                DetPro.valor = int(float(row['debito'])) - int(float(row['credito']))
                DetPro.oficina = Oficina
                DetPro.save()
                DetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = CtaCon,tercero = Socio.tercero).first()
                if DetEco == None:
                    DetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = CtaCon,tercero = Socio.tercero)
                DetEco.detalle = 'Int Cta Aho = '+CtaAho.num_cta
                DetEco.detalle_prod = DetPro
                DetEco.item_concepto = 'IntCta'
                DetEco.debito = row['debito']
                DetEco.credito = row['credito']
                DetEco.save()
    print('          ... ',datetime.now())

def imp_con_cre():
    print('Imp Creditos   ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s16impconcre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            ImpConCre = justo.IMP_CON_CRE.objects.filter(cliente=Cliente,cod_imp = row['s16codimp']).first()
            if ImpConCre == None:
                ImpConCre = justo.IMP_CON_CRE.objects.create(cliente=Cliente,cod_imp = row['s16codimp'])
            ImpConCre.descripcion = row['s16descripcion']
            ImpConCre.kpte_cap = '42251201'
            ImpConCre.kpte_ic = '51155901'
            ImpConCre.kdet_gen_adi = row['s16ctaprogenadi'] 
            ImpConCre.kdet_gen = row['s16ctaprogen']
            ImpConCre.kdet_gen_gas = row['s16ctagasprogen']
            ImpConCre.kdet_gen_rec = row['s16ctarecprogen']
            ImpConCre.kdet_ind_gas = row['s16ctagasproind']
            ImpConCre.kdet_ind_rec = row['s16ctarecproind']
            ImpConCre.kdpp_ic = ''
            ImpConCre.save()
    print('             ',datetime.now())

def imp_con_cre_int():
    print('Imp Int Creditos',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s18impconcrecapcat.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            ImpConCreInt = justo.IMP_CON_CRE_INT.objects.filter(cliente=Cliente,cod_imp = row['s18codimp'],categoria = row['s18codcat']).first()
            if ImpConCreInt == None:
                ImpConCreInt = justo.IMP_CON_CRE_INT.objects.create(cliente=Cliente,cod_imp = row['s18codimp'],categoria = row['s18codcat'])
            ImpConCreInt.kcta_con = row['s18ctacon']
            ImpConCreInt.kcta_pro_ind = row['s18ctapro']
            ImpConCreInt.porcen_det = row['s18porpro']
            ImpConCreInt.save()
    print('   Continua  ',datetime.now())    
    with open('c:/ajusto/csv/s34asicatint.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            if row['s34cuenta'] not in ["Ingreso","CtaPte","CxP","Error","IngRec","OrdenI"]:
                if row['s34cuenta'] == 'OrdenC':
                    xCat = 'C'
                elif row['s34cuenta'] == 'OrdenD':
                    xCat = 'D'
                elif row['s34cuenta'] == 'OrdenE':
                    xCat = 'E'
                elif row['s34cuenta'] == 'OrdenF':
                    xCat = 'F'
                else:
                    xCat = row['s34cat']
                ImpConCreInt = justo.IMP_CON_CRE_INT.objects.filter(cliente=Cliente,cod_imp = row['s34codimpcon'],categoria = xCat).first()
                if ImpConCreInt == None:
                    ImpConCreInt = justo.IMP_CON_CRE_INT.objects.create(cliente=Cliente,cod_imp = row['s34codimpcon'],categoria = xCat)
                elif row['s34cuenta'] == 'CxCa':
                    ImpConCreInt.kcxc_ic = row['s34codcta']
                elif row['s34cuenta'] == 'CxCb':
                    ImpConCreInt.kcxc_ic = row['s34codcta']
                elif row['s34cuenta'] == 'CxCc':
                    ImpConCreInt.kcxc_ic = row['s34codcta']
                elif row['s34cuenta'] == 'CxCd':
                    ImpConCreInt.kcxc_ic = row['s34codcta']
                elif row['s34cuenta'] == 'CxCe':
                    ImpConCreInt.kcxc_ic = row['s34codcta']
                elif row['s34cuenta'] == 'CxCe':
                    ImpConCreInt.kcxc_ic = row['s34codcta']
                elif row['s34cuenta'] == 'CxCf':
                    ImpConCreInt.kcxc_ic = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenC':
                    ImpConCreInt.kord_ic = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenD':
                    ImpConCreInt.kord_ic = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenE':
                    ImpConCreInt.kord_ic = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenF':
                    ImpConCreInt.kord_ic = row['s34codcta']
                ImpConCreInt.save()
            else:
                ImpConCre = justo.IMP_CON_CRE.objects.filter(cliente=Cliente,cod_imp = row['s34codimpcon']).first()
                if ImpConCre == None:
                    ImpConCre = justo.IMP_CON_CRE.objects.create(cliente=Cliente,cod_imp = row['s34codimpcon'])
                if row['s34cuenta'] == 'CtaPte':
                    ImpConCre.kcta_pte_int = row['s34codcta']
                elif row['s34cuenta'] == 'Ingreso':
                    ImpConCre.kcta_ingreso = row['s34codcta']
                elif row['s34cuenta'] == 'CxP':
                    ImpConCre.cta_por_pag = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenI':
                    ImpConCre.kord_ic = row['s34codcta']
                elif row['s34cuenta'] == 'Error':
                    ImpConCre.cta_val = row['s34codcta']
                ImpConCre.save()
    print('             ',datetime.now())

def destino_cre():
    print('des Creditos   ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s17descre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            DesCre = justo.DESTINO_CRE.objects.filter(cliente=Cliente,codigo = ord(row['s17coddescre'])).first()
            if DesCre == None:
                DesCre = justo.DESTINO_CRE.objects.create(cliente=Cliente,codigo = ord(row['s17coddescre']))
            DesCre.descripcion = row['s17descripcion']
            DesCre.save()
    print('des Creditos   ',datetime.now())    

def cat_des_dia_cre():
    print('des Dia Creditos   ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s19catdescre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            CatDesDiaCre = justo.CAT_DES_DIA_CRE.objects.filter(cliente=Cliente,codigo = ord(row['s19coddes']),categoria = row['s19codcat']).first()
            if CatDesDiaCre == None:
                CatDesDiaCre = justo.CAT_DES_DIA_CRE.objects.create(cliente=Cliente,codigo = ord(row['s19coddescre']),categoria = row['s19codcat'])
            CatDesDiaCre.minimo_dias = row['s19diamin']
            CatDesDiaCre.maximo_dias = row['s19diamax']
            CatDesDiaCre.save()
    print('        ',datetime.now())    

def lineas_credito():
    print('Lineas Credito   ',datetime.now())    
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s14lincre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            LinCre = justo.LINEAS_CREDITO.objects.filter(cliente=Cliente,cod_lin_cre = ord(row['s14codlincre'])).first()
            if LinCre == None:
                LinCre = justo.LINEAS_CREDITO.objects.create(cliente=Cliente,cod_lin_cre = ord(row['s14codlincre']))
            LinCre.descripcion = row['s14descripcion']
            LinCre.tas_int_anu = row['s14tasintanu']
            LinCre.tas_int_mor = row['s14tasintmor']
            LinCre.por_pol = row['s14porpol']
            LinCre.por_des_pp = row['s14pordespropag']
            LinCre.dia_con_int_mor = row['s14diaconintmor']
            LinCre.save()
    print('Lineas Credito   ',datetime.now()) 

def creditos():
    print('Creditos....  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    
    with open('c:/ajusto/csv/s12creditos.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Socio = justo.ASOCIADOS.objects.filter(oficina=Oficina,cod_aso=row['s12codsoc']).first()
            if Socio == None:
                print('Socio con Docto ',row['s12codsoc'], ' No existe con el credito ',row['s12codcre'])
                continue
            Credito = justo.CREDITOS.objects.filter(oficina=Oficina,cod_cre=row['s12codcre']).first()
            if Credito == None:
                Credito = justo.CREDITOS.objects.create(oficina=Oficina,cod_cre=row['s12codcre'],socio=Socio)
            ImpConCre = justo.IMP_CON_CRE.objects.filter(cliente = Cliente,cod_imp = row['s12codimpcon']).first()
            if ImpConCre == None:
                ImpConCre = justo.IMP_CON_CRE.objects.create(cliente = Cliente,cod_imp = row['s12codimpcon'])
            Credito.imputacion = ImpConCre
            Credito.cod_lin_cre = ord(row['s12codlincre'])
            Credito.cap_ini = row['s12capini'] 
            Credito.libranza = row['s12libranza']
            Credito.pagare = row['s12pagare']
            Credito.termino = row['s12termino']
            Credito.for_pag = row['s12forpag']
            Credito.fec_des = asignar_fecha(row['s12fecdes'],'%m/%d/%Y')
            Credito.fec_pag_ini = asignar_fecha(row['s12fecpagini'],'%m/%d/%Y')
            Credito.fec_ree = asignar_fecha('01/01/1900','%m/%d/%Y')
            Credito.fec_ven = asignar_fecha(row['s12fecpagini'],'%m/%d/%Y')
            Credito.fec_ult_pag = asignar_fecha(row['s12fecultpag'],'%m/%d/%Y')
            Credito.val_cuo_ini = row['s12valcuo']
            Credito.val_cuo_act = row['s12valcuo']
            Credito.num_cuo_ini = row['s12numcuo']
            Credito.num_cuo_act = row['s12numcuo']
            Credito.num_cuo_gra = 0
            Credito.per_ano = row['s12perano']
            Credito.tian_ic_ini = row['s12tasintanuini']
            Credito.tian_ic_act = row['s12tasintanu']
            Credito.tian_im = row['s12tasintmor']
            Credito.tian_pol_seg = row['s12porpol']
            Credito.por_des_pro_pag = 0
            Credito.decreciente = 'N'
            Credito.estado = row['s12estjur'].strip()
            Credito.est_jur = row['s12estjur'].strip()
            Credito.cat_nue = row['s12nvocat'].strip()
            Credito.rep_cen_rie = row['s12repcenrie'][:0]
            Credito.val_gar_hip = row['s12valcomgarhip']
            Credito.mat_inm_gar = row['s12matinmgarhip']
            Credito.num_pol_gar_hip = row['s12numpolgh']
            Credito.figarantias = row['s12figrantias'][:0]
            Credito.save()
    with open('c:/ajusto/csv/s10codeudor.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Credito = justo.CREDITOS.objects.filter(oficina=Oficina,cod_cre=row['s10codcre']).first()
            if Credito != None:
                if Credito.val_gar_hip == 0:
                    Credito.tip_gar = '1'
                else:
                    Credito.tip_gar = '15'
                Credito.save()
                GarNoIdo = justo.GAR_NO_IDONEA.objects.filter(oficina = Oficina,credito = Credito,doc_ide = row['s10nit']).first()
                if GarNoIdo == None:
                    GarNoIdo = justo.GAR_NO_IDONEA.objects.create(oficina = Oficina,credito = Credito,doc_ide = row['s10nit'])
                    GarNoIdo.tipo = 'C' 
                    GarNoIdo.save()
    print('              ',datetime.now())

def importar_mov_cre():
    print('importar_mov_cre  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/xmovcre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            xCredito = justo.CREDITOS.objects.filter(oficina=Oficina,cod_cre=row['codcre']).first()
            xEsta = ' '
            if xCredito == None:
                print('Credito No Registrado ',row['codcre'])
                xEsta = 'N'
            xCredito  = justo.XMOV_CRE.objects.create(cod_cre=row['codcre'],
                        est_jur = row['esjur'],
                        fec_ulp_pag = asignar_fecha(row['felultpag'],'%m/%d/%Y'),
                        min_fecha = asignar_fecha(row['min_fecha'],'%m/%d/%Y'),
                        max_fecha = asignar_fecha(row['max_fecha'],'%m/%d/%Y'),
                        clase = row['s13clase'],
                        docto = row['s13documen'],
                        tip_mov = row['s13tipmov'],
                        fecha = asignar_fecha(row['s13fecha'],'%m/%d/%Y'),
                        capital = row['s13capital'],
                        int_cor = row['s13intcor'],
                        int_mor = row['s13intmor'],
                        acreed = row['s13acreedo'],
                        estado = xEsta)
            xCredito.save()
    print('                  ',datetime.now())

def grabar_causa_cre():
    print('Grabar Causa_cre  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    xMovCaus = justo.XMOV_CRE.objects.filter(tip_mov='2')
    for xMovCau in xMovCaus:
        xCuota = int(float(xMovCau.docto[1:8]))
        CreditoCausa = justo.CREDITOS_CAUSA.objects.filter(oficina=Oficina,cod_cre = xMovCau.cod_cre,
            comprobante=None,cuota=xCuota).first()
        if CreditoCausa == None:
            CreditoCausa = justo.CREDITOS_CAUSA.objects.create(oficina=Oficina,cod_cre = xMovCau.cod_cre,
            comprobante=None,cuota=xCuota)
        CreditoCausa.fecha = xMovCau.fecha 
        CreditoCausa.capital = xMovCau.capital
        CreditoCausa.int_cor = xMovCau.int_cor
        CreditoCausa.int_mor = xMovCau.int_mor
        CreditoCausa.pol_seg = 0
        CreditoCausa.save()
        xMovCau.estado= 'V'
        xMovCau.save()
    print('Grabar            ',datetime.now())

def detalle_prod():
    print('Detalle_prod ... ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    CentroCosto = justo.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    with open('c:/ajusto/csv/xc05movite.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            if row['c05clase'] == '7' or row['c05clase'] == 'C' or row['c05clase'] == 'T':
                continue
            DocZep = justo.XDOC_ZEP.objects.filter(per_con=row['c05fecha'],clase_zep=row['c05clase']).first()
            if DocZep == None:
                print('No Doc Zep',row['c05fecha'],row['c05clase'],row['c05documen'],row['c05concept'])
                continue
            DocCon = justo.DOCTO_CONTA.objects.filter(oficina=Oficina,per_con=DocZep.per_con,
                   codigo=DocZep.doc_ds).first()
            if DocCon == None:
                print('No Doc Justo',row['c05fecha'],row['c05clase'],row['c05documen'],row['c05concept'])
                continue
            HechEco = justo.HECHO_ECONO.objects.filter(docto_conta=DocCon,numero=int(row['c05documen'])).first()
            if HechEco == None:
                print('No Comp Justo',row['c05fecha'],row['c05clase'],row['c05documen'],row['c05concept'])
                continue
            xPro = '  '
            if row['c05concept'] == 'AHO' or row['c05concept'] == 'AHOCH':
                xPro = 'AH'
            elif row['c05concept'] == 'APOR' or row['c05concept'] == 'APORE' or row['c05concept'] == 'APORO':
                xPro = 'AP'
            elif row['c05concept'] == 'CUOTA' or row['c05concept'] == 'ABOCA' or row['c05concept'] == 'ABOCU'  or row['c05concept'] == 'DESEM'  or row['c05concept'] == 'CASTI'  or row['c05concept'] == 'CONDO':
                xPro = 'CR'
            DetProd = justo.DETALLE_PROD.objects.filter(hecho_econo=HechEco,producto=xPro,
                concepto = row['c05concept'],subcuenta=row['c05subcuen']).first()
            if DetProd == None:
                DetProd = justo.DETALLE_PROD.objects.create(hecho_econo=HechEco,producto=xPro,
                        concepto = row['c05concept'],subcuenta=row['c05subcuen'])
            DetProd.oficina = Oficina       # para mejorar la velocidad
            DetProd.valor = row['c05valor']
            DetProd.centro_costo = CentroCosto
            DetProd.save()
    print('             ... ',datetime.now())

def grabar_credito_mod():
    print('Grabar credito Mod  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    xMovCams = justo.XMOV_CRE.objects.filter(tip_mov__in=  ['3','4','5'])
    for xMovCam in xMovCams:
        try:
            numero = int(xMovCam.docto)  # Intenta convertir la cadena a un entero
        except ValueError:
            xMovCam.estado = '1'
            xMovCam.save()
            continue
        xper_con = xMovCam.fecha.year
        Comprobs = justo.HECHO_ECONO.objects.filter(numero = int(xMovCam.docto),fecha = xMovCam.fecha)
        if not Comprobs.exists():
            xMovCam.estado = '2'
            xMovCam.save()
            continue
        for Comprob in Comprobs:
            if Comprob.docto_conta.oficina != Oficina:
                continue
            DetProd = justo.DETALLE_PROD.objects.filter(hecho_econo=Comprob,producto='CR',subcuenta=xMovCam.cod_cre,
                    concepto__in = ['CUOTA','ABOCA','ABOCU','CASTI','CONDO']).first()
            if DetProd != None:
                xMovCam.estado = 'K'
                xMovCam.save()
                CamCre = justo.CAMBIOS_CRE.objects.filter(det_pro = DetProd).first()
                if CamCre == None:
                    CamCre = justo.CAMBIOS_CRE.objects.create(det_pro = DetProd)
                if DetProd.concepto in ['CUOTA','ABOCA','ABOCU']:
                    CamCre.tip_cam = '2' 
                elif DetProd.concepto in ['CASTI']:
                    CamCre.tip_cam = '4'
                elif DetProd.concepto in ['CONDO']:
                    CamCre.tip_cam = '4'
                CamCre.fecha = xMovCam.fecha   
                CamCre.capital = xMovCam.capital
                CamCre.int_cor = xMovCam.int_cor
                CamCre.int_mor = xMovCam.int_mor
                CamCre.pol_seg = 0
                CamCre.acreedor = xMovCam.acreed
                CamCre.save()
                break
        if xMovCam.estado != 'K':
            xMovCam.estado = '3'
            xMovCam.save()
    print('       credito Mod  ',datetime.now())

def grabar_credito_mod2():
    print('Grabar credito Mod2  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    xMovCams = justo.XMOV_CRE.objects.filter(clase = '6' ,estado = '2')
    for xMovCam in xMovCams:
        try:
            numero = int(xMovCam.docto)  # Intenta convertir la cadena a un entero
        except ValueError:
            xMovCam.estado = '1'
            xMovCam.save()
            continue
        xper_con = xMovCam.fecha.year
        xFecFin = xMovCam.fecha + timedelta(days=31)
        query = Q(numero=int(xMovCam.docto)) & Q(fecha__range=(xMovCam.fecha,xFecFin))
        Comprobs = justo.HECHO_ECONO.objects.filter(query)
        if not Comprobs.exists():
            xMovCam.estado = '2'
            xMovCam.save()
            continue
        for Comprob in Comprobs:
            if Comprob.docto_conta.oficina != Oficina:
                continue
            DetProd = justo.DETALLE_PROD.objects.filter(hecho_econo=Comprob,producto='CR',subcuenta=xMovCam.cod_cre,
                    concepto__in = ['CUOTA','ABOCA','ABOCU','CASTI','CONDO']).first()
            if DetProd != None:
                xMovCam.estado = 'Z'
                xMovCam.save()
                CamCre = justo.CAMBIOS_CRE.objects.filter(det_pro = DetProd).first()
                if CamCre == None:
                    CamCre = justo.CAMBIOS_CRE.objects.create(det_pro = DetProd)
                if DetProd.concepto in ['CUOTA','ABOCA','ABOCU']:
                    CamCre.tip_cam = '2' 
                elif DetProd.concepto in ['CASTI']:
                    CamCre.tip_cam = '4'
                elif DetProd.concepto in ['CONDO']:
                    CamCre.tip_cam = '4'
                CamCre.fecha = xMovCam.fecha   
                CamCre.capital = xMovCam.capital
                CamCre.int_cor = xMovCam.int_cor
                CamCre.int_mor = xMovCam.int_mor
                CamCre.pol_seg = 0
                CamCre.acreedor = xMovCam.acreed
                CamCre.save()
                break
        if xMovCam.estado != 'Z':
            xMovCam.estado = '3'
            xMovCam.save()
    print('       credito Mod  ',datetime.now())

def asigna_con_cre():
    print('Recorrido...  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    xMovCres = justo.XMOV_CRE.objects.filter(tip_mov__in = ['6','7','8','9','A'])   #,cod_cre = '132258',docto = '397335')
    for xMovCre in xMovCres:
        if xMovCre.cod_cre == '132258' and xMovCre.docto == '393495':
            i = 1        
        xFecha = xMovCre.fecha
        xDocto = xMovCre.docto
        xPercon = xMovCre.fecha.year
        xDocZep = justo.XDOC_ZEP.objects.filter(per_con=xPercon,clase_zep = xMovCre.clase).first()
        if xDocZep == None:
            xMovCre.estado = '1'
            xMovCre.save()
            continue
        xDocConta = justo.DOCTO_CONTA.objects.filter(oficina=Oficina,per_con=xPercon,codigo=xDocZep.doc_ds).first()
        if xDocConta == None:
            xMovCre.estado = '2'
            xMovCre.save()
            continue
        xHechoEco = justo.HECHO_ECONO.objects.filter(docto_conta=xDocConta,numero=xDocto).first()
        if xHechoEco == None:
            xMovCre.estado = '3'
            xMovCre.save()
            continue
        if xMovCre.tip_mov == '9':
            xConcepto = 'CUOTA'
        elif xMovCre.tip_mov == '8':
            xConcepto = 'ABOCA'
        elif xMovCre.tip_mov  == '7':
            xConcepto = 'CONDO'    
        elif xMovCre.tip_mov  == '6':
            xConcepto = 'CASTI'
        elif xMovCre.tip_mov  == 'A':
            xConcepto = 'ABOCU'
        DetProd = justo.DETALLE_PROD.objects.filter(hecho_econo = xHechoEco, concepto = xConcepto,
                            subcuenta = xMovCre.cod_cre).first()
        if DetProd == None:
            xMovCre.estado = '4'
            xMovCre.save()
            continue#
        Credito = justo.CREDITOS.objects.filter(oficina = Oficina,cod_cre = xMovCre.cod_cre).first()    
        if Credito == None:
            xMovCre.estado = '5'
            xMovCre.save()
            continue
        Tercero = Credito.socio.tercero
        if Tercero == None:
            xMovCre.estado = '6'
            xMovCre.save()
            continue
        if xMovCre.capital != 0: 
            Cuenta = justo.PLAN_CTAS.objects.filter(cliente=Cliente,per_con=xPercon,cod_cta='14433501').first()
            if Cuenta == None:
                xMovCre.estado = '7'
                xMovCre.save()
                continue
#  si Todo esto se cumple debe haber un asiento que refleje el movimiento del credito en capital
            HalDetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = xHechoEco,cuenta=Cuenta,
                                tercero = Tercero).first()
            if HalDetEco == None:
                xMovCre.estado = '8'
                xMovCre.save()
                continue
            if xMovCre.capital < 0 and xMovCre.capital == -HalDetEco.credito and (HalDetEco.valor_1 == 0 and HalDetEco.valor_2 == 0):
                HalDetEco.detalle_prod = DetProd
                HalDetEco.item_concepto = 'Kapita'
                HalDetEco.detalle = 'Ok ' + xMovCre.cod_cre
                HalDetEco.valor_2 = -xMovCre.capital
                HalDetEco.save()
            else:
                NvoDetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = xHechoEco,cuenta=Cuenta,
                               tercero = Tercero,detalle_prod = DetProd)
                NvoDetEco.item_concepto = 'Kapita'
                NvoDetEco.detalle = 'Nuevo ' + xMovCre.cod_cre
                NvoDetEco.debito = 0
                NvoDetEco.credito = 0
                NvoDetEco.valor_1 = 0
                NvoDetEco.valor_2 = -xMovCre.capital
                NvoDetEco.save()
        if xMovCre.int_cor != 0: 
            Cuenta = justo.PLAN_CTAS.objects.filter(cliente=Cliente,per_con=xPercon,cod_cta ='14433001').first()
            if Cuenta == None:
                xMovCre.estado = '7'
                xMovCre.save()
                continue
#  si Todo esto se cumple debe haber un asiento que refleje el movimiento del credito en IntCor
            HalDetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = xHechoEco,cuenta=Cuenta,
                                tercero = Tercero).first()
            if HalDetEco == None:
                xMovCre.estado = '8'
                xMovCre.save()
                continue
            if xMovCre.int_cor < 0 and xMovCre.int_cor == -HalDetEco.credito and (HalDetEco.valor_1 == 0 and HalDetEco.valor_2 == 0):
                HalDetEco.detalle_prod = DetProd
                HalDetEco.item_concepto = 'IntCor'
                HalDetEco.detalle = 'Ok ' + xMovCre.cod_cre
                HalDetEco.valor_2 = -xMovCre.int_cor
                HalDetEco.save()
            elif xMovCre.int_cor < 0:
                HalDetEco.save()
                NvoDetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = xHechoEco,cuenta=Cuenta,
                            tercero = Tercero,detalle_prod = DetProd)
                NvoDetEco.item_concepto = 'IntCor'
                NvoDetEco.detalle = 'Nuevo1 ' + xMovCre.cod_cre
                NvoDetEco.debito = 0
                NvoDetEco.credito = 0
                NvoDetEco.valor_1 = 0
                NvoDetEco.valor_2 = -xMovCre.int_cor
                NvoDetEco.save()
            if xMovCre.int_cor > 0 and xMovCre.int_cor == HalDetEco.debito and (HalDetEco.valor_1 == 0 and HalDetEco.valor_2 == 0):
                HalDetEco.detalle_prod = DetProd
                HalDetEco.item_concepto = 'IntCor'
                HalDetEco.detalle = 'Ok ' + xMovCre.cod_cre
                HalDetEco.valor_1 = xMovCre.int_cor
                HalDetEco.save()     
            elif xMovCre.int_cor > 0:
                NvoDetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = xHechoEco,cuenta=Cuenta,
                            tercero = Tercero,detalle_prod = DetProd)
                NvoDetEco.item_concepto = 'IntCor'
                NvoDetEco.detalle = 'Nuevo1 ' + xMovCre.cod_cre
                NvoDetEco.debito = 0
                NvoDetEco.credito = 0
                NvoDetEco.valor_1 = xMovCre.int_cor
                NvoDetEco.valor_2 = 0
                NvoDetEco.save()
        if xMovCre.int_mor != 0: 
            Cuentas = justo.PLAN_CTAS.objects.filter(cliente=Cliente,per_con=xPercon,cod_cta__in = ['41504001','41503501'])
            HalDetEco = None
            for Cuenta in Cuentas:
                HalDetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = xHechoEco,cuenta=Cuenta,
                                tercero = Tercero,detalle_prod = None).first()
                if HalDetEco != None:
                    break
            if HalDetEco == None:
                xMovCre.estado = '7'
                xMovCre.save()
                continue
            HalDetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = xHechoEco,cuenta=Cuenta,
                                tercero = Tercero).first()
            if HalDetEco == None:
                xMovCre.estado = '8'
                xMovCre.save()
                continue
            if xMovCre.int_mor < 0 and xMovCre.int_mor == -HalDetEco.credito and (HalDetEco.valor_1 == 0 and HalDetEco.valor_2 == 0):
                HalDetEco.detalle_prod = DetProd
                HalDetEco.item_concepto = 'IntMor'
                HalDetEco.detalle = 'Ok ' + xMovCre.cod_cre
                HalDetEco.valor_2 = -xMovCre.int_mor
                HalDetEco.save()
            elif xMovCre.int_mor < 0 :
                NvoDetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = xHechoEco,cuenta=Cuenta,
                            tercero = Tercero,detalle_prod = DetProd)
                NvoDetEco.item_concepto = 'IntMor'
                NvoDetEco.detalle = 'Nuevo1 ' + xMovCre.cod_cre
                NvoDetEco.debito = 0
                NvoDetEco.credito = 0
                NvoDetEco.valor_1 = 0
                NvoDetEco.valor_2 = -xMovCre.int_mor
                NvoDetEco.save()
            if xMovCre.int_mor >= 0 and xMovCre.int_mor == HalDetEco.credito and (HalDetEco.valor_1 == 0 and HalDetEco.valor_2 == 0):
                HalDetEco.detalle_prod = DetProd
                HalDetEco.item_concepto = 'IntMor'
                HalDetEco.detalle = 'Ok ' + xMovCre.cod_cre
                HalDetEco.valor_1 = xMovCre.int_mor
                HalDetEco.save()          
            elif xMovCre.int_mor >= 0:
                HalDetEco.detalle = 'Varios IntMor +'
                HalDetEco.save()
                NvoDetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = xHechoEco,cuenta=Cuenta,
                            tercero = Tercero,detalle_prod = DetProd)
                NvoDetEco.item_concepto = 'IntMor'
                NvoDetEco.detalle = 'Nuevo1 ' + xMovCre.cod_cre
                NvoDetEco.debito = 0
                NvoDetEco.credito = 0
                NvoDetEco.valor_1 = xMovCre.int_mor
                NvoDetEco.valor_2 = 0
                NvoDetEco.save()
        if xMovCre.acreed != 0: 
            Cuenta = justo.PLAN_CTAS.objects.filter(cliente=Cliente,per_con=xPercon,cod_cta = '24459501').first()
            if Cuenta == None:
                xMovCre.estado = '7'
                xMovCre.save()
                continue
            HalDetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = xHechoEco,cuenta=Cuenta,
                                tercero = Tercero).first()
            if HalDetEco == None:
                xMovCre.estado = '8'
                xMovCre.save()
                continue
            if xMovCre.acreed < 0 and xMovCre.acreed == -HalDetEco.credito and (HalDetEco.valor_1 == 0 and HalDetEco.valor_2 == 0):
                HalDetEco.detalle_prod = DetProd
                HalDetEco.item_concepto = 'Acreed'
                HalDetEco.detalle = 'Ok ' + xMovCre.cod_cre
                HalDetEco.valor_2 = -xMovCre.acreed
                HalDetEco.save()
            elif xMovCre.acreed > 0 and xMovCre.acreed == HalDetEco.debito:
                HalDetEco.detalle_prod = DetProd
                HalDetEco.item_concepto = 'Acreed'
                HalDetEco.detalle = 'Ok ' + xMovCre.cod_cre
                HalDetEco.valor_1 = xMovCre.acreed
                HalDetEco.save()          
            else:
                NvoDetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = xHechoEco,cuenta=Cuenta,
                                tercero = Tercero,detalle_prod = DetProd)
                NvoDetEco.item_concepto = 'Acreed'
                NvoDetEco.detalle = 'Nuevo ' + xMovCre.cod_cre
                NvoDetEco.debito = 0
                NvoDetEco.credito = 0
                NvoDetEco.valor_1 = 0
                NvoDetEco.valor_2 = -xMovCre.acreed
                NvoDetEco.save()
        xMovCre.estado = 'V'
        xMovCre.save()
    print('Recorrido...  ',datetime.now())

def usuarios():
    print('usuarios  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo = 'A').first()
    Oficina = justo.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    with open('c:/ajusto/csv/c06cajeros.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            Usuario = justo.USUARIOS.objects.filter(oficina=Oficina,login = row['c06usuario']).first()
            if Usuario == None:
                Usuario = justo.USUARIOS.objects.create(oficina=Oficina,login = row['c06usuario'])
            Usuario.nit = ''
            Usuario.nombre = ''
            Usuario.fec_ing = asignar_fecha('01/01/1900','%M-%D-%Y')
            Usuario.es_cajero = 'S'
            Usuario.cod_caj = row['c06codcaj']
            Usuario.fec_sal = asignar_fecha('01/01/1900','%M-%D-%Y')
            Usuario.cta_con_acr = row['c06ctacon']
            Usuario.activo = 'S'
            Usuario.save()
    print('          ',datetime.now())

def cierre_mes():
    print('cierres  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo = 'A').first()
    Oficina = justo.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    with open('c:/ajusto/csv/g10cierres.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            CierreMes = justo.cierre_mes.objects.filter(oficina=Oficina,fecha = asignar_fecha(row['g10feccie'],'%M-%D-%Y')).first()
            if CierreMes == None:
                CierreMes = justo.cierre_mes.objects.create(oficina=Oficina,fecha = asignar_fecha(row['g10feccie'],'%M-%D-%Y'))
            CierreMes.protegido = row['g10protegido']
            CierreMes.tot_deb = row['g10debitos']
            CierreMes.tot_cre = row['g10creditos']
            CierreMes.fec_cie = asignar_fecha(row['g10feccie'],'%M-%D-%Y')
            CierreMes.usuario = row['g10usuario']
            CierreMes.save()
    print('         ',datetime.now())

def mov_caja():
    print('Mov Caja   ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo = 'A').first()
    Oficina = justo.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    with open('c:/ajusto/csv/c07movcaja.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            MovCaja = justo.MOV_CAJA.objects.filter(oficina=Oficina,cod_caj=row['c07codcaj'],
                    fecha=asignar_fecha(row['c07fecha'],'%M-%D-%Y'),jornada=row['c07jornada']).first()
            if MovCaja == None:
                MovCaja = justo.MOV_CAJA.objects.create(oficina=Oficina,cod_caj=row['c07codcaj'],
                    fecha=asignar_fecha(row['c07fecha'],'%M-%D-%Y'),jornada=row['c07jornada'])
                MovCaja.saldo_ini = row['c07salant']
                MovCaja.debitos = row['c07salant']
                MovCaja.creditos = row['c07salant']
                MovCaja.val_che_dev = row['c07chedev']
                MovCaja.saldo_fin =row['c07salfin']
                MovCaja.diferencia = row['c07difer']
                MovCaja.val_cheques = row['c07cheques']
                MovCaja.val_vales = row['c07vales']
                MovCaja.cerrado = 'S'
                MovCaja.monedas = row['c07moneda'].replace(';', ',')
                MovCaja.save()
    print('           ',datetime.now())

def est_fin():
    print('Estados_fin ..  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s02estfin.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')    
        for row in csv_reader:
            Tercero  = justo.TERCEROS.objects.filter(
                cliente = Cliente,
                doc_ide = row['s02nit']).first()
            if Tercero == None:
                continue
            Estfin = justo.estados_fin.objects.filter(
                cliente = Cliente,
                tercero = Tercero,
                fec_inf = asignar_fecha(row['s02fecmod'].strip(),'%m/%d/%Y')).first()
            if Estfin == None:
                Estfin = justo.estados_fin.objects.create(
                    cliente = Cliente,
                    tercero = Tercero,
                    fec_inf = asignar_fecha(row['s02fecmod'].strip(),'%m/%d/%Y'))
            ing_sal_fij = row['s02ingmen']
            Estfin.ing_hon = row['s02inghon']
            Estfin.ing_pen = row['s02ingpen']
            Estfin.ing_arr = row['s02ingarr']
            Estfin.ing_com = row['s02ingcom']
            Estfin.ing_ext = row['s02ingext']
            Estfin.ing_otr = 'S'
            Estfin.ing_tot = 0
            Estfin.egr_sec_fin = row['s02egrsecfin']
            Estfin.egr_cuo_hip = row['s02egrcuohip']
            Estfin.egr_des_nom = 'S'
            Estfin.egr_gas_fam = row['s02egrgasfam']
            Estfin.egr_otr_cre = row['s02egrotrcre']
            Estfin.egr_arr = row['s02egrarr']
            Estfin.egr_otr_gas = row['s02egrotrgas']
            Estfin.egr_tot = 0
            Estfin.act_otr_egr = 0
            Estfin.act_tip_bien = ''
            Estfin.act_vei = row['s02actveh']
            Estfin.act_otr = 'S'
            Estfin.tot_act = 0
            Estfin.act_fin_rai = row['s02actfinrai']
            Estfin.act_inv = 0
            Estfin.escritura = ''
            Estfin.pas_otr = 'S'
            Estfin.pas_tip = row['s02pasfin']
            Estfin.tot_pat = 0
            Estfin.pas_val = row['s02pasotr']
            Estfin.tot_pas = 0
            Estfin.pas_des = 0 
            Estfin.dec_ren = 'N'
            Estfin.tip_pas = ''
            Estfin.des_pas = ''
            Estfin.val_pas = 0
            Estfin.ope_mon_ext = 'N'
            Estfin.nom_ban_ext = ''
            Estfin.ope_pais_ext = 'S'
            Estfin.ope_monto_ext = 0
            Estfin.num_cta_ext = ''
            Estfin.tip_ope_ext = ''
            Estfin.mon_ope_ext = 'S'
            Estfin.prod_mon_ext = 0
            Estfin.des_prod_ext = 0
            Estfin.mon_prod_ext = 0
            Estfin.pais_prod_ext = 0
            Estfin.ciu_prod_ext = 0
            Estfin.prom_prod_ext = 0
            Estfin.save()
    print('Fin Estados_fin',datetime.now())

def bene_aso():
    print('Bene_aso  ',datetime.now())
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s01compfami.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        idocide = 1
        for row in csv_reader:
            Socio = justo.ASOCIADOS.objects.filter(
                    oficina=Oficina,
                    cod_aso = row['s01xcodsoc']).first()
            if Socio == None:
                continue
            AsoBene = justo.ASO_BENEF.objects.filter(asociado  = Socio,
                    doc_ide = str(idocide)).first()
            if AsoBene == None:
                AsoBene = justo.ASO_BENEF.objects.create(asociado  = Socio,
                    doc_ide = str(idocide))
            AsoBene.nombre = row['s01xnombre']
            AsoBene.agno_nac = row['s01xagnnac']
            AsoBene.parentesco = row['s01xparentesco']
            AsoBene.porcentaje = 0
            AsoBene.save()
            idocide = idocide + 1
    print('Fin Bene ',datetime.now())

def referencias():
    print('Referencias  ',datetime.now())
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s02referencias.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Socio = justo.ASOCIADOS.objects.filter(
                    oficina = Oficina,
                    cod_aso = row['s02nit']).first()
            if Socio == None:
                continue
            Referencia = justo.ASO_REFERENCIAS.objects.filter(asociado = Socio,nombre = row['s02nombre']).first()
            if Referencia == None:
                Referencia = justo.ASO_REFERENCIAS.objects.create(asociado = Socio,nombre = row['s02nombre'])
            if row['s02tipref'] < '7':
                Referencia.tipo_ref = '1'
                if row['s02tipref'] == '1':
                    Referencia.parentesco = '3'
                elif row['s02tipref'] == '2':
                    Referencia.parentesco = '6' 
                elif row['s02tipref'] == '3':
                    Referencia.parentesco = '2' 
                else:
                    Referencia.parentesco = '9' 
            else:
                Referencia.parentesco = '0' 
                if row['s02tipref'] == '7':
                    Referencia.tipo_ref = '2'
                if row['s02tipref'] == '8':
                    Referencia.tipo_ref = '3'
            Referencia.ocupacion = row['s02cargo']
            Referencia.empresa = row['s02empresa']
            Referencia.direccion = row['s02direccion']
            Referencia.tel_fijo = row['s02telfij'][:10]
            Referencia.tel_cel = row['s02telcel'][:10]
            Referencia.tel_emp = row['s02telemp'][:10]
            Referencia.save()
    print('Fin Referen ',datetime.now())

def plan_aportes():
    print('plan aportes     ',datetime.now())
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/S00APORTACION.CSV', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            PlanApor = justo.PLAN_APORTES.objects.filter(
                    oficina = Oficina,
                    agno = int(row['agno'])).first()
            if PlanApor == None:
                PlanApor = justo.PLAN_APORTES.objects.create(
                    oficina = Oficina,
                    agno = int(row['agno'])
                    )
            PlanApor.meses = row['agno']
            PlanApor.iniadu = row['s00iniadu']
            PlanApor.totadu = row['s00totadu']
            PlanApor.inichi1 = row['s00inichi1']
            PlanApor.totchi1 = row['s00totchi1']
            PlanApor.inichi2 = row['s00inichi2']
            PlanApor.totchi2 = row['s00totchi2']
            PlanApor.inijur = row['s00inijur']
            PlanApor.totjur = row['s00totjur']
            PlanApor.save()
        
    print('Fin Plan Aportes ',datetime.now())

def asigna_com_cre():
    print('Recorrido...  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    DetallesProSel = justo.DETALLE_PROD.objects.filter(concepto='CUOTA').all()
    ya = 0
    for oDP in DetallesProSel:
        if ya == 0:
            print('Recorrido...  ',datetime.now())
        ya = ya + 1
        oHE = oDP.hecho_econo
        oCtaCon = justo.PLAN_CTAS.objects.filter(cliente=Cliente,per_con= oHE.fecha.year,cod_cta='14433501').first()
        if oCtaCon == None:
            print('No hay Cta Con ',oDP.subcuenta)
        Credito = justo.CREDITOS.objects.filter(oficina=Oficina,cod_cre = oDP.subcuenta).first()
        if Credito == None:
            print('No hay Credito ',oDP.subcuenta)
            continue
        oTer = Credito.socio.tercero
        oHallado = justo.DETALLE_ECONO.objects.filter(hecho_econo=oHE,tercero=oTer,cuenta=oCtaCon).first()
        if oHallado == None:
            print('No hay Detalle Cr =',oDP.subcuenta,'  Comp=',oHE.docto_conta.codigo,oHE.numero,oHE.fecha)
            continue
        oHallado.item_concepto = 'Kapita'
        oHallado.detalle_prod = oDP
        oHallado.detalle = oHallado.detalle.strip()+','+oDP.subcuenta if len(oHallado.detalle.strip())>0 else oDP.subcuenta
        oHallado.save()    
    print('         ...  ',datetime.now(),ya)

def codeudores():
    print('Codeudores...  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s10codeudor.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Credito = justo.CREDITOS.objects.filter(oficina=Oficina,cod_cre=row['s10codcre']).first()
            if Credito == None:
                continue
            Tercero = justo.TERCEROS.objects.filter(cliente=Cliente,doc_ide=row['s10nit']).first()
            if Tercero == None:
                continue
            Codeudor = justo.CODEUDORES.objects.filter(oficina=Oficina,credito=Credito,tercero=Tercero).first()
            if Codeudor == None:
                Codeudor = justo.CODEUDORES.objects.create(oficina=Oficina,credito=Credito,tercero=Tercero)
            Codeudor.save()
    print('          ...  ',datetime.now())

def categorizacion():
    print('Grabar Categorizaciones  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    reg_inicio = 379997
    with open('c:/ajusto/csv/s24catecred.csv', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for index, row in enumerate(csv_reader, start=1):
            if index < reg_inicio:
                continue  # Saltar las filas hasta alcanzar el número de registro inicial
            CreCarHis = justo.CARTE_CAT_HIS.objects.filter(oficina = Oficina,fecha = asignar_fecha(row['s24fecha']),cod_cre = row['s24codcre']).first()
            if CreCarHis == None:
                CreCarHis = justo.CARTE_CAT_HIS.objects.create(oficina = Oficina,fecha = asignar_fecha(row['s24fecha']),cod_cre = row['s24codcre'])
            CreCarHis.nit = row['s24nit']
            CreCarHis.cod_lin_cre = row['s24codlincre']
            CreCarHis.cod_imp_con = row['s24codimpcon']
            CreCarHis.for_pag = row['s24forpag']
            CreCarHis.plazo = row['s24plazo']
            CreCarHis.dias_mor = row['s24diamor']
            CreCarHis.cap_ini = row['s24capini']
            CreCarHis.sal_cap = row['s24salcap']
            CreCarHis.sal_cap_dia = row['s24salcapdia']
            CreCarHis.sal_int_dia = row['s24salintdia']
            CreCarHis.int_cau_res_per = row['s24intcauresmes']
            CreCarHis.categoria = row['s24categoria']
            CreCarHis.arrastre = row['s24arrastre']
            CreCarHis.aporte = row['s24aporte']
            CreCarHis.pro_ind = row['s24provision']
            CreCarHis.saldo_1 = row['s24saldo1']
            CreCarHis.saldo_2 = row['s24saldo2']
            CreCarHis.vr_gar_hip = row['s24valgarhip']
            CreCarHis.cat_int_mes = row['s24catint']
            CreCarHis.sal_cat_int = row['s24salcatint']
            CreCarHis.castigo = row['s24casti']
            CreCarHis.gas_pro_ind = row['s24gasproind']
            CreCarHis.gas_pro_gen = row['s24gasprogen']
            CreCarHis.zeta = row['z']
            CreCarHis.puntaje = row['puntaje']
            CreCarHis.cat_mod = row['cat_mod']
            CreCarHis.cat_ree = row['cat_ree']
            CreCarHis.cat_eva = row['cat_eva']
            CreCarHis.pro_inc = row['pi']
            CreCarHis.pdi = row['pdi']
            CreCarHis.vea = row['vea']
            CreCarHis.pe = row['pe']
            CreCarHis.conta_per = row['conta']
            CreCarHis.ali_cuota = row['ali_mes']
            Credito = justo.CREDITOS.objects.filter(oficina = Oficina,cod_cre = row['s24codcre']).first()
            if Credito != None:
                CreCarHis.credito = Credito
            CreCarHis.save()
    print('Fin credito CATEGO  ',datetime.now())

def catego_detalle():
    print('Grabar Categori Detalle  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    reg_inicio = 0
    with open('c:/ajusto/csv/s31hiscatint.csv', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for index, row in enumerate(csv_reader, start=1):
            if index < reg_inicio:
                continue  # Saltar las filas hasta alcanzar el número de registro inicial
            CatDet = justo.CARTERA_CXC.objects.filter(oficina = Oficina,fecha = asignar_fecha(row['s31fecha']),cod_cre = row['s31codcre'],fec_ref = asignar_fecha(row['s31fecref'])).first()
            if CatDet == None:
                CatDet = justo.CARTERA_CXC.objects.create(oficina = Oficina,fecha = asignar_fecha(row['s31fecha']),cod_cre = row['s31codcre'],fec_ref = asignar_fecha(row['s31fecref']))
            CatDet.categoria = row['s31cat']
            CatDet.valor = row['s31valor']
            CatDet.val_ali = row['s31valali']
            CatDet.clave = row['s31clave']
            Credito = justo.CREDITOS.objects.filter(oficina = Oficina,cod_cre = row['s31codcre']).first()
            if Credito != None:
                CatDet.credito = Credito
            CatDet.save()
    print('Fin credito CATEGO  ',datetime.now())

def vMov_cre():
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    print('Creditos  ',datetime.now())
    Creditos = justo.CREDITOS.objects.filter(oficina=Oficina,estado = 'A')
    xTotSal = 0
    xNumCre = 0
    for Credito in Creditos:
        icod_cre = Credito.cod_cre
        if Credito == None:
            print('No Hay credito')
            exit()
        xNumCre = xNumCre + 1
        CreCaus = justo.CREDITOS_CAUSA.objects.filter(oficina=Oficina,cod_cre = Credito.cod_cre,comprobante=None)
        mov_cre = []
        for CreCau in CreCaus:
            mov_cre.append({
                'Fecha' : CreCau.fecha,
                'Tipo'  : '1',
                'Cuota' : CreCau.cuota,
                'KapTal': CreCau.capital,
                'IntCor': CreCau.int_cor,
                'IntMor': 0,
                'PolSeg': 0,
                'Acreed': 0
            })
        DetPros = justo.DETALLE_PROD.objects.filter(oficina=Oficina,producto='CR',subcuenta = Credito.cod_cre)
        for DetPro in DetPros:
            HecEco = justo.HECHO_ECONO.objects.filter(id=DetPro.hecho_econo.id).first()
            DetEcos = justo.DETALLE_ECONO.objects.filter(detalle_prod=DetPro)
            xKap,xIntCor,xIntMor,xPolSeg,xAcre = 0,0,0,0,0
            xTipMov = ' '
            if DetPro.concepto == 'CUOTA':
                xTipMov = '8'
            elif DetPro.concepto == 'ABOCA':
                xTipMov = '7'
            elif DetPro.concepto == 'ABOCU':
                xTipMov = '9'
            elif DetPro.concepto == 'CONDO':
                xTipMov = '6'
            elif DetPro.concepto == 'GASTI':
                xTipMov = '5'
            for DetEco in DetEcos:
                if DetEco.item_concepto == 'Kapita':
                    xKap = 0 if DetEco.valor_2 is None  else -DetEco.valor_2 
                elif DetEco.item_concepto == 'IntCor':
                    xIntCor = 0 if DetEco.valor_2 is None  else -DetEco.valor_2
                elif DetEco.item_concepto == 'IntMor':
                    xIntMor = 0 if DetEco.valor_2 is None  else -DetEco.valor_2
                elif DetEco.item_concepto == 'PolSeg':
                    xPolSeg = 0 if DetEco.valor_2 is None  else -DetEco.valor_2
                elif DetEco.item_concepto == 'Acreed':
                    xAcre = 0 if DetEco.valor_2 is None  else -DetEco.valor_2
            mov_cre.append({
                'Fecha' : HecEco.fecha,
                'Tipo'  : xTipMov,
                'Cuota' : 99,
                'KapTal': xKap,
                'IntCor': xIntCor,
                'IntMor': xIntMor,
                'PolSeg': xPolSeg,
                'Acreed': xAcre
            })
            ModCre = justo.CAMBIOS_CRE.objects.filter(det_pro = DetPro).first()
            if ModCre != None:
                mov_cre.append({
                    'Fecha' : HecEco.fecha,
                    'Tipo'  : ModCre.tip_cam,
                    'Cuota' : 99,
                    'KapTal': ModCre.capital,
                    'IntCor': ModCre.int_cor,
                    'IntMor': ModCre.int_mor,
                    'PolSeg': ModCre.pol_seg,
                    'Acreed': ModCre.acreedor
                })
        mov_cre = sorted(mov_cre, key=lambda x: (x['Fecha'],x['Cuota']))
        saldo = sum(elem['KapTal'] for elem in mov_cre )
        xTotSal += saldo
        # print(icod_cre,' Saldo ',saldo)
    print('Total Saldo',xTotSal,'  Numero de Creditos ',xNumCre)
    print('xxx       ',datetime.now())

def prueba():
    TIPOS_MOV_CRE = {
        'DESEM': '0',
        'CAUSA': '1',
        'AJUST': '2',
        'DESPP': '3',
        'KASCO': '4',
        'CASTI': '5',
        'CONDO': '6',
        'ABOCA': '7',
        'ABOCU': '8',
        'CUOTA': '9'
    }
    print('Duracion  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    Creditos = justo.CREDITOS.objects.filter(oficina=Oficina,estado = 'A')
    xTotSal = 0
    xNumCre = 0
    for Credito in Creditos:
        queryset1 = justo.CREDITOS_CAUSA.objects.values('fecha', 'cuota') \
            .filter(oficina=Oficina, cod_cre=Credito.cod_cre) \
            .annotate(
                tipmov=Value('1'),
            kapital=F('capital'),
            intcor=F('int_cor'),
            intmor=Value(0, output_field=IntegerField()),
            polseg=Value(0, output_field=IntegerField()),
            despp=Value(0, output_field=IntegerField()),
            acreed=Value(0, output_field=IntegerField())
        )

        #for lista in queryset1:
        #    print(lista)
        #    break
        queryset2 = justo.DETALLE_PROD.objects.filter(oficina=Oficina, producto='CR', subcuenta=Credito.cod_cre) \
            .values(fecha=F('hecho_econo__fecha')) \
            .annotate(
                cuota=Value(0),
                tipmov=Case(
                    *[When(concepto=concept, then=Value(value)) for concept, value in TIPOS_MOV_CRE.items()],
                    output_field=CharField()
                ),
                kapital=Coalesce(Sum(Case(When(detalle_econo__item_concepto='Kapita', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                intcor=Coalesce(Sum(Case(When(detalle_econo__item_concepto='IntCor', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                intmor=Coalesce(Sum(Case(When(detalle_econo__item_concepto='IntMor', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                polseg=Coalesce(Sum(Case(When(detalle_econo__item_concepto='PolSeg', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                despp=Coalesce(Sum(Case(When(detalle_econo__item_concepto='DesPP', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                acreed=Coalesce(Sum(Case(When(detalle_econo__item_concepto='Acreed', then=-F('detalle_econo__valor_2')))), Value(0.0)) 
            )
        #for lista in queryset2:
        #    print(lista)
        #    break

        queryset3 = justo.CAMBIOS_CRE.objects.filter(det_pro__oficina=Oficina, det_pro__producto='CR', det_pro__subcuenta=Credito.cod_cre) \
            .values(fecha=F('det_pro__hecho_econo__fecha')) \
            .annotate(
                cuota=Value(0, output_field=IntegerField()),
                tipmov=F('tip_cam'),
                kapital=F('capital'),
                intcor=F('int_cor'),
                intmor=F('int_mor'),
                polseg=F('pol_seg'),
                despp=Value(0, output_field=IntegerField()),
                acreed=F('acreedor')
            )
        tab_liq = list(queryset1) + list(queryset2) + list(queryset3)
        tab_liq = sorted(tab_liq, key = itemgetter('fecha', 'tipmov'))
        nr = 0
        saldo = sum(objeto['kapital'] for objeto in tab_liq if objeto['tipmov'] != '0')
        #print(Credito.cod_cre,' ', saldo)
        xTotSal = xTotSal + saldo
        xNumCre = xNumCre + 1
    print('Creditos  ',xNumCre,'   ',xTotSal)
    print('Fin       ',datetime.now())

def huerfanos_aho():
    print('Huerfanos Ahorros ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    CentroCosto = justo.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    ctas_aho = ['21100501','21100501','21101001','21101001','21101501','21101501','21102001','21102001','21050501','21051001',
			    '21250501','21050502','21051002','21050503','21051003','21250501','21251501','21050504','21051004']
    DetHues = justo.DETALLE_ECONO.objects.filter(cuenta__cod_cta__in=ctas_aho,detalle_prod__isnull=True
            ).select_related('cuenta', 'hecho_econo')
    print(DetHues.count())
    for DetHue in DetHues:
        Tercero = DetHue.tercero
        ImpCon = justo.IMP_CON_LIN_AHO.objects.filter(Q(ctaafeact=DetHue.cuenta.cod_cta) | Q(ctaafeina=DetHue.cuenta.cod_cta)).first()
        if ImpCon == None:
            continue
        Socio = justo.ASOCIADOS.objects.filter(oficina = Oficina,tercero = Tercero).first()
        if Socio == None:
            print('No Existe Asociado',Tercero.doc_ide)
            continue
        CtaAho = justo.CTAS_AHORRO.objects.filter(oficina = Oficina,asociado = Socio,lin_aho = ImpCon.linea_ahorro,cod_imp = ImpCon.cod_imp).first()
        if CtaAho == None:
            print('Asociado ',Tercero.doc_ide,' No tiene cuenta de ahorro')
            continue
        DetPro = justo.DETALLE_PROD.objects.filter(hecho_econo = DetHue.hecho_econo,producto = 'AH',concepto = 'AHO',subcuenta = CtaAho.num_cta,centro_costo = CentroCosto).first()
        if DetPro == None:
            DetPro = justo.DETALLE_PROD.objects.create(hecho_econo = DetHue.hecho_econo,producto = 'AH',concepto = 'AHO',subcuenta = CtaAho.num_cta,centro_costo = CentroCosto)
        DetPro.valor = DetHue.debito - DetHue.credito
        DetPro.save()
        DetHue.detalle = 'Int Cta Aho = '+CtaAho.num_cta
        DetHue.detalle_prod = DetPro
        DetHue.item_concepto = 'SalIni' if DetHue.hecho_econo.numero == 1 else ('Deposi' if DetPro.valor < 0 else 'Retiro')
        DetHue.save()
    print('Fin   Huerfanos  ',datetime.now())        
    return

def init():
    #   prueba()
    #   vMov_cre()
    #   inicio()
    #   tablas_de_referencia()
    #   terceros()       #  SOLO LOS REGISTRADOS EN DINAMICA
    #   pagadores()
    #   socios()            
    #   plan_ctas()
    #   conceptos()
    #   docto_conta()
    #   comprobantes()      #  59 
    #   detalle_econo()     # 190 
    #   linaho()
    #   imp_con_lin_aho()
    #   int_lin_aho()
    #   ret_fue_aho()
    #   ctas_aho()          #  quitar aviso
    #   cta_cdat()
    #   cta_cdat_amp()
    #   cta_cda_liq()
    #   ImpIntDiaAho()      #  110 minutos
    #   lineas_credito()
    #   cat_des_dia_cre()
    #   imp_con_cre()
    #   imp_con_cre_int()
    #   destino_cre()
    #   creditos()              #  10 Min
    #   importar_mov_cre()      #  36 Min
    #   grabar_causa_cre()      #    42 Min tener en cuenta que en la implantacion final se debe importar completamente 
    #   detalle_prod()          #    110 Min
    #   deta_eco_aho()
    #   grabar_credito_mod()
    #   grabar_credito_mod2()    #  necesidad de un ajuste cuando se aplica abocu con ajuste en fecha diferente al del movimiento
    #   asigna_con_cre()     #   47  Min  se ha cambiado temporalmente port erorres pero en la importacion definitiva deben quitarse los comentarios
    #   est_fin()
    #   bene_aso()
    #   referencias()
    #   usuarios()
    #   cierre_mes()
    #   mov_caja()
    #   asigna_com_cre()   No seria necesario solo sondeo
    #   codeudores()
    #   plan_aportes()
    #   categorizacion()
    #   catego_detalle()    #  28 min
    #   huerfanos_aho()

init()