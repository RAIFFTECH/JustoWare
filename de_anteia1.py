from datetime import date,datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Justo_proy.settings')

# Initialize django application
import django
django.setup()
import requests
from clientes_app.models import CLIENTES
from oficinas_app.models import OFICINAS
from terceros_app.models import TERCEROS
from localidades_app.models import LOCALIDADES


import time

url = "https://dev.api.anteia.co/auth"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Basic NjM2MTJhNzQwY2YwYWE0MzVhNjhmMjdmOmVlNWQ0MWM4ZGUwZjE1MDk4NDE2ZjQ2ODkzZmE0NzMxOWYwMWFkMDE5ZTU5ZWQ5ZDFhMDI0ODZmODQzYTEzYjg=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
token = response.json()['token']

url = "https://dev.hyperflow.anteia.co/api/v2/hyperflow/getPendingSync/6527fd228cda1257e2422a73"

payload = {}
headers = {
  'Accept': 'application/json, application/xml',
  'Authorization': 'Bearer '+token
}

from django.core.exceptions import ValidationError
from django.db import models
class DefaultToZeroMixin(models.Model):
    def save(self, *args, **kwargs):
        for field_name in self._meta.fields:
            field = getattr(self, field_name)
            if isinstance(field, models.IntegerField) and (field is None or field == ''):
                setattr(self, field_name, 0)
        super(DefaultToZeroMixin, self).save(*args, **kwargs)
    class Meta:
        abstract = True

def asignar_fecha(fecha_str, formato='%d/%m/%Y'):
    try:
        fecha = datetime.strptime(fecha_str, formato)
        fecha_validada = fecha.strftime('%Y-%m-%d')
        return fecha_validada
    except ValueError:
        return None

def init():
    response = requests.request("GET", url, headers=headers, data=payload)
    nom_arc = "c:/aaa/archivo4"
    anteia1 = response.json()
    with open(nom_arc, 'w') as archivo:
        archivo.write(str(anteia1))
    Cliente = CLIENTES.objects.filter(codigo='A').first()
    if Cliente == None:
        Cliente=CLIENTES.objects.create(codigo = "A",
            doc_ide = '892000914',
            sigla = 'COORINOQUIA',
            nombre = 'COOPERATIVA ESPECIALIZADA DE AHORRO Y CRÉDITO DE LA ORINOQUIA',
            celular = '3118993251',
        )
    Oficina = OFICINAS.objects.filter(codigo='A0001').first()
    if Oficina == None:
        Oficina=OFICINAS.objects.create(cliente = Cliente,codigo = "A0001",
            contabiliza = 'S',
            nombre_oficina = 'Oficina Principal',
            responsable = 'Jose Guillermo Prieto López',
            celular = '3153263722',
        )
    for idsocio in anteia1['flows']:
        doc_ide = anteia1['flows'][idsocio]['user.document.number'] = anteia1['flows'][idsocio]['user.document.number']
        # nombre = anteia1['flows'][idsocio]['user.fullName']     # Terceros Nombre
        tipTra = anteia1['flows'][idsocio]['tipoTramite']
        dirTot = anteia1['flows'][idsocio]['user.manualAdress.numVia']
        dirTot = dirTot + ' '+anteia1['flows'][idsocio]['user.manualAdress.segundoNumero']
        dirTot = dirTot + ' '+anteia1['flows'][idsocio]['user.manualAdress.numViaDos']
        tipVia = anteia1['flows'][idsocio]['user.manualAdress.tipoVia']
        direccion = tipVia+' '+dirTot
        Cliente = CLIENTES.objects.filter(codigo='A').first()
        Tercero = TERCEROS.objects.filter(cliente=Cliente,
            cla_doc = anteia1['flows'][idsocio]['user.document.type.cod'][0],
            doc_ide = anteia1['flows'][idsocio]['user.document.number']).first()
        if Tercero == None:
            Tercero = TERCEROS.objects.create(
                cliente = Cliente,
                cla_doc = anteia1['flows'][idsocio]['user.document.type.cod'][0],
                doc_ide = anteia1['flows'][idsocio]['user.document.number']
            )
        Tercero.tip_ter = 'N'
        Tercero.pri_ape = anteia1['flows'][idsocio]['user.firstLastName']
        Tercero.seg_ape = anteia1['flows'][idsocio]['user.secondLastName']
        Tercero.pri_nom = anteia1['flows'][idsocio]['user.firstNameFirst']
        Tercero.seg_nom = anteia1['flows'][idsocio]['user.middleName']
        Tercero.direccion = anteia1['flows'][idsocio]['user.manualAdress.concat']
        Tercero.nombre = anteia1['flows'][idsocio]['user.fullName']
        Tercero.dig_ver = ' '
        Tercero.nit_rap = ' '
        Tercero.tel_res = anteia1['flows'][idsocio]['user.phone']
        Tercero.celular1 =  anteia1['flows'][idsocio]['user.phone'] # Celular
        Localidad = LOCALIDADES.objects.filter(cliente=Cliente,
            codigo=anteia1['flows'][idsocio]['user.document.expeditionCity.cod']).first()
        Tercero.cod_ciu_exp = Localidad
        Localidad = LOCALIDADES.objects.filter(cliente=Cliente,
            codigo=anteia1['flows'][idsocio]['user.city.cod']).first()
        Tercero.cod_ciu_res = Localidad
        print('Fecha ',anteia1['flows'][idsocio]['user.document.expeditionDate2'])
        Tercero.fec_exp_ced = datetime.strptime(anteia1['flows'][idsocio]['user.document.expeditionDate2'], "%d/%m/%Y").strftime("%Y-%m-%d")
        Tercero.email = anteia1['flows'][idsocio]['user.email']
        Tercero.fec_act = date.today()
        Tercero.regimen = '49'
        Tercero.save()
        #   Asociados 
        Asociado = ASOCIADOS.objects.filter(oficina=Oficina,
            cod_aso = doc_ide).first()
        if Asociado == None:
            Asociado = ASOCIADOS.objects.create(
                oficina = Oficina,
                cod_aso = doc_ide,
            )
        Asociado.tercero = Tercero
        Asociado.sexo = anteia1['flows'][idsocio]['user.document.sex']
        Asociado.est_civ = anteia1['flows'][idsocio]['user.civilState'][0]
        Asociado.fec_nac = datetime.strptime(anteia1['flows'][idsocio]['user.document.birthDateFormated'],"%d/%m/%Y").strftime("%Y-%m-%d")
        Asociado.ciu_res = anteia1['flows'][idsocio]['user.workInfo.city.cod']
        Asociado.zona = anteia1['flows'][idsocio]['user.zone']
        Asociado.estrato = anteia1['flows'][idsocio]['user.estrato']
        Asociado.niv_est = anteia1['flows'][idsocio]['user.studiesLevel.cod']
        Asociado.ocupacion = anteia1['flows'][idsocio]['user.ocupation']
        Asociado.ocupacion_cod = anteia1['flows'][idsocio]['user.ocupation.cod']
        Asociado.profesion = anteia1['flows'][idsocio]['user.tituloProfesional']
        Asociado.cab_fam = anteia1['flows'][idsocio]['user.houseHolder'][0]  # asociados
        # datetime.strptime(anteia1['flows'][idsocio]['user.document.birthDate'], "%d-%b-%Y").strftime("%Y-%m-%d")
        Asociado.fec_afi = asignar_fecha(anteia1['flows'][idsocio]['form.date'])
        # , "%d-%b-%Y").strftime("%Y-%m-%d")
        Asociado.cargo_emp = anteia1['flows'][idsocio]['user.workInfo.position']
        Asociado.per_a_cargo = anteia1['flows'][idsocio]['user.personsInCharge']
        Asociado.num_hij_men = anteia1['flows'][idsocio]['user.numsChildren.menores']
        Asociado.num_hij_may = anteia1['flows'][idsocio]['user.numsChildren.mayores']
        Asociado.tip_viv = anteia1['flows'][idsocio]['user.home.type.cod']
        # Asociado.tie_en_ciu = anteia1['flows'][idsocio]['user.home.time']
        Asociado.med_con = anteia1['flows'][idsocio]['coorinoquia.medioContacto']
        #   Asociado.fec_ing_tra = datetime.strptime(anteia1['flows'][idsocio]['user.workInfo.startDate'],"%d-%b-%Y").strftime("%Y-%m-%d")
        Asociado.tel_tra = anteia1['flows'][idsocio]['user.workInfo.phone']
        #   Asociado.tip_sal = anteia1['flows'][idsocio]['user.workInfo.salaryType']
        Asociado.ciu_tra = anteia1['flows'][idsocio]['user.workInfo.city']
        #   Asociado.act_eco = anteia1['flows'][idsocio]['user.workInfo.economicActivity'] 
        Asociado.cod_ciiu = anteia1['flows'][idsocio]['user.workInfo.ciiu'][:12]
        #   Asociado.tip_con = anteia1['flows'][idsocio]['user.workInfo.contractType']
        Asociado.nom_emp = anteia1['flows'][idsocio]['user.workInfo.company']
        #   Asociado.nit_emp = anteia1['flows'][idsocio]['user.workInfo.nit']
        #   Asociado.dir_emp = anteia1['flows'][idsocio]['user.workInfo.address']
        #   Asociado.email_emp = anteia1['flows'][idsocio]['user.workInfo.email']
        Asociado.sector_emp = anteia1['flows'][idsocio]['user.workInfo.sector']
        Asociado.empresa_ant = anteia1['flows'][idsocio]['user.workInfo.tiempo']
        Asociado.emp_num_emp = anteia1['flows'][idsocio]['user.workInfo.hasEmployees.quantity']
        #    negocio_lug = anteia1['flows'][idsocio]['user.workInfo.location']
        #    ocuEmp = anteia1['flows'][idsocio]['user.workInfo.occupation']
        Asociado.negocio_pro = anteia1['flows'][idsocio]['user.workInfo.hasBusiness']
        Asociado.negocio_nom = anteia1['flows'][idsocio]['user.business.name']
        Asociado.negocio_tel = anteia1['flows'][idsocio]['user.business.owner.phone']
        Asociado.negocio_loc_pro = anteia1['flows'][idsocio]['user.business.rental']
        Asociado.negocio_cam_com = anteia1['flows'][idsocio]['user.business.camaraComercio']
        Asociado.negocio_ant = anteia1['flows'][idsocio]['user.business.time']
        Asociado.pension_ent = anteia1['flows'][idsocio]['user.pensioner.entity']
        Asociado.pension_tie = anteia1['flows'][idsocio]['user.pensioner.startDate']
        Asociado.pension_otr = anteia1['flows'][idsocio]['user.pensioner.other']
        Asociado.pension_ent_otr = anteia1['flows'][idsocio]['user.pensioner.other.entity']
        Asociado.pep_es_fam = anteia1['flows'][idsocio]['user.pep.esFamiliar'][0]
        Asociado.pep_fam_par = anteia1['flows'][idsocio]['user.pep.fam.parentesco']
        Asociado.pep_fam_nom = anteia1['flows'][idsocio]['user.pep.fam.nombre']
        Asociado.pep_car_pub = anteia1['flows'][idsocio]['user.ostentaCargoPublico'][0]
        Asociado.pep_cargo = anteia1['flows'][idsocio]['user.pep.cargo']
        #   Asociado.pep_eje_pod = anteia1['flows'][idsocio]['user.ejercePoder'][0]
        #   Asociado.pep_adm_rec_est = anteia1['flows'][idsocio]['user.administraRecursos'][0]
        Asociado.tie_gre_car = anteia1['flows'][idsocio]['coorinoquia.fatca2'][0]
        Asociado.recibe_pag_ext = anteia1['flows'][idsocio]['coorinoquia.fatca3'][0]
        Asociado.recide_ext_mas_186 = anteia1['flows'][idsocio]['coorinoquia.fatca1'][0]
        Asociado.recibe_ing_ext = anteia1['flows'][idsocio]['coorinoquia.fatca4'][0]
        
        Asociado.save()
        # Estados Financieros
        Estados_Fin = ESTADOS_FIN.objects.filter(cliente=Cliente,tercero=Tercero).first()
        if Estados_Fin == None:
            Estados_Fin = ESTADOS_FIN.objects.create(
                cliente = Cliente,
                tercero = Tercero,
            )
        Estados_Fin.ing_sal_fij = anteia1['flows'][idsocio]['user.financial.salary']
        #   Estados_Fin.ing_hon = anteia1['flows'][idsocio]['user.financial.honoraries']
        #   Estados_Fin.ing_pen = anteia1['flows'][idsocio]['user.financial.pension']
        #   Estados_Fin.ing_arr = anteia1['flows'][idsocio]['user.financial.otherIncome.act']  # no esta
        #   Estados_Fin.ing_com = anteia1['flows'][idsocio]['user.financial.pension']  # no esta
        #   Estados_Fin.ing_ext = anteia1['flows'][idsocio]['user.financial.extra']
        #   Estados_Fin.ing_otr = anteia1['flows'][idsocio]['user.financial.agregarOtros'][0]
        Estados_Fin.ing_tot = anteia1['flows'][idsocio]['user.financial.totalIncomes']
        #   Estados_Fin.egr_sec_fin = anteia1['flows'][idsocio]['user.financial.familyExpenses']
        #   Estados_Fin.egr_cuo_hip = anteia1['flows'][idsocio]['user.financial.otherIncome']
        #   Estados_Fin.egr_des_nom = anteia1['flows'][idsocio]['user.financial.hasOtherExpenses'][0]
        #   Estados_Fin.egr_gas_fam = anteia1['flows'][idsocio]['user.financial.personalExpenses']
        #   Estados_Fin.egr_otr_cre = anteia1['flows'][idsocio]['user.financial.creditCards']
        #   Estados_Fin.egr_arr = anteia1['flows'][idsocio]['user.financial.leasing']
        #   Estados_Fin.egr_otr_gas = anteia1['flows'][idsocio]['user.financial.otherExpenses']
        Estados_Fin.egr_tot = anteia1['flows'][idsocio]['user.financial.totalExpenses']
        #   Estados_Fin.act_otr_egr = anteia1['flows'][idsocio]['user.financial.otherExpenses.act']
        Estados_Fin.act_tip_bien = anteia1['flows'][idsocio]['coorinoquia.activos.tipo2']
        Estados_Fin.act_vei = anteia1['flows'][idsocio]['coorinoquia.activos.valorComercial2']
        Estados_Fin.act_otr = anteia1['flows'][idsocio]['coorinoquia.agregarActivo'][0]
        Estados_Fin.tot_act = anteia1['flows'][idsocio]['user.financial.totalAssets']
        Estados_Fin.act_fin_rai =anteia1['flows'][idsocio]['coorinoquia.activos.valorComercial']
        Estados_Fin.act_inv = anteia1['flows'][idsocio]['coorinoquia.inversiones']
        Estados_Fin.escritura = anteia1['flows'][idsocio]['coorinoquia.activos.tipo']
        #   Estados_Fin.pas_otr = anteia1['flows'][idsocio]['coorinoquia.agregarPasivo'][0]
        Estados_Fin.pas_tip = anteia1['flows'][idsocio]['coorinoquia.pasivos.tipo']
        Estados_Fin.tot_pat = anteia1['flows'][idsocio]['user.financial.totalEquity']
        Estados_Fin.pas_val = anteia1['flows'][idsocio]['coorinoquia.pasivos.valorComercial2']
        Estados_Fin.tot_pas = anteia1['flows'][idsocio]['coorinoquia.totalLiability']
        Estados_Fin.pas_des = anteia1['flows'][idsocio]['coorinoquia.pasivos.descripcion2']
        Estados_Fin.dec_ren = anteia1['flows'][idsocio]['coorinoquia.declaraciones.renta'][0]
        Estados_Fin.tip_pas = anteia1['flows'][idsocio]['coorinoquia.pasivos.tipo2']
        Estados_Fin.des_pas = anteia1['flows'][idsocio]['coorinoquia.pasivos.descripcion']
        Estados_Fin.val_pas = anteia1['flows'][idsocio]['coorinoquia.pasivos.valorComercial']
        Estados_Fin.ope_mon_ext = anteia1['flows'][idsocio]['coorinoquia.declaraciones.realizaOperaciones'][0]
        Estados_Fin.nom_ban_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.nombreEntidad']
        Estados_Fin.ope_monto_ext = anteia1['flows'][idsocio]['coorinoquia.operExtranjeras.monto']
        Estados_Fin.ope_pais_ext = anteia1['flows'][idsocio]['coorinoquia.operExtranjeras.pais']
        Estados_Fin.num_cta_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.numCuenta']
        Estados_Fin.tip_ope_ext = anteia1['flows'][idsocio]['coorinoquia.operExtranjeras.tipoOperacion']
        Estados_Fin.mon_ope_ext = anteia1['flows'][idsocio]['coorinoquia.operExtranjeras.moneda']
        Estados_Fin.prod_mon_ext = anteia1['flows'][idsocio]['coorinoquia.declaraciones.productosExtranjeros'][0]
        Estados_Fin.des_prod_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.descripcion']
        Estados_Fin.mon_prod_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.moneda']
        Estados_Fin.pais_prod_ext =anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.pais']
        Estados_Fin.ciu_prod_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.ciudad']
        Estados_Fin.prom_prod_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.monto']
        Estados_Fin.fec_inf = asignar_fecha(anteia1['flows'][idsocio]['form.date'])
        Estados_Fin.save()
        if tipTra == 'Afiliación y solicitud de crédito':
            fec_hoy = datetime.strptime("2023-11-6", "%Y-%m-%d")
            Originacion = ORIGINACION.objects.filter(asociado=Asociado).first()
            if Originacion == None:
                Originacion = ORIGINACION.objects.create(
                    asociado = Asociado,
                )     
            Originacion.lin_cre = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.linea']				
            Originacion.monto = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.monto']				
            Originacion.plazo = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.plazo']				
            Originacion.gar_cre_sol = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.garantia.cod']
            Originacion.lin_cre_sol = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.linea.cod']
            Originacion.mod_cre_sol = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.modalidad.cod']
            Originacion.save()

        for beneficiario in anteia1['arrayData'][idsocio]['coorinoquia.beneficiarios']['data']:
            benNumDoc = beneficiario['index']
            Aso_benef = ASO_BENEF.objects.filter(asociado = Asociado,doc_ide = benNumDoc).first()
            if Aso_benef == None:
                Aso_benef = ASO_BENEF.objects.create(
                    asociado = Asociado,
                    doc_ide = benNumDoc,
            )
            #   Aso_benef.cla_doc = beneficiario['data']['docType'][0]
            if beneficiario['data']['parentesco'] == 'Hijo/Hijastro':
                Aso_benef.parentesco = '2'
            elif beneficiario['data']['parentesco'] == 'Nuera': 
                Aso_benef.parentesco = '9'
            else: 
                Aso_benef.parentesco = '3'
            # Aso_benef.parentesco = Aso_benef['data']['parentesco'][0]
            #   Aso_benef.porcentaje = beneficiario['data']['porcentaje']
            Aso_benef.nombre = beneficiario['data']['nombreCompleto']
            Aso_benef.save()

        return
        
        for reffam in anteia1['arrayData'][idsocio]['coorinoquia.referenciasFamiliares']['data']:
            refFamNomCom = reffam['data']['nombreCompleto']
            Aso_ref_fam = justoAppModels.ASO_REF_FAM.objects.filter(asociado = Asociado,nombre = refFamNomCom).first()
            if Aso_ref_fam == None:
                Aso_ref_fam = justoAppModels.ASO_REF_FAM.objects.create(
                    asociado = Asociado,
                    nombre = refFamNomCom,
            )
            
            Aso_ref_fam.telefono = reffam['data']['celular']
            Aso_ref_fam.ocupacion = reffam['data']['ocupacion']    
            Aso_ref_fam.direccion = reffam['data']['direccion']
                
        for refPer in anteia1['arrayData'][idsocio]['coorinoquia.referenciasPersonales']['data']:
            refPerNom = refPer['data']['nombreCompleto']
            Aso_ref_per = justoAppModels.ASO_REF_PER.objects.filter(asociado = Asociado,nombre = refPerNom).first()
            if Aso_ref_per == None:
                Aso_ref_per = justoAppModels.ASO_REF_PER.objects.create(
                    asociado = Asociado,
                    nombre = refPerNom,
            )
            Aso_ref_per.direccion = refPer['data']['direccion']    
            Aso_ref_per.ocupacion = ''
            Aso_ref_per.celular = refPer['data']['telefono']
            Aso_ref_per.save()
init()