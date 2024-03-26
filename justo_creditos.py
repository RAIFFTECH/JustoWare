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
from datetime import datetime,timedelta
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd
from django.db.models import Q
from decimal import Decimal, ROUND_DOWN
from django.db.models import Sum,Max
from io import BytesIO
from django.http import HttpResponse
import numpy as np
import math

PERIODICIDAD = {
        'SEMANAL': 'E',
        'QUINCENAL': 'U',
        'MENSUAL': 'M',
        'BIMENSUAL': 'B',
        'TRIMESTRAL': 'T',
        'CUATRIMESTRAL': 'C',
        'QUINQUENAL': 'Q',
        'SEMESTRAL': 'S',
        'ANUAL': 'A',
    }

TIPOS_MOV_CRE = {
        'DESEM': 'A',
        'REFIN': '0',
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

def asignar_fecha(fecha_str, formato='%m/%d/%Y'):
    try:
        fecha = datetime.strptime(fecha_str, formato)
        fecha_validada = fecha.date()
        return fecha_validada
    except ValueError:
        return None

def truncar(numero, num_decimales):
    return float(Decimal(str(numero)).quantize(Decimal(10) ** -num_decimales, rounding=ROUND_DOWN))

def gomonth(fecha, meses):
    return fecha + relativedelta(months=meses)

def cargue_mov_cre(iCodCre,valores):
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    Credito = justo.CREDITOS.objects.filter(oficina=Oficina,cod_cre = iCodCre).first()
    xTotSal = 0
    xNumCre = 0
    valores[0] = Credito.tian_ic_act
    valores[1] = Credito.per_ano
    valores[2] = Credito.cap_ini
    valores[3] = Credito.tian_im
    valores[4] = Credito.por_des_pro_pag
    valores[5] = Credito.per_ano
    valores[6] = Credito.tian_ic_act
    valores[7] = Credito.for_pag
    valores[8] = Credito.fec_des
    valores[9] = Credito.val_cuo_act
    queryset1 = justo.CREDITOS_CAUSA.objects.values('fecha', 'cuota') \
        .filter(oficina=Oficina, cod_cre=Credito.cod_cre,comprobante = None) \
        .annotate(
        tipmov=Value('1'),
        kapital=F('capital'),
        intcor=F('int_cor'),
        intmor=Value(0, output_field=IntegerField()),
        polseg=Value(0, output_field=IntegerField()),
        despp=Value(0, output_field=IntegerField()),
        acreed=Value(0, output_field=IntegerField())
    )
    queryset2 = justo.DETALLE_PROD.objects.filter(oficina=Oficina, producto='CR', subcuenta=Credito.cod_cre) \
        .values(fecha=F('hecho_econo__fecha')) \
        .annotate(
            cuota=Value(0),
            tipmov=Case(
                *[When(concepto=concept, then=Value(value)) for concept, value in TIPOS_MOV_CRE.items()],
                    output_field=CharField()
            ),
            kapital=Coalesce(Sum(Case(When(detalle_econo__item_concepto='Kapita', then=-F('detalle_econo__valor_2')+F('detalle_econo__valor_1')))), Value(0.0)),
            intcor=Coalesce(Sum(Case(When(detalle_econo__item_concepto='IntCor', then=-F('detalle_econo__valor_2')+F('detalle_econo__valor_1')))), Value(0.0)),
            intmor=Coalesce(Sum(Case(When(detalle_econo__item_concepto='IntMor', then=-F('detalle_econo__valor_2')+F('detalle_econo__valor_1')))), Value(0.0)),
            polseg=Coalesce(Sum(Case(When(detalle_econo__item_concepto='PolSeg', then=-F('detalle_econo__valor_2')+F('detalle_econo__valor_1')))), Value(0.0)),
            despp=Coalesce(Sum(Case(When(detalle_econo__item_concepto='DesPP', then=-F('detalle_econo__valor_2')+F('detalle_econo__valor_1')))), Value(0.0)),
            acreed=Coalesce(Sum(Case(When(detalle_econo__item_concepto='Acreed', then=-F('detalle_econo__valor_2')+F('detalle_econo__valor_1')))), Value(0.0)) 
        )
    queryset3 = justo.CAMBIOS_CRE.objects.filter(det_pro__oficina=Oficina, det_pro__producto='CR', det_pro__subcuenta=Credito.cod_cre) \
        .values('fecha') \
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
    return tab_liq if len(tab_liq)>0 else None
     
def calculo_cuota(ikapital,iTIEA,iTIDIC,iPerio,iNumCuo,iFecDes,iFecPagIni,iNumCuoGra=0,iTIDPS=0,iIntCorAnt=0):
    xDias = 0
    xMeses = 0
    if iPerio == 'E':
        xDias = 7
    elif iPerio == 'U':
        xDias = 15
    elif iPerio == 'M':
        xMeses = 1
        xPerAno = 12
    elif iPerio == 'B':
        xMeses = 2
        xPerAno = 6
    elif iPerio == 'T':
        xMeses = 3
        xPerAno = 4
    elif iPerio == 'C':
        xMeses = 4
        xPerAno = 3
    elif iPerio == 'Q':
        xMeses = 5
        xPerAno = 5/12
    elif iPerio == 'S':
        xMeses = 6
        xPerAno = 2
    elif iPerio == 'A':
        xMeses = 12
        xPerAno = 1
    if iTIEA == 0:
        return(int(ikapital/iNumCuo)+1)
    iTIEA = round(iTIEA,4)
    if xMeses != 0:
        xTasPer = round((iTIEA+1)**(1/xPerAno)-1,4)
    elif xDias == 7:
        xTasPer = round((iTIEA+1)**(1/52.1428)-1,4)
    elif xDias == 15:
        xTasPer = round((iTIEA+1)**(1/24)-1,4)
    xValCuo = int(ikapital*xTasPer/round(1-(1+xTasPer)**(-iNumCuo),4)+1)
    xCiclos = 0
    xSaldoAnt = 0
    xValcuoAnt = 0
    x0 = xValCuo
    while True:
        xCiclos = xCiclos + 1
        xFecAnt = iFecDes
        xFecPagFin = iFecDes
        xSaldo = ikapital
        xFecCuo = iFecPagIni
        xIntPorApl = iIntCorAnt
        xIntApl = 0
        for xPer in range(1,iNumCuo+iNumCuoGra+1):
            xDifDias = (xFecCuo-xFecAnt).days
            xIntIC = round(xSaldo * iTIDIC * 1000,0)
            xIntIC = round(xIntIC/1000,0)*xDifDias
            xIntPS = round(xSaldo * iTIDPS * 1000,0)*(xDifDias)
            xIntPS = round(xIntPS/1000,0)*(xDifDias)
            xIntPer = xIntIC + xIntPS + xIntPorApl
            xCapPer = round(xValCuo-xIntApl-xIntPer if xPer > iNumCuoGra and xValCuo-xIntApl-xIntPer > 0 else 0)
            xNueCapPer = xCapPer 
            # xCapPer= xCapPer + si tiene cuotas extras  
            xIntApl = xIntApl + (xIntPer if xPer < iNumCuoGra else 0)
            xIntApl = xIntApl + (xValCuo - xNueCapPer - xIntPer if xIntPorApl > 0 else 0)
            xIntApl = xIntApl if xIntApl > 0 else 0
            #xIntPorApl = xIntPorApl - xIntPer
            xFecAnt = xFecCuo
            xSaldo = xSaldo - xCapPer 
            xFecPagFin = xFecCuo
            if xMeses > 0 :
                xFecCuo = gomonth(iFecPagIni,xMeses*xPer)
            elif iPerio == 'E':
                xFecCuo = xFecCuo + 7
            elif  xPer % 2 == 1:
                xFecCuo = xFecCuo + 15
            else:
                xFecCuo = gomonth(xFecCuo-15,1)
        if ((xSaldo > -(iNumCuo+iNumCuoGra)*3) or xCiclos  >= 10) and (xSaldo < 1 or round(xSaldo/(iNumCuo+iNumCuoGra),0) == 0):
            break
        if xCiclos == 1:
            y0 = xSaldo
            xValCuo = xValCuo + round(xSaldo/(iNumCuo+iNumCuoGra),0)
            x1 = xValCuo
        else:
            y1 = xSaldo
            if y1 == y0:
                xValCuo = xValCuo + (1 if y1 < 0 else -1)
            else:
                xValCuo = round(x1 - y1*(x1-x0)/(y1-y0),0)
            if xValCuo == x1:
                xValCuo = xValCuo + (1 if xSaldo > 0 else -1)
            x0 = x1
            x1 = xValCuo
            yo = y1
    return(xValCuo)        

class Liquida_cre:
    cod_cre = ''
    cap_ini = 0
    fecha_focal = None
    lista_mov = []
    val_cuo = 0
    fec_des = None
    for_pag = ' '
    sal_cap_tot = -1
    sal_cap_dia = -1
    sal_int_dia = -1
    sal_ps_dia = -1
    sal_int_mor = -1
    int_cau_fra = -1
    int_aju_pa = -1
    int_aju_ac = -1
    int_pag_tot = 0
    altura = -1
    cuo_pag = -1
    cuo_pac = -1
    fec_al_dia = None
    fec_ven = None
    tas_ic_ea = 0.0
    tas_ic_dia = 0.0
    tas_im_anual = 0.0
    por_des_pp = 0.0
    per_ano = 0
    tip_pag = ''
    capital_a_pag = 0
    int_cor_a_pag = 0
    pol_seg_a_pag = 0
    int_mor_a_pag = 0
    acreedor_a_pag = 0
    int_mor_cau = -1
    aju_cap_a_pag = 0
    aju_ic_a_pag = 0
    aju_ps_a_pag = 0
    aju_im_a_pag = 0
    max_pag_couta = 0
    min_pag_aboca = 0
    min_pag_abocu = 0
    fec_sig_pag1 = None
    fec_sig_pag2 =None
    tip_pag = 'DESEM'
    int_pag_per = 0
    int_condo = 0
    
    def __init__(self, iCodCre, iFecha_Focal = datetime.now().date()):
        self.cod_cre = iCodCre
        self.fecha_focal = iFecha_Focal 
        params = [0.0,0,0,0.0,0.0,0,0.0,' ',date(1900,1,1),0]
        self.lista_mov = cargue_mov_cre(iCodCre,params) 
        if self.lista_mov == None:
            return 
        self.cap_ini = params[2]
        xTasIntPer = round((params[0]/100+1)**(1/params[1])-1,6)
        self.tas_ic_dia = round(xTasIntPer*params[1]*100/36525,6)
        #xTasNomAnu = ((params[0]/100+1)**(1/params[1])-1)*1200
        #self.tas_ic_dia = truncar(xTasNomAnu/36525,6)

        self.tas_im_anual = params[3]
        self.por_des_pp = params[4]
        self.per_ano = params[5]
        self.tas_ic_ea = params[6]
        self.for_pag = params[7]
        self.fec_des = params[8]
        self.fec_al_dia = params[8]
        self.val_cuo = params[9]
        self.fec_ven = params[8]
        self._calculos_generales()
        return 
 
    def _calculos_generales(self):
        xCapIni = 0
        xCapCau = 0
        xCapPag = 0
        self.sal_cap_tot = 0
        self.sal_cap_dia = 0
        xFecPag = None
        for reg in self.lista_mov:
            if reg['tipmov'] == 'A':
                self.fec_des = reg['fecha']
                self.fec_al_dia = reg['fecha']
            #    self.cap_ini = reg['kapital']  
                continue
            self.sal_cap_tot = self.sal_cap_tot + (reg['kapital'] if (reg['fecha'] - self.fecha_focal).days <= 0 or reg['tipmov'] == '0' or reg['tipmov'] == '1' else 0)
            xCapPag = xCapPag + (reg['kapital'] if reg['fecha'] <= self.fecha_focal and reg['tipmov'] != '1' else 0)
            self.sal_cap_dia = self.sal_cap_dia + (reg['kapital'] if reg['fecha'] <= self.fecha_focal else 0)
            if reg['fecha'] <= self.fecha_focal and reg['tipmov'] == '1':
                self.altura = reg['cuota']
        xYaApl = False
        for reg in self.lista_mov:
            if reg['tipmov'] == 'A':
                continue
            if reg['tipmov'] == '0' or reg['tipmov'] == '1':
                xCapCau = xCapCau + reg['kapital']
                if xCapCau + xCapPag > 0:
                    if xYaApl == False:
                        self.fec_al_dia = reg['fecha']
                        self.cuo_pag = reg['cuota'] - 1
                        xYaApl = True
                else:
                    xYaApl = False
            if reg['kapital'] > 0 and reg['intcor'] != 0:
                self.cuo_pac = reg['cuota']
                self.fec_ven = reg['fecha']

    def calculo_periodo(self):
        self.int_pag_per = 0
        self.int_condo = 0
        lista_periodo = [objeto for objeto in self.lista_mov if objeto['fecha'].year == self.fecha_focal.year and objeto['fecha'].month == self.fecha_focal.month and objeto['tipmov'] > '3']
        for reg in lista_periodo:
            if reg['tipmov'] > '3':
                self.int_pag_per = self.int_pag_per - reg['intcor']
            else:
                self.int_condo = self.int_condo = 0 - reg['intcor']
        return

    def liq_al_dia(self,ifecha_focal = datetime.now().date(),recarga = False):
        if self.fecha_focal != ifecha_focal or recarga == True:
            self.fecha_focal = ifecha_focal 
            params = [0.0,0,0,0.0,0.0,0,0.0,' ',date(1900,1,1),0]
            self.lista_mov = cargue_mov_cre(self.cod_cre)
            self._calculos_generales()
        self.sal_int_dia = 0
        self.sal_int_mor = 0
        self.int_mor_cau = 0
        self.sal_ps_dia = 0
        self.int_cau_fra = 0
        self.int_aju_pa = 0
        self.int_pag_tot = 0
        oIntPagTot = 0    #  sirve  no 
        oIntAjuAboCap = 0
        xDiaConIntMor = 0
        xSalPro = xSalRea = xSalProDia = xSalReaDia = self.cap_ini
        xFecCer = self.fec_des
        xFecUltPag = xFecCer
        xFecUltCau = xFecCer
        xFecCauCapNeg = datetime(1900, 1, 1).date()
        xFecRefMor = self.fecha_focal + timedelta(days=1)
        xSalCuoPag = 0
        lista_al_dia = [objeto for objeto in self.lista_mov if objeto['fecha'] <= self.fecha_focal and objeto['tipmov'] != 'A']
        for reg in lista_al_dia:
            self.sal_int_dia = self.sal_int_dia + reg['intcor']
            self.sal_int_mor = self.sal_int_mor + reg['intmor']
            self.sal_ps_dia = self.sal_ps_dia + reg['polseg']
            if reg['tipmov'] == '0' or reg['tipmov'] == '1':
                xFecUltCau = reg['fecha'] 
                if reg['fecha'] < self.fecha_focal:
                    xSalPro = xSalPro - reg['kapital']
                if reg['kapital'] < 0:
                    xFecCauCapNeg = reg['fecha'] 
            else:
                if reg['tipmov'] >= '5': 
                    xFecUltPag = reg['fecha'] if reg['fecha'] <= self.fec_ven else self.fec_ven
                    xFecRefMor = reg['fecha']
                    xSalCuoPag = xSalCuoPag + reg['kapital']
                    oIntPagTot = oIntPagTot - reg['intcor']
        self.int_pag_tot = oIntPagTot 
        xFecAntMov = xFecUltCau
        xSalReaAnt = xSalRea
        oIntPagPosDia = 0
        xYaAjuIntAnt = False
        for reg in lista_al_dia:
            if reg['tipmov'] == '3' and reg['fecha'] > xFecUltCau and reg['fecha'] >= xFecUltPag and xFecUltPag <= self.fecha_focal and xFecUltPag >= xFecUltCau:
                oIntAjuAboCap = oIntAjuAboCap - (reg['int_cor'] if reg['intcor'] < 0 else 0)
            if reg['fecha'] <= xFecUltCau:
                xSalProDia = xSalProDia - (reg['kapital'] if reg['tipmov'] == '1' else 0)
                xSalReaDia = xSalReaDia + (reg['kapital'] if reg['tipmov'] >= '4' else 0)
                if reg['fecha'] == xFecUltCau and reg['tipmov'] == '4':
                    xYaAjuIntAnt = True
                else:
                    oIntPagPosDia = oIntPagPosDia- (reg['intcor'] if reg['tipmov'] else 0)
            if  reg['tipmov'] >= '5': 
                xSalReaAnt = xSalRea
                xSalRea = xSalRea + reg['kapital']
                if reg['fecha'] > xFecUltCau: 
                    self.int_cau_fra = self.int_cau_fra + int((xSalPro if xSalPro <= xSalRea else (xSalPro if xSalPro <= xSalReaAnt else xSalReaAnt))*(reg['fecha']-xFecAntMov).days*self.tas_ic_dia)
                    xFecAntMov = reg['fecha']
            if  reg['tipmov'] == '1': 
                if xSalCuoPag < 100:
                    oFecUltCuoPag = reg['fecha']
                xSalCuoPag = xSalCuoPag + reg['kapital']
                if  reg['fecha'] > xFecCauCapNeg:  
                    if xSalCuoPag > 0:
                        if reg['fecha'] <= xFecRefMor and xFecRefMor <= self.fecha_focal:
                            xDiaMor = ((self.fecha_focal-xFecRefMor).days if (xFecRefMor-reg['fecha']).days > xDiaConIntMor else (self.fecha_focal-reg['fecha']).days)
                            xDiaMor = xDiaMor if (self.fecha_focal-reg['fecha']).days > xDiaConIntMor else 0 
                        else:
                            xDiaMor = (self.fecha_focal - reg['fecha']).days
                            xDiaMor = xDiaMor if xDiaMor > xDiaConIntMor else 0
                        self.int_mor_cau = self.int_mor_cau + round((reg['kapital'] if xSalCuoPag > reg['kapital'] else xSalCuoPag)*xDiaMor*self.tas_im_anual/36525,0)
        if (self.fecha_focal - xFecAntMov).days > 0:
            self.int_cau_fra = self.int_cau_fra + int((xSalPro if xSalPro < xSalRea else xSalRea)*(self.fecha_focal-xFecAntMov).days*self.tas_ic_dia)
        xBasCapAju = xSalProDia - xSalReaDia
        xBasCapAju  = 0 if xYaAjuIntAnt else xBasCapAju
        self.int_aju_ac = oIntAjuAboCap
        for reg in self.lista_mov:
            if reg['tipmov'] == '1':
                if xBasCapAju > 0:
                    xBasCap = reg['kapital'] if reg['kapital'] < xBasCapAju else xBasCapAju
                    self.int_aju_pa = self.int_aju_pa + round(xBasCap*(reg['fecha']-xFecUltCau).days*self.tas_ic_dia,0)
                    xBasCapAju = xBasCapAju - xBasCap
                xSalPro = xSalPro - reg['kapital']
                if xSalCuoPag < 100:
                    oFecUltCuoPag = reg['fecha']
                xSalCuoPag = xSalCuoPag + reg['kapital']
        self.capital_a_pag = self.sal_cap_dia
        self.int_cor_a_pag = self.sal_int_dia
        self.pol_seg_a_pag = self.sal_ps_dia
        self.int_mor_a_pag = self.int_mor_cau if self.for_pag == 'P' else 0
        lista_final = [objeto for objeto in self.lista_mov if objeto['fecha'] > self.fecha_focal and objeto['tipmov'] == '1']
        xSig = 0
        for reg in lista_final:
            if xSig == 0:
                self.fec_sig_pag1 = reg['fecha']
                xDia1 = (self.fec_sig_pag1 - self.fecha_focal).days
                xMaxSaldo = self.val_cuo / (self.tas_ic_dia*xDia1) 
                self.min_pag_aboca = self.int_cor_a_pag + self.pol_seg_a_pag + self.int_mor_a_pag +self.int_cau_fra
                self.min_pag_aboca = self.min_pag_aboca + (self.sal_cap_dia if self.sal_cap_tot - self.sal_cap_dia < xMaxSaldo else  xMaxSaldo - self.sal_cap_tot)
            elif xSig == 1:
                self.fec_sig_pag2 = reg['fecha']
                xDia2 = (self.fec_sig_pag2 - self.fecha_focal).days
                xMaxSaldo = self.val_cuo / (self.tas_ic_dia*xDia2) 
                self.min_pag_abocu = self.int_cor_a_pag + self.pol_seg_a_pag + self.int_mor_a_pag +self.int_cau_fra
                self.min_pag_abocu = self.min_pag_abocu + (self.sal_cap_dia if self.sal_cap_tot - self.sal_cap_dia < xMaxSaldo else  xMaxSaldo - self.sal_cap_tot)
            else:
                break
            xSig = xSig + 1    
 
    def liq_por_cuotas(self,iAltura):
        tip_pag = 'CUOTA'
        xDiaConIntMor = 0
        xCapIni = self.cap_ini
        xSalPro = self.cap_ini
        xSalRea = xSalPro
        xTasIntPer = 0
        zTasDesIntPer = self.por_des_pp/(self.per_ano*100)
        xTasIntDesDia = self.por_des_pp/36525
        xFecCer = self.fec_des
        xFecUltPag = self.fecha_focal + timedelta(days=1)
        xFecUltCau = xFecCer
        Anticipo = True
        xCapPag = xIntPag = xMorPag = xPolSegPag = xMorCau = 0
        lista_al_dia = [objeto for objeto in self.lista_mov if objeto['fecha'] <= self.fecha_focal and objeto['tipmov'] != 'A']
        for reg in lista_al_dia:
            if reg['tipmov'] != '1' :
                xSalRea = xSalRea + reg['kapital']
                xCapPag = xCapPag - reg['kapital']
                xIntPag = xIntPag - reg['intcor']
                xMorPag = xMorPag - (reg['intmor'] if reg['tipmov'] >= '5' else 0)
                xMorCau = xMorCau + (reg['intmor'] if reg['tipmov'] == '2' else 0)
                xPolSegPag = xPolSegPag - reg['polseg']
                xFecUltPag = reg['fecha']
            else:
                if reg['fecha'] < self.fecha_focal:
                    xSalPro = xSalPro - reg['kapital']
        xCapMor = -xCapPag
        xMorAnt = 0
        xMorAcu = xMorCau - xMorPag
        xMorYaPag = 0
        if xFecUltPag <= self.fecha_focal:
            for reg in lista_al_dia:
                if reg['tipmov'] == '1' :
                    xCapMor = xCapMor + reg['kapital']
                    xMorAcu = xMorAcu + reg['intmor']
                    if xCapMor > 0:
                        xDiaMor1 = ((self.fecha_focal if xFecUltPag > self.fecha_focal else xFecUltCau) - reg['fecha']).days
                        xDiaMor1 = xDiaMor1 if xDiaMor1 > xDiaConIntMor else 0
                        xMorAnt = xMorAnt + round(reg['kapital'] if xCapMor > reg['kapital'] else xCapMor*xDiaMor1*self.tas_im_anual/36525,0)
            xMorYaPag = xMorAnt - xMorAcu
        xCapCau = xIntCau = xPolSegCau = 0
        xMorCauCuo = 0
        xFecUltPer = xFecCer
        for reg in lista_al_dia:
            if reg['tipmov'] == '1' :
                xCapCau = xCapCau + reg['kapital']
                xIntCau = xIntCau + reg['intcor']
                xPolCau = xPolSegCau + reg['polseg']
                if xCapCau >= xCapPag:
                    oCapital = xCapCau - xCapPag
                    oIntCor = xIntCau - xIntPag
                    oIntMor = xMorCau - xMorPag
                    oPolSeg = xPolSegCau - xPolSegPag
                    if reg['fecha'] == self.fecha_focal:
                        xSalPro = xSalPro - reg['kapital']
                    if reg['fecha'] <= xFecUltPag:
                        xDiaMor1 = ((self.fecha_focal if xFecUltPag > self.fecha_focal else xFecUltPag)- reg['fecha']).days
                        xDiaMor1 = xDiaMor1 if xDiaMor1 > xDiaConIntMor else 0
                        xDiaMor2 = (self.fecha_focal - xFecUltPag).days if oCapital > reg['kapital'] else 0
                        xMorCauAnt = round((reg['kapital'] if oCapital > reg['kapital']  else oCapital)*xDiaMor1*self.tas_im_anual/36525,0)
                        if xMorYaPag > 0:
                            if xMorYaPag > xMorCauAnt:
                                xMorYaPag = xMorYaPag - xMorCauAnt
                                xMorCauAnt = 0
                            else:
                                xMorCauAnt = xMorCauAnt - xMorYaPag
                                xMorYaPag = 0
                        xMorCauPer = xMorCauAnt + round((reg['kapital'] if oCapital > reg['kapital'] else oCapital)*xDiaMor2*self.tas_im_anual/36525,0)
                        xDiaMor = (self.fecha_focal - reg['fecha']).days if xFecUltPag > self.fecha_focal else (self.fecha_focal - xFecUltPag).days
                        xMorCauCuo = xMorCauCuo + xMorCauPer
                    else:
                        xDiaMor = (self.fecha_focal - reg['fecha']).days if (self.fecha_focal - reg['fecha']).days > xDiaConIntMor  else 0
                        xMorCauPer = round((reg['kapital'] if oCapital > reg['kapital'] else oCapital)*xDiaMor*self.tas_im_anual/36525,0)
                        xMorCauCuo = xMorCauCuo + xMorCauPer
                    if reg['cuota'] == iAltura:
                        Anticipo = False
                        break
            xFecUltPer = reg['fecha']
        oCapital = xCapCau - xCapPag
        oIntCor = xIntCau - xIntPag
        oIntMor = xMorCauCuo
        oPolSeg = xPolSegCau - xPolSegPag
        oIntAnt = 0
        print(oCapital,oIntCor,oIntMor)
        if Anticipo :
            lista_al_dia = [objeto for objeto in self.lista_mov if objeto['fecha'] > self.fecha_focal]
            for reg in lista_al_dia:
                oCapital = oCapital + reg['kapital'] 
                oIntCor = oIntCor + reg['intcor'] 
                oIntMor = oIntMor + reg['intmor'] 
                oPolSeg  = oPolSeg + reg['polseg'] 
                if reg['tipmov'] == '1':
                    xCapPer = oCapital if oCapital < reg['kapital'] else reg['kapital']
                    xCapPer = xCapPer if xCapPer > 0 else 0
                    xIntPer = oIntCor if oIntCor < reg['intcor'] and oIntCor >= 0 else (0 if oIntCor < 0  else reg['intcor'])
                    xFacInt = ((reg['fecha']-self.fecha_focal).days if (reg['fecha']-self.fecha_focal).days > 0 else 0)*self.tas_ic_dia
                    xConIntAnt = round(xCapPer*self.tas_ic_dia,0)*((reg['fecha']-self.fecha_focal).days if (reg['fecha']-self.fecha_focal).days > 0 else 0)
                    oIntAnt = oIntAnt + xConIntAnt
                    if reg['cuota'] == iAltura:
                        break
        print(oCapital,oIntCor,oIntMor)

    def distri_pago_cuota(self,iValPorDis):
        self.tip_pag = TIPOS_MOV_CRE['CUOTA']
        oAboCap = oAboIntCor = oAboIntMor = oAboPolSeg = oConIntAnt = oCauIntMor = oSalTot = zConIntAnt = 0
        oSalTot = self.cap_ini
        xSalPro = oSalTot
        xSalRea = xSalPro
        xDiaConIntMor = 0
        xFecCer = self.fec_des
        xTasIntPer = round((round(self.tas_ic_ea/100,4)+1)**(1/self.per_ano),4)
        xTasDesIntPer = 0
        xFecUltPag = xFecCer - timedelta(days=1)
        xFecUlpPagMor = xFecCer - timedelta(days=1)
        xAboCap = xAboIntCor = xAboIntMor = xAboPolSeg = xMenosUltPag = xMorYaPag = 0
        xFecCauCapNeg = datetime(1900, 1, 1).date()
        lista_al_dia = [objeto for objeto in self.lista_mov if objeto['fecha'] <= self.fecha_focal and objeto['tipmov'] != 'A']    
#   Uno
        for reg in lista_al_dia:
            if reg['tipmov'] != '1':
                xSalRea = xSalRea + reg['kapital']
                oSalTot = oSalTot + reg['kapital']
                xAboCap = xAboCap + reg['kapital']
                xAboIntCor = xAboIntCor + reg['intcor']  
                xAboIntMor = xAboIntMor + reg['intmor']
                xAboPolSeg = xAboPolSeg + reg['polseg']
                if reg['tipmov'] >= "5":
                    xFecUltPag = reg['fecha']
                    xMenosUltPag = reg['kapital']
            else:  
                if reg['kapital'] < 0:
                    xFecCauCapNeg = reg['fecha']
                if reg['fecha'] < self.fecha_focal:
                    xSalPro = xSalPro - reg['kapital']
            if reg['tipmov'] == '2':
                xMorYaPag = reg['acreed'] 
        
        xAntAboCap = xAboCap - xMenosUltPag
        xSalPorDis = iValPorDis
        oAboIntMor = 0
#  Solamente Causdaciones al dia 
        lista_al_dia = [objeto for objeto in self.lista_mov if objeto['fecha'] <= self.fecha_focal and objeto['tipmov'] == '1']    
        for reg in lista_al_dia:
            xAboCap = xAboCap + reg['kapital']
            xAntAboCap = xAntAboCap + reg['kapital']
            xAboIntCor = xAboIntCor + reg['intcor']
            xAboIntMor = xAboIntMor + reg['intmor']
            xAboPolSeg = xAboPolSeg + reg['polseg']
            if xAboCap > 0 or xAboIntCor > 0 or xAboPolSeg > 0:
                if reg['fecha'] == self.fecha_focal:
                    xSalPro = xSalPro - reg['kapital']
                xCapPer = xAboCap
                xIntPer = xAboIntCor if xAboIntCor > 0 else 0
                xPolSegPer = xAboPolSeg if xAboPolSeg > 0 else xAboPolSeg
                xIntMorDes = 0
                if not (reg['fecha'] + timedelta(days=35) > xFecCauCapNeg  and  reg['fecha'] < xFecCauCapNeg):
                    if reg['fecha'] < xFecUltPag:
                        if xFecUltPag > self.fecha_focal:
                            xDiaMor1 = 0
                            xMorCauAnt = 0
                            xDiaMor2 = (self.fecha_focal - reg['fecha']).days
                            xDiaMor2 = xDiaMor2 if xDiaMor2 > xDiaConIntMor else 0
                            xMoorCauNvo = round((reg['fecha'] if xCapPer > reg['fecha'] else xCapPer) * xDiaMor2*(self.tas_im_anual/36525),0)
                        else:
                            xDiaMorIni = xFecUltPag - reg['fecha']
                            xDiaMor1 = xDiaMorIni
                            xDiaMor1 = xDiaConIntMor if xDiaMor1 > xDiaConIntMor else 0
                            if xAntAboCap > 0:
                                xMorCauAnt = round((reg['kapital'] if xAntAboCap > reg['kapital'] else xAntAboCap)*xDiaMor1*(self.tas_im_anual/36525),0)
                            else:
                                xMorCauAnt = 0
                            xDiaMor2 = (self.fecha_focal - xFecUltPag).days + (xDiaMorIni if xDiaMorIni != xDiaMor1 else 0)
                            xDiaMor2 = xDiaMor2 if xDiaMor2 > xDiaConIntMor else 0
                            xMorCauNvo = round((reg['kapital'] if xCapPer > reg['kapital'] else xCapPer)*xDiaMor2*(self.tas_im_anual/36525),0)
                        xMorCauAnt = 0 if reg['fecha'] <= xFecUlpPagMor else xMorCauAnt
                        if xMorYaPag > 0:
                            if xMorYaPag > xMorCauAnt:
                                xIntMorDes = xMorCauAnt 
                                xMorYaPag = xMorYaPag - xMorCauAnt
                                xMorCauAnt = 0
                            else:
                                xIntMorDes = xMorYaPag 
                                xMorCauAnt = xMorCauAnt-xMorYaPag
                                xMorYaPag = 0
                        xMorCauPer = xMorCauAnt + xMorCauNvo
                        oCauIntMor = oCauIntMor + xMorCauNvo
                    else:
                        xDiaMor = (self.fecha_focal - reg['fecha']).days
                        xDiaMor = xDiaMor if xDiaMor > xDiaConIntMor else 0
                        xMorCauPer = round((reg['kapital'] if xCapPer > reg['kapital'] else xCapPer)*xDiaMor*(self.tas_im_anual/36525),0)
                        oCauIntMor = oCauIntMor + xMorCauPer  
                else:
                    xMorCauNvo = 0
                    xMorCauPer = 0
                xPrimero = True
#  TRES
                for rega in lista_al_dia[lista_al_dia.index(reg):]:
                    if xSalPorDis <= 0:
                        break
                    if xPrimero == False :
                        xAboCap = xAboCap + rega['kapital']
                        xAntAboCap = xAntAboCap + rega['kapital']
                        xAboIntCor = xAboIntCor + rega['intcor']  
                        xAboIntMor =xAboIntMor + rega['intmor']
                        xAboPolSeg = xAboPolSeg + rega['polseg']
                        xCapPer = rega['kapital'] if rega['kapital'] < xAboCap else xAboCap
                        xCapPer = xCapPer if xCapPer > 0 and xFecCauCapNeg < self.fecha_focal else 0
                        xIntPer = rega['intcor'] if rega['intcor'] < xAboIntCor else xAboIntCor
                        xIntPer = xIntPer if xIntPer > 0 else 0
                        if rega['fecha'] == self.fecha_focal:
                            xSalPro = xSalPro - rega['kapital']
                        xPolSegPer = rega['polseg'] if rega['polseg'] < xAboPolSeg else xAboPolSeg
                        xPolSegPer = xPolSegPer if xPolSegPer > 0 else 0        
                        xIntMorDes=0 
                        if rega['fecha'] <= xFecUltPag:
                            if xFecUltPag > self.fecha_focal:
                                xDiaMor1 = 0
                                xDiaMor2 = (self.fecha_focal- rega['fecha']).days
                            else:
                                xDiaMor1 = (xFecUltPag - rega['fecha']).days
                                xDiaMor2 = (self.fecha_focal - xFecUltPag).days + (xDiaMor1 if xDiaMor1 <= xDiaConIntMor else 0)
                            xDiaMor1 = xDiaMor1 if xDiaMor1 > xDiaConIntMor else 0
                            if xAntAboCap > 0:
                                xMorCauAnt = round((rega['kapital'] if xAntAboCap > rega['kapital'] else xAntAboCap)*xDiaMor1*(self.tas_im_anual/36525),0)
                            else:
                                xMorCauAnt = 0
                            if xMorYaPag > 0:
                                if xMorYaPag > xMorCauAnt:
                                    xIntMorDes = xMorCauAnt
                                    xMorYaPag = xMorYaPag-xMorCauAnt
                                    xMorCauAnt = 0
                                else:
                                    xIntMorDes = xMorYaPag 
                                    xMorCauAnt = xMorCauAnt - xMorYaPag
                                    xMorYaPag = 0
                            xDiaMor2 = xDiaMor2 if xDiaMor1+xDiaMor2>xDiaConIntMor else 0
                            xMorFra = round((rega['kapital'] if xCapPer > rega['kapital'] and rega['kapital'] > 0 else (xCapPer if xCapPer <= rega['kapital'] else 0))*xDiaMor2*(self.tas_im_anual/36525),0)
                            xMorCauPer = xMorCauPer + xMorFra
                            oCauIntMor = oCauIntMor + xMorFra
                        else:
                            xDiaMor = (self.fecha_focal - rega['fecha']).days
                            xDiaMor = xDiaMor if xDiaMor > xDiaConIntMor else 0
                            xMorCauPer = round((rega['kapital'] if xAboCap > rega['kapital'] and rega['kapital'] > 0 else (xAboCap if xAboCap <= rega['kapital'] else 0))*xDiaMor*(self.tas_im_anual/36525),0)
                            oCauIntMor = oCauIntMor + xMorCauPer 
                    xPrimero = False
                    if xPolSegPer > 0:
                        if xSalPorDis >= xPolSegPer:
                            oAboGasPol = oAboGasPol + xPolSegPer
                            xSalPorDis = xSalPorDis - xPolSegPer
                        else:
                            oAboPolSeg = oAboGasPol + xSalPorDis
                            xSalPorDis = 0
                    xMorCauPer = xMorCauPer if self.for_pag != 'L' else 0
                    if xMorCauPer > 0:
                        if xSalPorDis >= xMorCauPer:
                            oAboIntMor = oAboIntMor + xMorCauPer
                            xSalPorDis = xSalPorDis - xMorCauPer
                        else:
                            oAboIntMor = oAboIntMor + xSalPorDis 
                            xSalPorDis = 0
                    if xIntPer > 0 :
                        if xSalPorDis >= xIntPer:
                            oAboIntCor = oAboIntCor + xIntPer
                            xSalPorDis = xSalPorDis - xIntPer
                        else:
                            oAboIntCor = oAboIntCor + xSalPorDis
                            xSalPorDis = 0
                    if xCapPer >= 0 and xFecCauCapNeg < rega['fecha']: 
                        if xSalPorDis >= xCapPer:
                            oAboCap = oAboCap + xCapPer
                            xSalPorDis = xSalPorDis - xCapPer 
                        else:
                            oAboCap = oAboCap + xSalPorDis
                            xSalPorDis = 0
                    else:
                        oAboCap = 0
#  causar la mora total si paga algo pero no queda al dia avanza al sigiente regisdtro 
                for regb in lista_al_dia[lista_al_dia.index(rega) + 1:]:
                    xAboCap = xAboCap + regb['kapital'] 
                    xAboIntCor = xAboIntCor + regb['intcor']   
                    xAboIntMor = xAboIntMor + regb['intmor'] 
                    xAboPolSeg = xAboPolSeg + regb['polseg'] 
                    if regb['fecha'] <= xFecUltPag and xAboCap > 0:
                        xDiaMor = (self.fecha_focal - regb['fecha']).days if xFecUltPag > self.fecha_focal else  (self.fecha_focal - xFecUltPag).days
                        xDiaMor = xDiaMor if xDiaMor > xDiaConIntMor else 0
                        oCauIntMor = oCauIntMor + round((rega['kapital'] if xAboCap > rega['kapital'] else xAboCap)*xDiaMor if xDiaMor > 0 else 0*(self.tas_im_anual/36525),0)
                    else:
                        xDiaMor = (self.fecha_focal - regb['fecha']).days if (self.fecha_focal - regb['fecha']).days > 0 else 0
                        xDiaMor = xDiaMor if xDiaMor > xDiaConIntMor else 0
                        oCauIntMor = oCauIntMor + round((rega['kapital'] if xAboCap > rega['kapital'] else xAboCap)*xDiaMor*(self.tas_im_anual/36525),0)
                break 
        lista_posterior = [objeto for objeto in self.lista_mov if objeto['fecha'] > self.fecha_focal and objeto['tipmov'] == '1']    
        for reg2 in lista_posterior:
            if xSalPorDis > 0:
                xAboCap = xAboCap + reg2['kapital']
                xAboIntCor = xAboIntCor + reg2['intcor']  
                xAboIntMor = xAboIntMor + reg2['intmor']
                xAboPolSeg = xAboPolSeg + reg2['polseg']
                xPolPer = xAboPolSeg if xAboPolSeg > reg2['polseg'] else reg2['polseg']
                xPolPer = xPolPer if xPolPer > 0 else 0
                xCapPer = xAboCap if xAboCap < reg2['kapital'] else reg2['kapital']
                xCapPer = xCapPer if xCapPer > 0 else 0                    
                xIntPer = xAboIntCor if xAboIntCor < reg2['intcor'] and xAboIntCor >=0 else reg2['intcor'] if  xAboIntCor >= 0 else 0
                xFacInt = ((reg2['fecha'] - self.fecha_focal).days if (reg2['fecha'] - self.fecha_focal).days > 0 else 0)*self.tas_ic_dia
                xConIntAnt = round(xCapPer * self.tas_ic_dia,0) * (reg2['fecha'] - self.fecha_focal).days if (reg2['fecha'] - self.fecha_focal).days > 0 else 0
                xTotPer = xCapPer + xIntPer + xPolPer - xConIntAnt
                if xTotPer <= xSalPorDis and xTotPer >= 0:
                    oAboPolSeg = oAboPolSeg + xPolPer    
                    oAboCap = oAboCap + xCapPer
                    oConIntAnt = oConIntAnt + xConIntAnt
                    oAboIntCor = oAboIntCor + xTotPer-xCapPer-xPolPer
                    xSalPorDis = xSalPorDis - xTotPer
                else:
                    if xSalPorDis > xPolPer:
                        oAboPolSeg = oAboPolSeg + xPolPer
                        xSalPorDis = xSalPorDis - xPolPer
                    else:
                        oAboGasPol = oAboGasPol + xSalPorDis
                        xSalPorDis = 0 
                    xFacInt = round(xFacInt,4)
                    if xSalPorDis > xIntPer:
                        xCap = int((xSalPorDis - xIntPer*(1-xTasDesIntPer/xTasIntPer))/(1-xFacInt*(1-xTasDesIntPer/xTasIntPer)))
                        xConIntAnt = int(xCap*xFacInt)
                        oConIntAnt = oConIntAnt + xConIntAnt
                        oAboIntCor = oAboIntCor + xIntPer - xConIntAnt
                        oAboCap = oAboCap + xSalPorDis - xIntPer + xConIntAnt
                    else:
                        xFraInt=int(xSalPorDis*xTasDesIntPer/xTasIntPer)
                        oAboIntCor = oAboIntCor + xSalPorDis + xFraInt
                    xSalPorDis = 0
                if oAboIntCor+xSalPorDis<=0:
                    break
            else:
                break
        if oAboIntCor + oConIntAnt < 0:
            if oAboIntCor < 0:
                oAboIntCor = oAboIntCor - oAboIntCor
        self.int_mor_cau =  oCauIntMor
        self.capital_a_pag = oAboCap
        self.int_cor_a_pag = oAboIntCor
        self.pol_seg_a_pag = oAboPolSeg
        self.int_mor_a_pag = oAboIntMor
        self.acreedor_a_pag = 0
        self.aju_ic_a_pag = -oConIntAnt
    
    def distri_pago_abo(self,iValorPorDis,idet_pro = None):
        self.tip_pag = 'ABOCA'
        xValtPagAct = 0
        xFec_mod = None
        if idet_pro != None:
            reg_pag_act = justo.DETALLE_PROD.objects.filter(id = idet_pro).first()
            if reg_pag_act != None:
                xValPagAct = -reg_pag_act.valor
                reg_hecho = justo.HECHO_ECONO.objects.filter(id = reg_pag_act.hecho_econo).first()
                xfec_mod = reg_hecho.fecha
            if xValPagAct != iValorPorDis or xFec_mod != self.fecha_focal or reg_pag_act.concepto == 'ABOCU':
                return 2
            regis = [fila for fila in self.lista_mov if fila['fecha'] == self.fecha_focal and fila['tip_mov'] == '7']
            self.capital_a_pag = regis['kapital']
            self.int_cor_a_pag = regis['intcor']
            self.pol_seg_a_pag = regis['polseg']
            self.int_mor_a_pag = regis['intmor']
            self.acreedor_a_pag = regis['acreed']
            return 1
        xSaldo = self.sal_cap_tot
        xAltura = self.altura
        xCuoPag = self.cuo_pag
        xCuoTot = self.cuo_pac
        xDifCuo = xAltura - xCuoPag
        xPagoPorDis = iValorPorDis
        xFecUlPag = None
        self.liq_al_dia(self.fecha_focal)
        
        xSalCapDia = self.sal_cap_dia
        xSalIntDia = self.sal_int_dia
        xSalMora = self.int_mor_cau
        xSalPolDia = self.sal_ps_dia
        xSalCapTot = self.sal_cap_tot
        xIntCauFra = self.int_cau_fra
        xIntAjuPagAnt = self.int_aju_pa
        xIntPagTot = self.int_pag_tot
        xPagCuoPolAde = 0
        xSalPolDia = xSalPolDia + xPagCuoPolAde
        xIntDia = xSalIntDia if xSalIntDia > 0 else -xIntPagTot if xSalIntDia + xIntPagTot < 0 else xSalIntDia
        xAjuIntAnt = xSalIntDia - xIntDia if xIntDia < 0 else 0
        xIntDia = xIntDia + xIntAjuPagAnt
        xSalMora = xSalMora if self.for_pag == 'P' else 0
        if xPagoPorDis < xSalCapDia+xIntDia + xSalMora + xSalPolDia + xIntCauFra :
            return 3
        xAcre = 0
        xAboCap = xPagoPorDis - (xIntDia + xSalMora +xSalPolDia+xIntCauFra)
        if xAboCap > xSalCapTot:
            xAcre = xAboCap - xSalCapTot
            xAboCap = xSalCapTot
        self.capital_a_pag = -xAboCap
        self.int_cor_a_pag = -xIntDia - xIntCauFra
        self.pol_seg = -xSalPolDia
        self.int_mor_a_pag = -xSalMora
        self.acreedor_a_pag = -xAcre
        return 0
        
    def distri_pago_condona(self,iValPorDis):
        self.tip_pag = 'CONDO'

        return
    
    def distri_pago_castigo(self,iValPorDis):
        self.tip_pag = 'KASTI'
        return
    
    def aplicar_pago(self,iValPorDis):
        Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
        CenCos = justo.CENTROCOSTOS.objects.filter(cliente = Cliente,codigo='A001').first()
        Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
        Credito = justo.CREDITOS.objects.filter(oficina=Oficina,cod_cre = self.cod_cre).first()
        ImpConCre = justo.IMP_CON_CRE.objects.filter(id=Credito.imputacion_id).first()
        Socio = justo.ASOCIADOS.objects.filter(id = Credito.socio_id).first()
        Ter = justo.TERCEROS.objects.filter(id = Socio.tercero_id).first()
        if ImpConCre == None:
            print('No Existe Imp Contable')
            return
        xValPag = -(self.capital_a_pag + self.int_cor_a_pag + self.pol_seg_a_pag + self.int_mor_a_pag + self.acreedor_a_pag)
        if xValPag == 0 or xValPag != iValPorDis:
            return
        DocCon = justo.DOCTO_CONTA.objects.filter(oficina=Oficina,per_con = self.fecha_focal.year,codigo=1).first()
        HecEco = justo.HECHO_ECONO.objects.filter(docto_conta=DocCon,numero = 1).first()
        if HecEco == None:
            HecEco = justo.HECHO_ECONO.objects.create(docto_conta=DocCon,numero = None,fecha=self.fecha_focal,descripcion='Aboca Prueba')
        DetPro = justo.DETALLE_PROD.objects.filter(hecho_econo = HecEco,oficina = Oficina,centro_costo = CenCos,producto='CR',concepto = self.tip_pag,subcuenta=self.cod_cre).first()
        if DetPro == None:
            DetPro = justo.DETALLE_PROD.objects.create(hecho_econo = HecEco,oficina = Oficina,centro_costo = CenCos,producto='CR',concepto = self.tip_pag,subcuenta=self.cod_cre,valor = -xValPag)
        if self.capital_a_pag != 0:
            PlaCta = justo.PLAN_CTAS.objects.filter(cliente = Cliente,per_con = DocCon.per_con,cod_cta = ImpConCre.kpte_cap).first()
            DetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,detalle_prod = DetPro,cuenta = PlaCta,tercero = Ter).first()
            if DetEco == None:
                DetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,detalle_prod = DetPro,cuenta = PlaCta,tercero = Ter)
            if self.capital_a_pag < 0:
                DetEco.credito = -self.capital_a_pag
                DetEco.debito = 0
                DetEco.valor_1 = 0
                DetEco.valor_2 = -self.capital_a_pag
            else:
                DetEco.credito = -self.capital_a_pag
                DetEco.debito = 0
                DetEco.valor_1 = 0
                DetEco.valor_2 = -self.capital_a_pag
            DetEco.item_concepto = 'kapita'
            DetEco.detalle = self.tip_pag,'  Capital = '+self.cod_cre    
            DetEco.save()
        if self.int_cor_a_pag != 0:
            PlaCta = justo.PLAN_CTAS.objects.filter(cliente = Cliente,per_con = DocCon.per_con,cod_cta = ImpConCre.kpte_ic).first()
            DetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,detalle_prod = DetPro,cuenta = PlaCta,tercero = Ter).first()
            if DetEco == None:
                DetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,detalle_prod = DetPro,cuenta = PlaCta,tercero = Ter)
            if self.int_cor_a_pag < 0:
                if self.capital_a_pag < 0:
                    DetEco.credito = -self.int_cor_a_pag
                    DetEco.debito = 0
                    DetEco.valor_1 = 0
                    DetEco.valor_2 = -self.int_cor_a_pag
                else:
                    DetEco.credito = -self.int_cor_a_pag
                    DetEco.debito = 0
                    DetEco.valor_1 = 0
                    DetEco.valor_2 = -self.int_cor_a_pag
                DetEco.detalle = self.tip_pag,'  Int Cor = '+self.cod_cre
                DetEco.item_concepto = 'IntCor'
                DetEco.save()
        if self.int_mor_a_pag != 0:
            PlaCta = justo.PLAN_CTAS.objects.filter(cliente = Cliente,per_con = DocCon.per_con,cod_cta = '41504001').first()
            DetEco = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,detalle_prod = DetPro,cuenta = PlaCta,tercero = Ter).first()
            if DetEco == None:
                DetEco = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,detalle_prod = DetPro,cuenta = PlaCta,tercero = Ter)
            if self.int_mor_a_pag < 0:
                if self.int_mor_a_pag < 0:
                    DetEco.credito = -self.int_mor_a_pag
                    DetEco.debito = 0
                    DetEco.valor_1 = 0
                    DetEco.valor_2 = -self.int_mor_a_pag
                else:
                    DetEco.credito = -self.int_mor_a_pag
                    DetEco.debito = 0
                    DetEco.valor_1 = 0
                    DetEco.valor_2 = -self.int_mor_a_pag
                DetEco.item_concepto = 'IntMor'
                DetEco.detalle = self.tip_pag,'  Int Mor = '+self.cod_cre
                DetEco.save()


        if self.int_mor_cau != 0:    #  Faltan mas Condiciones
            CamCre = justo.CAMBIOS_CRE.objects.filter(det_pro = DetPro,tip_cam = '2').first()
            if CamCre == None:
                CamCre = justo.CAMBIOS_CRE.objects.create(det_pro = DetPro,tip_cam = '2')
            CamCre.int_mor = self.int_mor_cau
            CamCre.capital = 0
            CamCre.int_cor = 0
            CamCre.pol_seg = 0
            CamCre.des_pp = 0
            CamCre.fecha = HecEco.fecha
            CamCre.acreedor = 0
            CamCre.save()
        
        params = [0.0,0,0,0.0,0.0,0,0.0,' ',date(1900,1,1),0]
        self.lista_mov = cargue_mov_cre(self.cod_cre,params)
        lista_causa = [objeto for objeto in self.lista_mov if objeto['tipmov'] == '1']    
        for reg in lista_causa:   #  Guarda Causacion por si se elimina el movimiento se puede restaurar 
            RegResCau = justo.CREDITOS_CAUSA.objects.create(cod_cre = self.cod_cre,cuota = reg['cuota'],fecha=reg['fecha'],
                capital = reg['kapital'],int_cor = reg['intcor'],oficina = Oficina,comprobante = DetPro)
        xTotCap = xTotIC = 0
        xSalCap = self.cap_ini
        lista_al_dia = [objeto for objeto in self.lista_mov if objeto['fecha'] <= self.fecha_focal]
        for reg in lista_al_dia:
            if reg['tipmov'] != 'A':
                print(reg['tipmov'],'',reg['kapital'],' ',reg['intcor'])
                xTotCap = xTotCap + reg['kapital']
                xTotIC = xTotIC + reg['intcor']
                xSalCap = xSalCap + (reg['kapital'] if reg['kapital'] < 0 else 0)

        #[objeto for objeto in self.lista_mov if objeto['fecha'] >= self.fecha_focal and objeto['tipmov'] == '1']
        lista_final = justo.CREDITOS_CAUSA.objects.filter(Q(comprobante_id=None) & Q(cod_cre=self.cod_cre) &
            Q(oficina=Oficina) & Q(fecha__gte=self.fecha_focal)).order_by('cuota')
        xFecAnt = self.fecha_focal
        xPrimero = True
        xIntIni = 0
        for reg in lista_final:     #  se re aplican causaciones futuras
            if xSalCap > 0:
                xIntMes = round(xSalCap * self.tas_ic_dia,0) * (reg.fecha - xFecAnt).days 
                if xPrimero and self.tip_pag == 'ABOCU':
                    xCapMes = 0
                    xIntIni = xIntMes
                    xPrimero = False
                else:
                    xCapMes = self.val_cuo - xIntMes - xIntIni
                    xIntIni = 0
                xCapMes = xCapMes if xSalCap - xCapMes > 0 else xSalCap 
                reg.capital = xCapMes - xTotCap
                reg.int_cor = xIntMes - xTotIC
                xSalCap = xSalCap - xCapMes
                xTotCap = 0
                xTotIC = 0
            else:
                reg.capital = 0
                reg.int_cor = 0
            xFecAnt = reg.fecha
            reg.save()
            
    def eliminar_pago(self,iDetPro):
        Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
        DetPro = justo.DETALLE_PROD.objects.filter(id = iDetPro).first()
        if DetPro == None:
            return
        if DetPro.concepto == 'ABOCA' or DetPro.concepto == 'ABOCU' or DetPro.concepto == 'CASTI':
            CauCres = justo.CREDITOS_CAUSA.objects.filter(comprobante_id = DetPro,cod_cre=self.cod_cre,oficina=Oficina)
            if CauCres == None:
                return
            CauCreRets = justo.CREDITOS_CAUSA.objects.filter(comprobante_id = None,cod_cre=self.cod_cre,oficina=Oficina)
            for CauCreRet in CauCreRets:
                CauCreRet.delete()
            CauCres = justo.CREDITOS_CAUSA.objects.filter(comprobante_id = DetPro,cod_cre=self.cod_cre,oficina=Oficina)
            for CauCre in CauCres:
                CauCre.comprobante_id = None
                CauCre.save()
        HecEco = justo.HECHO_ECONO.objects.filter(id = DetPro.hecho_econo_id).first()   
        DetEcos = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,detalle_prod = DetPro)
        for DetEco in DetEcos:
            DetEco.delete()
        DetPro.delete()
        CreCau = justo.CAMBIOS_CRE.objects.filter(det_pro_id = iDetPro)
        if CreCau != None:
            CreCau.delete()
        return

    def Exportar_mov(self):
        ruta_excel = "c:/aaa/c"+self.cod_cre+".xlsx"
        df = pd.DataFrame(self.lista_mov)
        writer = pd.ExcelWriter(ruta_excel, engine='xlsxwriter')
        df.to_excel(writer, index=False)
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']  # Ajusta el nombre de la hoja según tu caso
        workbook.close()
        #for reg in tab_liq :
        #    print(reg['cuota'],'  ',reg['fecha'],'  ',reg['tipmov'],'  ',reg['kapital'],'  ',reg['intcor'],'  ',reg['intmor'])

class Sal_cre:
    def __init__(self, cod_cre,estado,sal_cap_tot,cap_dia,int_dia,sal_mor,dia_mor):
        self.cod_cre = cod_cre
        self.estado = estado
        self.sal_cap_tot = sal_cap_tot
        self.cap_dia = cap_dia
        self.int_dia = int_dia
        self.sal_mor = sal_mor
        self.dia_mor = dia_mor
  
def imprime_liq(liq_cre):
    print('Credito Nro.     ',liq_cre.cod_cre)
    print('kapital Inicial  ',liq_cre.cap_ini)
    print('Fecha Desembolso ',liq_cre.fec_des)
    print('Forma de Pago    ',liq_cre.for_pag)
    print('Tasa Efec. Anual ',liq_cre.tas_ic_ea)
    print('Tasa Int Cor Dia ',liq_cre.tas_ic_dia)
    print('Tasa Int Mor Anu ',liq_cre.tas_im_anual)
    print('Por Descto PP    ',liq_cre.por_des_pp)
    print('Per Ano          ',liq_cre.per_ano)
    print('Tip Pag          ',liq_cre.tip_pag)
    print('Saldo Cap Tot    ',liq_cre.sal_cap_tot)
    print('Saldo Cap Dia    ',liq_cre.sal_cap_dia)
    print('Saldo int Dia    ',liq_cre.sal_int_dia)
    print('Saldo pol seg    ',liq_cre.sal_ps_dia)
    print('Int Mor No Pagado',liq_cre.sal_int_mor+liq_cre.int_mor_cau)
    print('Dias Mora        ',(liq_cre.fecha_focal-liq_cre.fec_al_dia).days)
    print('Int Aju pa       ',liq_cre.int_aju_pa)
    print('Int Aju Ac       ',liq_cre.int_aju_ac)
    print('Int Pag Tot      ',liq_cre.int_pag_tot)
    print('Altura           ',liq_cre.altura)
    print('Cuotas Pagadas   ',liq_cre.cuo_pag)
    print('Cuotas Pactadas  ',liq_cre.cuo_pac)
    print('Ult Fecha Al Dia ',liq_cre.fec_al_dia)
    print('Fecha Vencimient ',liq_cre.fec_ven)
    print('------ Datos par Aplicar Pagos -------')
    print('(capital_a_pag)  capital a Pagar  ',liq_cre.capital_a_pag)
    print('(int_cor_a_pag)  Int Cor a Pagar  ',liq_cre.int_cor_a_pag)
    print('(pol_seg_a_pag)  Pol Seg a Pagar  ',liq_cre.pol_seg_a_pag)
    print('(int_mor_a_pag)  Int Mor a Pagar  ',liq_cre.int_mor_a_pag)
    print('(acreedor_a_pag) Sobra en el Pago ',liq_cre.acreedor_a_pag)
    print('(aju_cap_a_pag)  aju cap en pago  ',liq_cre.aju_cap_a_pag)
    print('(aju_ic_a_pag)   aju ic en pago   ',liq_cre.aju_ic_a_pag)
    print('(aju_ps_a_pag)   aju PS en pago   ',liq_cre.aju_ps_a_pag)
    print('(int_mor_cau)    Int Mor Cau Pago ',liq_cre.int_mor_cau) 
    print('(aju_im_a_pag)   aju IM a Pagar   ',liq_cre.aju_im_a_pag)
    print('(int_cau_fra)    Int Cau Fra      ',liq_cre.int_cau_fra)
    print('---------------------------------------')
    print('max Valor Cuota  ',liq_cre.max_pag_couta)
    print('min valor aboca  ',liq_cre.min_pag_aboca)
    print('min valor abocu  ',liq_cre.min_pag_abocu)
    print('sig fecha pago1  ',liq_cre.fec_sig_pag1)
    print('sig fecha pago2  ',liq_cre.fec_sig_pag2)
    return

class AsiConRow:
    def __init__(self,CodCta,Nit,Tipo,Detalle, Debito, Credito):
        self.CodCta = CodCta
        self.Nit = Nit
        self.Tipo = Tipo
        self.Detalle = Detalle
        self.Debito = Debito
        self.Credito = Credito
        
class AsiCon:
    def __init__(self):
        self.rows = []
        self.indexed_rows = {}

    def actualizar(self,CodCta,Nit,Tipo,Detalle, Debito, Credito):
        # Crear una clave para buscar en el índice
        clave_busqueda = (CodCta,Nit,Tipo)
        reg_existe = self.indexed_rows.get(clave_busqueda)
        if reg_existe:
            reg_existe.Detalle = reg_existe.Detalle + ('' if Detalle in reg_existe.Detalle else ';'+Detalle)  
            reg_existe.Debito = reg_existe.Debito + Debito
            reg_existe.Credito = reg_existe.Credito + Credito
        else:
            # Crear un nuevo registro si no existe
            nuevo_registro = AsiConRow(CodCta,Nit,Tipo,Detalle, Debito, Credito)
            self.rows.append(nuevo_registro)
            self.indexed_rows[clave_busqueda] = nuevo_registro

    def eliminar_iguales(self):
        # Filtrar los registros donde Debito es igual a Credito
        self.rows = [registro for registro in self.rows if registro.Debito != registro.Credito]
    
    def convertir_a_dataframe(self):
        data = {
            'CodCta': [],
            'Nit': [],
            'Tipo': [],
            'Detalle': [],
            'Debito': [],
            'Credito': []
        }

        for row in self.rows:
            data['CodCta'].append(row.CodCta)
            data['Nit'].append(row.Nit)
            data['Tipo'].append(row.Tipo)
            data['Detalle'].append(row.Detalle)
            data['Debito'].append(row.Debito)
            data['Credito'].append(row.Credito)

        df = pd.DataFrame(data)

        return df

    def guardar_en_excel(self, nombre_archivo, ubicacion):
        df = self.convertir_a_dataframe()
        ruta_completa = os.path.join(ubicacion, nombre_archivo)
        df.to_excel(ruta_completa, index=False, engine='openpyxl')
        return ruta_completa  # Devolver la ruta completa del archivo guardado

class CateHistRow:
    def __init__(self,CodCre,FechaRef,Categoria,Valor):
        self.CodCre = CodCre
        self.Categoria = Categoria
        self.FechaRef = FechaRef
        self.Valor = Valor
        
class CateHist:
    def __init__(self):
        self.rows = []
        self.indexed_rows = {}

    def actualizar(self,CodCre,FechaRef,Categoria,Valor):
        # Crear una clave para buscar en el índice
        clave_busqueda = (CodCre,FechaRef)
        registro_existente = self.indexed_rows.get(clave_busqueda)
        if registro_existente:
            registro_existente.CodCre = CodCre
            registro_existente.FechaRef = FechaRef
            registro_existente.Categoria = Categoria
            registro_existente.valor = Valor
        else:
            # Crear un nuevo registro si no existe
            nuevo_registro = CateHistRow(CodCre,FechaRef,Categoria,Valor)
            self.rows.append(nuevo_registro)
            self.indexed_rows[clave_busqueda] = nuevo_registro

class Reclasificacion:
    fecha_ant_rec = None
    fecha_rec = None
    AsiConCap = AsiCon()
    AsiRecInt = AsiCon()
    def __init__(self,ifecha,Oficina):
        self.fecha_rec = ifecha
        self.fecha_ant_rec = ifecha.replace(day=1) - timedelta(days=1)
        return
    
    def Creacion_tablas(self,ifecha,Oficina):
        Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
        justo.CATE_INTE.objects.filter(oficina=Oficina, fecha=self.fecha_rec).delete()      #  Elimina la Reclasificacion del mes para volver a empezar 
    #   Colocar Castigo en la causacion anterior si durante el periodo se presento un castigo o una condonacion
        CreMovKC = justo.CAMBIOS_CRE.objects.filter(tip_cam ='4',fecha__gt=self.fecha_ant_rec, fecha__lte=self.fecha_rec,
            det_pro__hecho_econo__docto_conta__oficina=Oficina)
        if CreMovKC != None:
            for reg in CreMovKC:
                DetPro = justo.DETALLE_PROD.objects.filter(id = reg.det_pro_id).first()
                CreHis = justo.CARTE_CAT_HIS.objects.filter(oficina=Oficina,fecha = self.fecha_ant_rec,cod_cre = DetPro.subcuenta).first()
                xCreCas = ' '
                if reg.capital != 0 and reg.int_cor  != 0:
                    xCreCas = 'T'
                elif reg.int_cor != 0:
                    xCreCas = 'K'
                CreHis.castigo = xCreCas
                CreHis.save()
        justo.CARTE_CAT_HIS.objects.filter(oficina=Oficina,fecha=self.fecha_rec).delete()   #  se marcan los registros para luego borrarlos si no se reinicio
        Creditos = justo.CREDITOS.objects.filter(oficina=Oficina).exclude(estado='H')    #  se recorren todos los creditos
        nr = 0
        for Credito in Creditos:
            nr = nr + 1
            liq_cre = Liquida_cre(Credito.cod_cre,self.fecha_rec)
            if liq_cre.lista_mov == None:
                Credito.estado = 'H'
                Credito.save()
                continue 
            liq_cre.liq_al_dia(self.fecha_rec)
            if liq_cre.sal_cap_tot <= 0 :
                if not (Credito.fec_des.year == ifecha.year and Credito.fec_des.month == ifecha.month):
                    CarCatAnt = justo.CARTE_CAT_HIS.objects.filter(oficina=Oficina,fecha=self.fecha_ant_rec,cod_cre = Credito.cod_cre).first()
                    if CarCatAnt == None:
                        continue
                    if CarCatAnt.sal_cap <= 0:
                        continue 
            liq_cre.calculo_periodo()
            xdias_mor = (liq_cre.fecha_focal-liq_cre.fec_al_dia).days
            xdias_mor = xdias_mor if liq_cre.sal_cap_tot > 0 else 0
            if xdias_mor < 1:
                xCat = 'A'
            else:
                CatDesDia = justo.CAT_DES_DIA_CRE.objects.filter(cliente=Oficina.cliente_id,codigo=Credito.cod_lin_cre,
                    minimo_dias__lte=xdias_mor,maximo_dias__gte=xdias_mor).first()
                if CatDesDia == None:
                    xCat = 'F'
                else:
                    xCat = CatDesDia.categoria
        #   Se crea o se modifica LA FOTO DE LA FECHA
            xCat = xCat if not (Credito.fec_des.year == ifecha.year and Credito.fec_des.month == ifecha.month) else 'A'
            CarCatHis = justo.CARTE_CAT_HIS.objects.filter(oficina=Oficina,fecha=self.fecha_rec,cod_cre = Credito.cod_cre).first()
            if CarCatHis == None:
                CarCatHis = justo.CARTE_CAT_HIS.objects.create(oficina=Oficina,fecha=self.fecha_rec,cod_cre = Credito.cod_cre)
            CarCatHis.nit = Credito.socio.tercero.doc_ide
            CarCatHis.for_pag = Credito.for_pag
            CarCatHis.cod_lin_cre = Credito.cod_lin_cre
            CarCatHis.plazo = Credito.num_cuo_act
            CarCatHis.dias_mor = xdias_mor
            CarCatHis.cap_ini = Credito.cap_ini
            CarCatHis.cod_imp_con = Credito.imputacion.cod_imp
            CarCatHis.sal_cap = liq_cre.sal_cap_tot
            CarCatHis.categoria = xCat
            CarCatHis.sal_cap_dia = liq_cre.sal_cap_dia
            CarCatHis.sal_int_dia = liq_cre.sal_int_dia
            CarCatHis.int_cau_res_per = (liq_cre.int_cau_fra+liq_cre.aju_ic_a_pag) if liq_cre.sal_cap_tot > 0 else 0
            CarCatHis.vr_gar_hip = Credito.val_gar_hip
            CarCatHis.conta_per = (liq_cre.cuo_pac - liq_cre.altura) if liq_cre.cuo_pac - liq_cre.altura else 36
            CarCatHis.int_pag_per = liq_cre.int_pag_per
            CarCatHis.int_conkas_per = liq_cre.int_condo
            CarCatHis.save()

        #   se calcula arastre,  proporcion de aportes , garantia Hipotearia y provision de capital
        CatPorNit = justo.CARTE_CAT_HIS.objects.filter(oficina=Oficina,fecha=ifecha).values('nit').annotate(
            sum_cap_ini=Sum('cap_ini'),sum_vr_gar_hip=Sum('vr_gar_hip'),max_categoria=Max('categoria'))
        for row in CatPorNit:      
            nit = row['nit']
            sum_cap_ini = row['sum_cap_ini']
            sum_vr_gar_hip = row['sum_vr_gar_hip']
            max_categoria = row['max_categoria']
            xAporte = 0
            Aportes = justo.DETALLE_PROD.objects.filter(oficina = Oficina,producto='AP',hecho_econo__fecha__lte=ifecha,
                subcuenta=nit).aggregate(total_apor=Sum('valor'))
            if Aportes['total_apor'] == None:
                xAporte = 0 
            else:
                xAporte = -Aportes['total_apor']
            CatPorNits = justo.CARTE_CAT_HIS.objects.filter(oficina=Oficina,fecha=ifecha,nit = row['nit'])
            xSaldo_1 = xSaldo_2 = 0
            for CatPorNit in CatPorNits:
                if max_categoria == 'A':
                    xSaldo_1 = xSaldo_1 + CatPorNit.sal_cap
                else:
                    xSaldo_2 = xSaldo_2 + CatPorNit.sal_cap
                xFactor = CatPorNit.cap_ini /sum_cap_ini
                CatPorNit.aporte = xAporte
                CatPorNit.arrastre = max_categoria
                CatPorNit.vr_gar_hip = round(sum_vr_gar_hip*xFactor,0)
                CatPorNit.save()
            for CatPorNit in CatPorNits:
                CatPorNit.saldo_1 = xSaldo_1
                CatPorNit.saldo_2 = xSaldo_2
                CatPorNit.save()
        CarCatPers = justo.CARTE_CAT_HIS.objects.filter(oficina=Oficina,fecha=ifecha)
        for CarCatPer in CarCatPers:
            if CarCatPer.arrastre != 'A':
                PorProInd = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = CarCatPer.cod_imp_con,categoria = CarCatPer.arrastre).first()
                if PorProInd == None:
                    xTasPro = 100
                else:
                    xTasPro = PorProInd.porcen_det
                CarCatPer.aporte = round(CarCatPer.aporte/CarCatPer.saldo_2*CarCatPer.sal_cap if CarCatPer.saldo_2 > 0 else 0,0)
                if CarCatPer.dias_mor <= 547:
                    xPorGarHip = 0.7
                elif CarCatPer.dias_mor <= 730:
                    xPorGarHip = 0.5
                elif CarCatPer.dias_mor <= 910:
                    xPorGarHip = 0.3
                elif CarCatPer.dias_mor <= 1905:
                    xPorGarHip = 0.15
                else:
                    xPorGarHip = 0.15 
                if CarCatPer.dias_mor >0 and CarCatPer.plazo == 1:
                    xPorGarApo = 0
                xProvision = round((CarCatPer.sal_cap - (CarCatPer.vr_gar_hip*xPorGarHip))*xTasPro/100,0) 
                CarCatPer.pro_ind = xProvision if xProvision > 0 else 0
                CarCatPer.vr_gar_hip = round(CarCatPer.vr_gar_hip*xPorGarHip,0)
            else:
                if CarCatPer.saldo_2 == 0 and CarCatPer.saldo_1>0:
                    CarCatPer.aporte = round(CarCatPer.aporte/CarCatPer.saldo_1*CarCatPer.sal_cap,0)
                    CarCatPer.pro_ind = 0
                else:
                    CarCatPer.aporte = 0
                    CarCatPer.pro_ind = 0
            CarCatPer.save()
#   Aqui se crea lA RECLASIFICACION UNIDA INICIANDO EN LA DEL Periodo Anterior 
        CatInis = justo.CARTE_CAT_HIS.objects.filter(oficina = Oficina,fecha = self.fecha_ant_rec)
        for CatIni in CatInis:
            if CatIni.castigo == 'T':
                continue
            CateInt = justo.CATE_INTE.objects.filter(oficina=Oficina,fecha = self.fecha_rec,cod_cre = CatIni.cod_cre).first()
            if CateInt == None:
                CateInt = justo.CATE_INTE.objects.create(oficina=Oficina,fecha = self.fecha_rec,cod_cre = CatIni.cod_cre)
            CateInt.tipo = '1'
            CateInt.nit = CatIni.nit
            CateInt.int_dia_ini = CatIni.sal_int_dia
            CateInt.arr_ini = CatIni.arrastre
            CateInt.int_cau_ini = CatIni.int_cau_res_per
            CateInt.sal_cap_ini = CatIni.sal_cap
            CateInt.cat_ini = CatIni.categoria
            CateInt.cre_con_cas = 'N' if CatIni.castigo == ' ' else 'F'
            CateInt.pro_ind_ini = CatIni.pro_ind
            CateInt.gas_pro_ind_ini = CatIni.gas_pro_ind
            CateInt.gas_gen_ini = CatIni.gas_pro_gen
            CateInt.det_ind_gas_acu = CatIni.det_ind_gas_acu
            CateInt.save()
#   continua cLA UNION con el periodo actual
        CatFins = justo.CARTE_CAT_HIS.objects.filter(oficina = Oficina,fecha = self.fecha_rec)
        for CatFin in CatFins:
            CateInt = justo.CATE_INTE.objects.filter(oficina=Oficina,fecha = self.fecha_rec,cod_cre = CatFin.cod_cre).first()
            if CateInt == None:
                CateInt = justo.CATE_INTE.objects.create(oficina=Oficina,fecha = self.fecha_rec,cod_cre = CatFin.cod_cre)
                CateInt.tipo = '0' if CatFin.sal_cap <= 0 else '1'  # 0 Si el credito no existia en el periodo NTERIOS
            else:
                CateInt.tipo = '3' if CatFin.sal_cap > 0 else '2'   # 2 Si termino en este periodo 3 si esta en ambos periodos
            CateInt.nit = CatFin.nit
            CateInt.int_dia_fin = CatFin.sal_int_dia if CatFin.sal_cap > 0 else 0
            CateInt.arr_fin = CatFin.arrastre
            CateInt.int_cau_fin = CatFin.int_cau_res_per
            CateInt.sal_cap_fin = CatFin.sal_cap
            CateInt.cat_fin = CatFin.categoria
            CateInt.pro_ind_fin = CatFin.pro_ind
            CateInt.gas_pro_ind_fin = CatFin.gas_pro_ind
            CateInt.gas_gen_fin = CatFin.gas_pro_gen
            CateInt.int_pag = CatFin.int_pag_per
            CateInt.int_con = CatFin.int_conkas_per
            CateInt.save()
#   Ahora se carga cod_imp y fec des a partir de los creditos
        CateInts = justo.CATE_INTE.objects.filter(oficina=Oficina,fecha = self.fecha_rec)
        for CateInt in CateInts:
            Cred = justo.CREDITOS.objects.filter(oficina=Oficina,cod_cre = CateInt.cod_cre).first()
            CateInt.fec_des = Cred.fec_des
            CateInt.cod_imp = Cred.imputacion.cod_imp
            CateInt.save()
        return

    def ReclaProv_capital(self,Oficina):
        print('   Provision Capital        ',datetime.now())
        Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
#  aqui se recorre la cat del periodo para calcular reclasificacion del Capital 
        xNitEmpresa = Cliente.doc_ide
        CreRecs = justo.CATE_INTE.objects.filter(oficina=Oficina,fecha = self.fecha_rec)
        for CreRec in CreRecs:
            if CreRec.tipo == '0':    #   si el desembolso y el pago total ocurrieron en el mismo periodo no afecta nada
                continue
            xCodImp = CreRec.cod_imp
            xArrIni = CreRec.arr_ini if CreRec.arr_ini > ' ' and CreRec.arr_ini < 'F' else ('E' if CreRec.arr_ini == 'F' else 'A')
            xArrFin = CreRec.arr_fin if CreRec.arr_fin > ' ' and CreRec.arr_fin < 'F' else ('E' if CreRec.arr_fin == 'F' else 'A')
            if CreRec.sal_cap_ini == CreRec.sal_cap_fin and xArrIni == xArrFin :  # sin cambios no son necesarios los ASIENTOS
                continue
            ImpCon = justo.IMP_CON_CRE.objects.filter(cliente = Cliente,cod_imp = xCodImp).first()        
#  Se hacen los asientos para que el saldo de la cuenta puente vuelva a cero
            if CreRec.sal_cap_ini < CreRec.sal_cap_fin:     #  Se Desembolso en ese mes
                self.AsiConCap.actualizar(ImpCon.kpte_cap,xNitEmpresa,'CapPte','',0,CreRec.sal_cap_fin - CreRec.sal_cap_ini)
            else:                                           #  Se hicieron pagos 
                self.AsiConCap.actualizar(ImpCon.kpte_cap,xNitEmpresa,'CapPte','',CreRec.sal_cap_ini - CreRec.sal_cap_fin,0)
#  Deterioro general y general adicional
            xDifProGen = round(CreRec.sal_cap_ini*0.01,0) - round(CreRec.sal_cap_fin*0.01,0)
            xDifProGenAdi = round(CreRec.sal_cap_ini*0.005,0) - round(CreRec.sal_cap_fin*0.005,0)
            RegCapIni = justo.IMP_CON_CRE_INT.objects.filter(cliente=Cliente,cod_imp = xCodImp,categoria = xArrIni).first()
            RegCapFin = justo.IMP_CON_CRE_INT.objects.filter(cliente=Cliente,cod_imp = xCodImp,categoria = xArrFin).first()
            xDetIni = round(CreRec.sal_cap_ini*RegCapIni.porcen_det/100,0)
            xDetFin = round(CreRec.sal_cap_fin*RegCapFin.porcen_det/100,0)
            if CreRec.sal_cap_ini > 0:  #  Se debe asegurar que el credito no se haya desembolsado ese periodo
                if xDifProGen + xDifProGenAdi > 0:     #   se desembolsa el credito 
                    self.AsiConCap.actualizar(ImpCon.kdet_gen,CreRec.nit,CreRec.cod_cre,CreRec.cod_cre,0,xDifProGen)
                    self.AsiConCap.actualizar(ImpCon.kdet_gen_adi,CreRec.nit,CreRec.cod_cre,CreRec.cod_cre,0,xDifProGenAdi)
                    self.AsiConCap.actualizar(ImpCon.kdet_gen_gas,CreRec.nit,CreRec.cod_cre,CreRec.cod_cre,xDifProGen+xDifProGenAdi,0)
                    if CreRec.sal_cap_ini > 0:  #   Se Desembolso el credito en el periodo Anterior 
                        self.AsiConCap.actualizar(ImpCon.kdet_gen,CreRec.nit,CreRec.cod_cre,CreRec.cod_cre,xDifProGen,0) 
                        self.AsiConCap.actualizar(ImpCon.kdet_gen_adi,CreRec.nit,CreRec.cod_cre,CreRec.cod_cre,xDifProGenAdi,0)
                else:   #  Debe haber saldo inicial ya que el desembolso pudo haber ocurrido ese mes 
                    self.AsiConCap.actualizar(ImpCon.kdet_gen,CreRec.nit,'DetGen',CreRec.cod_cre,-xDifProGen,0)
                    self.AsiConCap.actualizar(ImpCon.kdet_gen_adi,CreRec.nit,'DetGen',CreRec.cod_cre,-xDifProGenAdi,0)
                    if CreRec.fec_des.year == self.fecha_rec.year:  # Puede Disminuir el Gasto por ser del mismo Año   
                        self.AsiConCap.actualizar(ImpCon.kdet_gen_gas,CreRec.nit,'DetGenGas',CreRec.cod_cre,0,xDifProGen+xDifProGenAdi)
                    else:   #  Ingreso Recuperado por ser del año siguiente a la causacion
                        self.AsiConCap.actualizar(ImpCon.kdet_gen_rec,CreRec.nit,'DetGen',CreRec.cod_cre,0,xDifProGen+xDifProGenAdi)
            else:   #  El Credito se desmbolso ese periodo 
                self.AsiConCap.actualizar(ImpCon.kdet_gen,CreRec.nit,CreRec.cod_cre,CreRec.cod_cre,0,-xDifProGen)
                self.AsiConCap.actualizar(ImpCon.kdet_gen_adi,CreRec.nit,CreRec.cod_cre,CreRec.cod_cre,0,-xDifProGenAdi)
                self.AsiConCap.actualizar(ImpCon.kdet_gen_gas,CreRec.nit,CreRec.cod_cre,CreRec.cod_cre,-(xDifProGen+xDifProGenAdi),0)
#  Se reclasifica el Capital  y se liquida  el Deteterioro individual               
            if CreRec.sal_cap_ini > 0:  #  se reversa el asientos de Capital y deterioro individual para generar el nuevo
                self.AsiConCap.actualizar(RegCapIni.kcapital,CreRec.nit,'Capita_'+xArrIni,CreRec.cod_cre,0,CreRec.sal_cap_ini)   #  Se reversa capital
                self.AsiConCap.actualizar(RegCapIni.kdet_ind,CreRec.nit,'DetInd_'+xArrIni,CreRec.cod_cre,xDetIni,0)   #  Se reversa Deterioro  Ind
            if CreRec.sal_cap_fin > 0:  #  se Generan los nuevos asientos de Reclasificacion de Cpaital y deterioro Individual
                RegCapFin = justo.IMP_CON_CRE_INT.objects.filter(cliente=Cliente,cod_imp = xCodImp,categoria = xArrFin).first()        
                self.AsiConCap.actualizar(RegCapFin.kcapital,CreRec.nit,'Capita_'+xArrFin,CreRec.cod_cre,CreRec.sal_cap_fin,0)
                self.AsiConCap.actualizar(RegCapFin.kdet_ind,CreRec.nit,'DetInd_'+xArrFin,CreRec.cod_cre,0,xDetFin)
            xDifDetInd = xDetIni - xDetFin
            xDetIndGasAcu = CreRec.det_ind_gas_acu
            if xDifDetInd < 0:   #  se incrementa el gasto 
                self.AsiConCap.actualizar(ImpCon.kdet_ind_gas,CreRec.nit,'DetIndGas',CreRec.cod_cre,xDetFin,xDetIni)
                xDetIndGasAcu = xDetIndGasAcu + xDetFin - xDetIni
            else:   #  se disminuye el gasto y hay que distribuiirlo entre ingreso recuperado y gasto al credito
                xIng_x_cau = xDetIni - xDetIndGasAcu
                if xIng_x_cau < xDifDetInd:  #   no alcanza con el ingreso recuperado pero se aplica lo que alcance
                    self.AsiConCap.actualizar(ImpCon.kdet_ind_rec,CreRec.nit,'DetIndGas',CreRec.cod_cre,0,xIng_x_cau)
                    self.AsiConCap.actualizar(ImpCon.kdet_ind_gas,CreRec.nit,'DetIndGas',CreRec.cod_cre,0,xDifDetInd-xIng_x_cau)
                    xDetIndGasAcu = xDetIndGasAcu - (xDifDetInd-xIng_x_cau)
                else:
                    self.AsiConCap.actualizar(ImpCon.kdet_ind_rec,CreRec.nit,'DetIndGas',CreRec.cod_cre,0,xDifDetInd)
            CreRec.det_ind_gas_acu = xDetIndGasAcu
            CreRec.save()
        self.AsiConCap.eliminar_iguales()  #  Se borran los iguales 
        self.AsiConCap.guardar_en_excel('ReclaCar.xlsx','C:/AAA/')
        return
 
    def ReclaProv_interes(self,Oficina):
        print('   Reclasificacion Interes  ',datetime.now())
        CurCatHis = CateHist()
        CateIntes = justo.CATE_INTE.objects.filter(oficina=Oficina,fecha=self.fecha_rec)
        for CateInte in CateIntes:
            CateInte.cat_ini = 'A' if CateInte.cat_ini == ' ' else CateInte.cat_ini
            CateInte.cat_fin = 'A' if CateInte.cat_fin == ' ' else CateInte.cat_fin
            CateInte.int_cau_mes = CateInte.int_dia_fin + CateInte.int_cau_fin + CateInte.int_pag - CateInte.int_dia_ini - CateInte.int_cau_ini
            CateInte.cue_pr_cob_A = CateInte.cue_pr_cob_A = CateInte.cue_pr_cob_C = CateInte.cue_pr_cob_D = CateInte.cue_pr_cob_E = CateInte.cue_pr_cob_F = 0
            CateInte.ingreso = CateInte.cue_por_pag = CateInte.cau_ZET = 0
            CateInte.int_cau_mes = CateInte.int_dia_fin + CateInte.int_cau_fin + CateInte.int_pag - CateInte.int_dia_ini -  CateInte.int_cau_ini    
            xIni = CateInte.int_cau_ini + CateInte.int_dia_ini
            xFin = CateInte.int_cau_fin + CateInte.int_dia_fin
            xIpAnt = 0
            xIpAct = 0
            xIpAde = 0
            xPag = CateInte.int_pag
            if xPag > 0 :
                if xIni > xPag:
                    xIpAnt = xPag
                    xPag = 0
                else:
                    if xIni > 0:
                        xIpAnt = xIni
                        xPag = xPag - xIpAnt
                    else:
                        if xFin <= 0:
                            if CateInte.int_cau_mes + xIni > 0:
                                if xPag >= CateInte.int_cau_mes + xIni :
                                    xIpAct = CateInte.int_cau_mes + xIni
                                    xIpAde = xPag - xIpAct
                                else:
                                    xIpAct = xPag 
                            else:
                                xIpAde = xPag 
                        xPag = 0
                if xPag > 0:
                    if CateInte.int_cau_mes > xPag:
                        xIpAct = xIpAct + xPag
                        xPag = 0
                    else:
                        xIpAct = xIpAct + CateInte.int_cau_mes
                        xPag = xPag - CateInte.int_cau_mes
                if xFin >= 0 :
                    if xFin > xPag:
                        xIpAct = xIpAct + xPag
                        xPag = 0
                    else:
                        if CateInte.sal_cap_fin == 0:
                            xIpAct = xIpAct + xPag
                            xPag = 0
                        else: 
                            xIpAct = xIpAct + xFin
                            xPag = xPag - xFin 
                if xPag > 0:
                    xIpAde = xPag
                    xPag = 0
            CateInte.int_pag_ant = xIpAnt
            CateInte.int_pag_act = xIpAct
            CateInte.int_pag_ade = xIpAde
            CateInte.inicio = xIni
            CateInte.final = xFin
            CateInte.ip_ant_A = 0
            CateInte.ip_ant_B = 0
            CateInte.ip_ant_C = 0
            CateInte.ip_ant_D = 0
            CateInte.ip_ant_E = 0
            CateInte.ip_ant_Z = 0
            CateInte.ip_ant_ZC = 0
            CateInte.ip_ant_ZD = 0
            CateInte.ip_ant_ZE = 0
            CateInte.ip_ant_ZF = 0
            CateInte.save()
            CreCatHiss = justo.CARTERA_CXC.objects.filter(oficina=Oficina,fecha = self.fecha_ant_rec,cod_cre=CateInte.cod_cre)
            for Reg in CreCatHiss:
                CurCatHis.actualizar(Reg.cod_cre,Reg.fec_ref,Reg.categoria,Reg.valor)
            RegCat = justo.CARTE_CAT_HIS.objects.filter(oficina=Oficina,cod_cre=CateInte.cod_cre,fecha=self.fecha_ant_rec).first()
            if RegCat != None:
                if RegCat.sal_cat_int != 0:
                    CurCatHis.actualizar(RegCat.cod_cre,self.fecha_ant_rec,RegCat.cat_int_mes,RegCat.sal_cat_int)
#   La rutina Importante        
        print('     Comienza el ciclo ',datetime.now())
        justo.CARTERA_CXC.objects.filter(oficina=Oficina,fecha = self.fecha_rec).delete()
        xtc = 0
        CateIntes = justo.CATE_INTE.objects.filter(oficina=Oficina,fecha=self.fecha_rec)
        for Reg in CateIntes:
            xCodCre = Reg.cod_cre
            xFin = Reg.final
            xIni = Reg.inicio
            xNit = Reg.nit
            xTipo = 0
            zDebito = 0
            zCredito = 0
            xCatFin = Reg.cat_fin if Reg.cat_fin < 'F' else 'E'
            xtx = xtc + 1
            if xIni >= 0 and xFin >=0 and xIni < xFin:      #  comienza debiendo termina debiendo (+)
                xTipo=1
            elif xIni >= 0 and xFin >= 0 and xIni >= xFin:  #   comienza debiendo termina debiendo (-)
                xTipo=2            
            elif xIni < 0 and xFin >= 0:                    #   comienza con saldo a favor termina debiendo
                xTipo = 3
            elif xIni >=0 and xFin < 0:                     #   comienza debiendo termina con saldo a favor
                xTipo = 6
            elif xIni < 0 and xFin < 0 and xFin >= xIni: 	#   comienza con saldo a favor termina con saldo a favor (-)
                xTipo = 7
            elif xIni < 0 and  xFin < 0 and xFin < xIni:    #   comienza con saldo a favor termina con saldo a favor (+)
                xTipo = 8
            ImpCon = justo.IMP_CON_CRE.objects.filter(cliente = Oficina.cliente,cod_imp = Reg.cod_imp).first()
            if ImpCon == None:
                ImpCon = justo.IMP_CON_CRE.objects.filter(cliente = Oficina.cliente,cod_imp = Reg.cod_imp).first()
                if ImpCon == None:
                    print('Grave  ',Reg.cod_cre,'  Inicio ',Reg.cod_imp,' Final ',Reg.cod_imp)
            ImpConCat = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = Reg.cod_imp,categoria = xCatFin).first()
            if ImpConCat == None:
                ImpConCat = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = Reg.cod_imp,categoria = xCatFin).first()
            
            CatAct = justo.CARTE_CAT_HIS.objects.filter(oficina = Oficina,fecha = self.fecha_rec,cod_cre = Reg.cod_cre).first()
            if Reg.cat_fin < 'C':                           #   Los Interese causados van a ingreso
                self.AsiRecInt.actualizar(ImpCon.kcta_ingreso,xNit,'Ingres',xCodCre,0,Reg.int_cau_mes)
                zCredito = zCredito + Reg.int_cau_mes
                Reg.ingreso = Reg.ingreso - Reg.int_cau_mes
                xDifMes = Reg.int_cau_mes - Reg.int_pag_act - (-xIni if xTipo == 3 else (-xIni if xTipo > 6 else 0))
                xDifMes = xDifMes - (Reg.int_pag if Reg.int_pag < 0 and xTipo == 3 else 0)
                if xDifMes > 0:
                    self.AsiRecInt.actualizar(ImpConCat.kcxc_ic,xNit,'CxC',xCodCre,xDifMes,0)
                    zDebito = zDebito + xDifMes 
                    CatAct.cat_int_mes = Reg.cat_fin
                    CatAct.sal_cat_int = xDifMes
                    CatAct.save()
            else:   #  No se afecta el ingreso 
                if xIni < 0 :
                    xIngCre = Reg.int_pag_act - xIni
                else:
                    xIngCre = Reg.int_pag_act
                if xIngCre > 0:
                    Reg.ingreso = Reg.ingreso -xIngCre
                    self.AsiRecInt.actualizar(ImpCon.kcta_ingreso,xNit,'Ingres',xCodCre,0,xIngCre)
                    zCredito = zCredito + xIngCre   #    xc+CateInte.IPAct
                if Reg.int_cau_mes > xIngCre:
                    self.AsiRecInt.actualizar(ImpConCat.kord_ic,xNit,'CtaOrd',xCodCre,0,Reg.int_cau_mes - xIngCre)
                    if Reg.cat_fin == 'C':
                        CatZ = 'W'
                    elif Reg.cat_fin == 'D':
                        CatZ = 'X'
                    elif Reg.cat_fin == 'E':
                        CatZ = 'Y'
                    elif Reg.cat_fin == 'F':
                        CatZ = 'Z'
                    self.AsiRecInt.actualizar(ImpCon.kic_orden_i,xNit,'CtaOrd',xCodCre,Reg.int_cau_mes - xIngCre,0)
                    zCredito = zCredito + Reg.int_cau_mes - xIngCre
                    zDebito = zDebito + Reg.int_cau_mes - xIngCre
                    if Reg.int_cau_mes - xIngCre > 0 :
                        CatAct.cat_int_mes = CatZ
                        CatAct.sal_cat_int =  Reg.int_cau_mes - xIngCre
                        CatAct.save()
                if Reg.int_pag > 0:
                    self.AsiRecInt.actualizar(ImpCon.kpte_ic,xNit,'Ingres',xCodCre,Reg.int_pag,0)
                    zDebito = zDebito + Reg.int_pag
                elif Reg.int_pag < 0:
                    self.AsiRecInt.actualizar(ImpCon.kpte_ic,xNit,'Ingres',xCodCre,0,-Reg.int_pag)
                    zCredito = zCredito - Reg.int_pag
            
            if Reg.int_pag > 0:     #  Aqui Afecta la Cta Pte
                self.AsiRecInt.actualizar(ImpCon.kpte_ic,xNit,'CtaPte',xCodCre,Reg.int_pag,0)
                zDebito = zDebito + Reg.int_pag
            else:                   #  Pudo haber sido un pago negativo cuando es Interes Adelantado
                self.AsiRecInt.actualizar(ImpCon.kpte_ic,xNit,'CtaPte',xCodCre,0,-Reg.int_pag)
                zCredito = zCredito - Reg.int_pag
            
            if xTipo < 3 or xTipo == 6:
                if Reg.int_pag_ant > 0 or (xTipo == 2 and Reg.ingreso > 0):
                    xLimCxC = Reg.int_pag_ant
                    xIntPag = xLimCxC
                    if xTipo == 2 and Reg.ingreso > 0:
                        xLimCxC = xLimCxC + Reg.ingreso
                    RegHiss = [regis for regis in  CurCatHis.rows if regis.CodCre == Reg.cod_cre]
                    for RegHis in RegHiss:
                        if RegHis.Valor > 0: 
                            xAboCxC = RegHis.Valor if RegHis.Valor <= xLimCxC else xLimCxC
                            xAboCxC = RegHis.Valor if xAboCxC > xIntPag else xAboCxC
                            if xAboCxC > 0:
                                xAboIntPag = xIntPag if xAboCxC > xIntPag else xAboCxC
                                xIntPag = xIntPag - xAboIntPag
                                if RegHis.Categoria < 'G':
                                    RegImpCatH = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = ImpCon.cod_imp,categoria = RegHis.Categoria).first()
                                    self.AsiRecInt.actualizar(RegImpCatH.kcxc_ic,xNit,'CxC',xCodCre,0,xAboCxC)
                                    zCredito = zCredito + xAboCxC
                                    if RegHis.Categoria == 'A':
                                        Reg.ip_ant_A = Reg.ip_ant_A + xAboIntPag
                                    elif RegHis.Categoria == 'B':
                                        Reg.ip_ant_B = Reg.ip_ant_B + xAboIntPag
                                    elif RegHis.Categoria == 'C':
                                        Reg.ip_ant_C = Reg.ip_ant_C + xAboIntPag
                                    elif RegHis.Categoria == 'D':
                                        Reg.ip_ant_D = Reg.ip_ant_D + xAboIntPag
                                    elif RegHis.Categoria == 'E':
                                        Reg.ip_ant_E = Reg.ip_ant_E + xAboIntPag
                                    elif RegHis.Categoria == 'B':
                                        Reg.ip_ant_E = Reg.ip_ant_E + xAboIntPag
                                else:
                                    self.AsiRecInt.actualizar(ImpCon.kcta_ingreso,xNit,'IngRec ',xCodCre,0,xAboCxC)
                                    zCredito = zCredito + xAboCxC  
                                    if RegHis.Categoria == 'W':
                                        xCtaHom = 'C'
                                    elif RegHis.Categoria == 'X':
                                        xCtaHom = 'D'
                                    elif RegHis.Categoria == 'Y':
                                        xCtaHom = 'E'
                                    elif RegHis.Categoria == 'Z':
                                        xCtaHom = 'F'
                                    RegImpCatH = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = ImpCon.cod_imp,categoria = xCtaHom).first()
                                    self.AsiRecInt.actualizar(RegImpCatH.kord_ic,xNit,'IngRec',xCodCre,0,xAboCxC)
                                    zCredito = zCredito + xAboCxC  
                                    self.AsiRecInt.actualizar(ImpCon.kic_orden_i,xNit,'IngRec',xCodCre,xAboCxC,0)
                                    zDebito = zDebito + xAboCxC  
                                xLimCxC = xLimCxC - xAboCxC
                            RegHis.Valor = RegHis.Valor - xAboCxC
                            if RegHis.Valor > 0 and Reg.int_con > 0:
                                xOtrVal = Reg.int_con if RegHiss.Valor < Reg.int_con else Reg.int_con
                                RegHis.Valor = RegHis.Valor - xOtrVal
                                Reg.int_con = Reg.int_con - xOtrVal
                    if xLimCxC > 0:
                        self.AsiRecInt.actualizar('51109501',xNit,'Error',xCodCre,0,xLimCxC)
                        zCredito = zCredito + xLimCxC
                if xTipo == 6:
                    self.AsiRecInt.actualizar('27200505',xNit,'CxP',xCodCre,xLimCxC,Reg.int_pag_ade)
                    zCredito = zCredito + Reg.int_pag_ade
                    Reg.cue_por_pag = Reg.cue_por_pag - Reg.int_pag_ade
            if xTipo == 3:
                self.AsiRecInt.actualizar('27200505',xNit,'CxP',xCodCre,-xIni,0)
                Reg.cue_por_pag = Reg.cue_por_pag - xIni
                zDebito = zDebito - xIni
            if xTipo == 7 or xTipo == 8:
                xDifDef = xFin - xIni
                if xDifDef > 0:
                    self.AsiRecInt.actualizar('27200505',xNit,'CxP',xCodCre,xDifDef,0)
                    zCredito = zCredito - xDifDef
                    Reg.cue_por_pag = Reg.cue_por_pag + xDifDef
                else:
                    self.AsiRecInt.actualizar('27200505',xNit,'CxP',xCodCre,0,-xDifDef)
                    zDebito = zDebito + xDifDef
                    Reg.cue_por_pag = Reg.cue_por_pag + xDifDef
            
            RegHiss = [regis for regis in  CurCatHis.rows if regis.CodCre == Reg.cod_cre]
            for RegHis in RegHiss:
                xNueCat = Reg.cat_fin
                if RegHis.Valor > 0:
                    if RegHis.Categoria != xNueCat and  RegHis.Categoria <= 'F':
                        ImpConCat1 = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = ImpCon.cod_imp,categoria = RegHis.Categoria).first()
                        self.AsiRecInt.actualizar(ImpConCat1.kcxc_ic,xNit,'CxC',xCodCre,0,RegHis.Valor)
                        zCredito = zCredito + RegHis.Valor
                        ImpConCat2 = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = ImpCon.cod_imp,categoria = xNueCat).first()
                        self.AsiRecInt.actualizar(ImpConCat2.kcxc_ic,xNit,'CxC',xCodCre,RegHis.Valor,0)
                        zDebito = zDebito + RegHis.Valor
                        RegHis.Categoria = xNueCat
                    if RegHis.Categoria > "F" and ((RegHis.Categoria == "W" and xNueCat != "C") or (RegHis.Categoria == "X" and xNueCat != 'D') or (RegHis.Categoria == 'Y' and xNueCat != 'E') or (RegHis.Categoria == 'Z' and xNueCat != 'F')):
                        if RegHis.Categoria == 'W':
                            xCtaHom = 'C'
                        elif RegHis.Categoria == 'X':
                            xCtaHom = 'D'
                        elif RegHis.Categoria == 'Y':
                            xCtaHom = 'E'
                        elif RegHis.Categoria == 'Z':
                            xCtaHom = 'F'
                        ImpConCat1 = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = ImpCon.cod_imp,categoria = xCtaHom).first()
                        self.AsiRecInt.actualizar(ImpConCat1.kcxc_ic,xNit,'CxC',xCodCre,0,RegHis.Valor)
                        zCredito = zCredito + RegHis.Valor
                        if xNueCat < 'C':
                            Reg.ingreso = Reg.ingreso - RegHis.Valor
                            self.AsiRecInt.actualizar(ImpCon.kic_orden_i,xNit,'CtaOrI',xCodCre,RegHis.Valor,0)
                            zDebito = zDebito + RegHis.Valor
                            self.AsiRecInt.actualizar(ImpCon.kcta_ingreso,xNit,'IngRec',xCodCre,0,RegHis.Valor)
                            zCredito = zCredito + RegHis.Valor
                            ImpConCat1 = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = ImpCon.cod_imp,categoria = xNueCat).first()
                            self.AsiRecInt.actualizar(ImpConCat1.kcxc_ic,xNit,'CtaOrI',xCodCre,RegHis.Valor,0)
                            zDebito = zDebito + RegHis.Valor
                            xNueCatSal  = xNueCat
                        else:
                            ImpConCat1 = justo.IMP_CON_CRE_INT.objects.filter(cliente = Oficina.cliente,cod_imp = ImpCon.cod_imp,categoria = xNueCat).first()
                            self.AsiRecInt.actualizar(ImpConCat1.kord_ic,xNit,'CxC',xCodCre,RegHis.Valor,0)
                            zDebito = zDebito + RegHis.Valor
                            if Reg.cat_fin == 'C':
                                xNueCatSal = 'W'
                            if Reg.cat_fin == 'D':
                                xNueCatSal = 'X'
                            if Reg.cat_fin == 'E':
                                xNueCatSal = 'Y'
                            if Reg.cat_fin == 'F':
                                xNueCatSal = 'Z'
                        RegHis.Categoria = xNueCatSal
            if zDebito != zCredito :
                if zDebito > zCredito:
                    self.AsiRecInt.actualizar('51109501',xNit,'Error ',xCodCre,0,zDebito - zCredito)
                else:
                    self.AsiRecInt.actualizar('51109501',xNit,'Error ',xCodCre,-zDebito+zCredito,0)
            #   Termino            
            RegHiss = [regis for regis in  CurCatHis.rows if regis.CodCre == Reg.cod_cre]
            for RegHis in RegHiss:
                if RegHis.Valor > 0:
                    CatHisCre = justo.CARTERA_CXC.objects.filter(oficina = Oficina,cod_cre = RegHis.CodCre,
                        fecha = self.fecha_rec,fec_ref = RegHis.FechaRef,categoria = RegHis.Categoria).first() 
                    if CatHisCre == None:
                        CatHisCre = justo.CARTERA_CXC.objects.create(oficina = Oficina,cod_cre = RegHis.CodCre,
                        fecha = self.fecha_rec,fec_ref = RegHis.FechaRef,categoria = RegHis.Categoria)
                    CatHisCre.valor = RegHis.Valor
                    CatHisCre.categoria = RegHis.Categoria
                    CatHisCre.save()
                    if RegHis.Categoria == 'A' :
                        Reg.cue_pr_cob_A = Reg.cue_pr_cob_A + RegHis.Valor
                    elif RegHis.Categoria == 'B' :
                        Reg.cue_pr_cob_B = Reg.cue_pr_cob_B + RegHis.Valor
                    elif RegHis.Categoria == 'C' :
                        Reg.cue_pr_cob_C = Reg.cue_pr_cob_C + RegHis.Valor
                    elif RegHis.Categoria == 'D' :
                        Reg.cue_pr_cob_D = Reg.cue_pr_cob_D + RegHis.Valor
                    elif RegHis.Categoria == 'E' :
                        Reg.cue_pr_cob_E = Reg.cue_pr_cob_E + RegHis.Valor
                    elif RegHis.Categoria == 'F' :
                        Reg.cue_pr_cob_F = Reg.cue_pr_cob_F + RegHis.Valor
                    elif RegHis.Categoria == 'W' :
                        Reg.cau_ZC = Reg.cau_ZC + RegHis.Valor
                    elif RegHis.Categoria == 'X' :
                        Reg.cau_ZD = Reg.cau_ZD + RegHis.Valor
                    elif RegHis.Categoria == 'Y' :
                        Reg.cau_ZE = Reg.cau_ZE + RegHis.Valor
                    elif RegHis.Categoria == 'Z' :
                        Reg.cau_ZET = Reg.cau_ZET + RegHis.Valor
            Reg.save()
            self.AsiRecInt.eliminar_iguales()  #  Se borran los iguales 
            self.AsiRecInt.guardar_en_excel('ReclaInt.xlsx','C:/AAA/')
        return
        
    def Llevar_a_historico(self,Oficina):
        Creditos = justo.CREDITOS.objects.filter(oficina = Oficina)
        for Credito in Creditos:
            print(Credito.cod_cre)
            if Credito.fec_des.year == self.fecha_rec.year and Credito.fec_des.month == self.fecha_rec.month:
                continue
            HisAnt = justo.CARTE_CAT_HIS.objects.filter(oficina = Oficina,fecha = self.fecha_ant_rec,cod_cre = Credito.cod_cre).first()
            if HisAnt == None:
                Credito.estado = 'H'
                Credito.save()
        return

class perdida_esperada:
    Oficina = None
    fecha = None
    arr_his = np.zeros(36, dtype=int)

    def __init__(self,iOficina,iFecha):
        self.Oficina = iOficina 
        self.fecha = iFecha
        
    def calculo_pi(self,iCodCre):
        xSalPre = 0
        self.arr_his.fill(0) 
        Cred = justo.CREDITOS.objects.filter(oficina = self.Oficina,cod_cre = iCodCre).first()
        xPLAZOL = 1 if Cred.num_cuo_act > 36 else 0
        xVIN2 = 1 if (self.fecha - Cred.socio.fec_afi).days > 3650 else 0
        xANTIPRE1 = 1 if (Cred.fec_des - Cred.socio.fec_afi).days < 31 else 0
        xANTIPRE2 = 1 if (Cred.fec_des - Cred.socio.fec_afi).days > 365*3 else 0
        xREESTRUCT = 0
        xAporte = 0
        Aportes = justo.DETALLE_PROD.objects.filter(oficina = self.Oficina,producto='AP',hecho_econo__fecha__lte=self.fecha,
            subcuenta=Cred.socio.cod_aso).aggregate(total_apor=Sum('valor'))
        if Aportes['total_apor'] == None:
            xAporte = 0 
        else:
            xAporte = -Aportes['total_apor']
        xAP = 1 if xAporte > 0 else 0
        xEA = 1
        XCOOPCDAT = XCUENAHO = XCDAT = xPER = 0
        CtasAho = justo.CTAS_AHORRO.objects.filter(oficina = self.Oficina,asociado = Cred.socio)
        for CtaAho in CtasAho:
            SalCta = justo.DETALLE_PROD.objects.filter(oficina = self.Oficina,concepto='AHO',hecho_econo__fecha__lte=self.fecha,
                subcuenta=CtaAho.num_cta).aggregate(saldo_cta=Sum('valor'))
            if 'saldo_cta' in SalCta and SalCta['saldo_cta'] is not None:
                xSalCta = -SalCta['saldo_cta']
            else:
                xSalCta = 0
            if CtaAho.num_cta[:2] == '04' and xSalCta > 0:
                XCOOPCDAT = 1
                XCDAT = 1
            elif xSalCta > 1:
                XCUENAHO = 1 
        fec_cor = self.fecha.replace(day=1) - timedelta(days=1)
        for iMes in range(36):
            CreHis = justo.CARTE_CAT_HIS.objects.filter(oficina = self.Oficina,fecha = fec_cor,cod_cre = iCodCre).first()
            if CreHis != None:
                self.arr_his[iMes] = CreHis.dias_mor
                if iMes == 0:
                    SalPre = 1 if CreHis.cap_ini * 0.2 > CreHis.sal_cap else 0
            fec_cor = fec_cor.replace(day=1) - timedelta(days=1)
        M1 = M2 = M3 = NMORAS1_31_60 = NMORAS3_31_60 = NUMMORTRIN = 0
        for iMes in range(36):
            if iMes < 35:
                M3 = self.arr_his[iMes] if self.arr_his[iMes] > M3 else M3
            if iMes < 24: 
                M2 = self.arr_his[iMes] if self.arr_his[iMes] > M2 else M2
            if iMes < 12: 
                M1 = self.arr_his[iMes] if self.arr_his[iMes] > M1 else M1
                NMORAS1_31_60 = NMORAS1_31_60 + (1 if self.arr_his[iMes] >= 31 and self.arr_his[iMes] <= 60 else 0)
            if iMes < 3: 
                NMORAS3_31_60 = NMORAS3_31_60 + (1 if self.arr_his[iMes] >= 31 and self.arr_his[iMes] <= 60 else 0)

        xTC = xFE = xESIN = xFAMOR = xVALCUOTA = xVALPRES = xOCOOP = xFONAHO = xFONDPLAZO = xENTIDAD1 = 0
        HisPun = justo.PE_CARTE_HIS.objects.filter(oficina = self.Oficina,fecha = self.fecha,cod_cre = iCodCre).first()
        if HisPun == None:
            HisPun = justo.PE_CARTE_HIS.objects.create(oficina = self.Oficina,fecha = self.fecha,cod_cre = iCodCre)
        HisPun.modalidad = 'CCSL' if Cred.for_pag == 'P' else 'CCCL'
        HisPun.val_ea = xEA
        HisPun.val_ap = xAP
        HisPun.val_tc = xTC
        HisPun.val_fe = xFE
        HisPun.val_esim = 0
        HisPun.val_famor = xFAMOR
        HisPun.val_valcuota = xVALCUOTA
        HisPun.val_valpres = xVALPRES
        HisPun.val_ocoop = xOCOOP
        HisPun.val_fonaho = xFONAHO
        HisPun.val_coopcdat = XCOOPCDAT
        HisPun.val_fondplazo = xFONDPLAZO
        HisPun.val_antipre1 = xANTIPRE1
        HisPun.val_mora15 = 1 if M1 >= 16 and M1 <= 30 else 0
        HisPun.val_mora1230 = 1 if M1 >= 31 and M1 <= 60 else 0
        HisPun.val_mora1260 = 1 if M1 > 60 else 0
        HisPun.val_mora2430 = 1 if M2 >= 31 and M2 <= 60 else 0
        HisPun.val_mora2460 = 1 if M2 > 60 else 0
        HisPun.val_mora3615 = 1 if M3 > 0 and M3 <= 15 else 0
        HisPun.val_m1mora30 = 1 if NMORAS1_31_60 == 1 else 0
        HisPun.val_m2mora30 = 1 if M3 >= 31 and M3 <= 60 else 0
        HisPun.val_m1mora30m3 = 1 if NMORAS1_31_60 == 1 else 0
        HisPun.val_simmora = 1 if M1 + M2 + M3 == 0 else 0
        HisPun.val_mortrim = 1 if NMORAS3_31_60 > 0 else 0
        HisPun.val_salpres =  xSalPre
        HisPun.val_cuenaho = XCUENAHO
        HisPun.val_reest = xREESTRUCT
        HisPun.val_cdat = XCDAT
        HisPun.val_per = 0
        HisPun.val_entidad1 = xENTIDAD1
        HisPun.val_antipre2 = xANTIPRE2
        HisPun.val_vin2 = xVIN2
        HisPun.val_entidad2 = 1
        HisPun.val_plazol = xPLAZOL
        HisPun.val_amor = 0
        HisPun.val_nodo4 = 0
        HisPun.val_nodo5 = 0
        HisPun.val_nodo7 = 0
        HisPun.val_nodo8 = 0
        HisPun.val_nodo9 = 0
        HisPun.val_nodo1 = 0
        HisPun.val_mora3660 = 0
        Mod = justo.PE_MODE_REFE.objects.filter(cliente = self.Oficina.cliente,modalidad = HisPun.modalidad).first()
        xz = 0
        xz = xz + Mod.constante + HisPun.val_ea*Mod.coe_ea + HisPun.val_ap*Mod.coe_ap + HisPun.val_tc * Mod.coe_tc + HisPun.val_fe * Mod.coe_fe 
        xz = xz + HisPun.val_famor*Mod.coe_famor + HisPun.val_valcuota*Mod.coe_valcuota + HisPun.val_valpres*Mod.coe_valpres + HisPun.val_ocoop*Mod.coe_ocoop
        xz = xz + HisPun.val_fonaho*Mod.coe_fonaho + HisPun.val_fondplazo*Mod.coe_fondplazo + HisPun.val_antipre1*HisPun.val_antipre1 + HisPun.val_coopcdat*Mod.coe_coopcdat
        xz = xz + HisPun.val_mora15*Mod.coe_mora15 + HisPun.val_mora1230*Mod.coe_mora1230 + HisPun.val_mora1260*Mod.coe_mora1260 + HisPun.val_mora2430*Mod.coe_mora2430
        xz = xz + HisPun.val_mora2460*Mod.coe_mora2460 + HisPun.val_mora3615*Mod.coe_mora3615 + HisPun.val_m1mora30*Mod.coe_m1mora30 + HisPun.val_m2mora30*Mod.coe_m2mora30
        xz = xz + HisPun.val_m2mora30*Mod.coe_m2mora30 + HisPun.val_m1mora30*Mod.coe_m1mora30 + HisPun.val_m1mora30m3+Mod.coe_m1mora30m3 + HisPun.val_simmora*Mod.coe_sinmora
        xz = xz + HisPun.val_mortrim*Mod.coe_mortrim + HisPun.val_cuenaho*Mod.coe_cuenaho + HisPun.val_cdat*Mod.coe_cdat + HisPun.val_entidad1*Mod.coe_entidad1
        xz = xz + HisPun.val_antipre2*Mod.coe_antipre2 + HisPun.val_vin2*Mod.coe_vin2 + HisPun.val_entidad2*Mod.coe_entidad2 + HisPun.val_plazol*Mod.coe_plazol
        xz = xz + HisPun.val_nodo1*Mod.coe_nodo1 + HisPun.val_nodo4*Mod.coe_nodo4 + HisPun.val_nodo5*Mod.coe_nodo5 + HisPun.val_nodo7*Mod.coe_nodo7
        xz = xz + HisPun.val_nodo8*Mod.coe_nodo8 + HisPun.val_nodo9*Mod.coe_nodo9 + HisPun.val_salpres*Mod.coe_salpres + HisPun.val_reest*Mod.coe_reest
        xPuntaje = 1/(1+math.exp(-xz))
        HisPun.z = xz
        HisPun.puntaje = xPuntaje
        
        RanCals = justo.PE_CALIF_RANGO.objects.filter(cliente = self.Oficina.cliente,clase_coop = self.Oficina.cliente.clase_coop,
                modalidad = HisPun.modalidad).order_by('-calificacion')
        xCal = ' '
        for RanCal in RanCals:
            if HisPun.puntaje < RanCal.pi_puntaje:
                xCal = RanCal.calificacion
                
        HisPun.calificacion = xCal
        PerEsp = justo.PE_PI_CALIF.objects.filter(cliente = self.Oficina.cliente,clase_coop = self.Oficina.cliente.clase_coop,
                modalidad = HisPun.modalidad,calificacion = HisPun.calificacion).first()
        HisPun.pi = PerEsp.pi_porcent
        CarCatHis = justo.CARTE_CAT_HIS.objects.filter(oficina = self.Oficina,fecha = self.fecha,cod_cre = HisPun.cod_cre).first()
        if CarCatHis == None:
            print(HisPun.cod_cre)
            return
        PePdi = justo.PE_PDI_RANGO.objects.filter(cliente = self.Oficina.cliente,garantia = Cred.tip_gar).first()
        if CarCatHis.dias_mor < PePdi.dias_inc_1:
            HisPun.pdi = PePdi.pdi_0
        elif CarCatHis.dias_mor < PePdi.dias_inc_2:
            HisPun.pdi = PePdi.pdi_1
        else:
            HisPun.pdi = PePdi.pdi_2
        HisPun.vea = CarCatHis.sal_cap + CarCatHis.sal_int_dia + CarCatHis.int_cau_res_per
        HisPun.pe = round(HisPun.pi/100 * HisPun.pdi/100 * HisPun.vea,0) 
        HisPun.save()


def init():
    print('Inicia Perdida Esperada   ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    fecha = date(2023,12,31)
    per_esp = perdida_esperada(Oficina,fecha)
    Creditos = justo.CREDITOS.objects.filter(oficina=Oficina,estado = 'A')
    for Credito in Creditos:
        per_esp.calculo_pi(Credito.cod_cre)
    print('Final  Perdida Esperada   ',datetime.now())
    
def init_recla():
    print('Inicia la Reclasificacion   ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    fecha = date(2023,12,31)
    ReclaMes = Reclasificacion(fecha,Oficina)
    ReclaMes.Creacion_tablas(fecha,Oficina)
    #ReclaMes.Llevar_a_historico(Oficina)
    ReclaMes.ReclaProv_capital(Oficina)
    ReclaMes.ReclaProv_interes(Oficina)
    print('Fin Reclasificacion         ',datetime.now(),ReclaMes.fecha_ant_rec,'  Fecha Ant Rec',ReclaMes.fecha_rec)
    return

def initcre():
    print('Inicio  ',datetime.now())
    lista_creditos = []
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    Creditos = justo.CREDITOS.objects.filter(oficina=Oficina,estado = 'A')
    for Credito in Creditos:
        liq_cre = Liquida_cre(Credito.cod_cre) 
        #liq_cre.Exportar_mov()
        #liq_cre.eliminar_pago(483603)
        liq_cre.liq_al_dia()
        imprime_liq(liq_cre)
        if liq_cre.lista_mov == None:
            print('Problemas Credito ',Credito.cod_cre)
            continue
        liq_cre.liq_al_dia()
        sal_cre = Sal_cre(liq_cre.cod_cre,Credito.estado,liq_cre.sal_cap_tot,liq_cre.sal_cap_dia,liq_cre.sal_int_dia,liq_cre.int_mor_cau,(liq_cre.fecha_focal-liq_cre.fec_al_dia).days)
        lista_creditos.append(vars(sal_cre))
        #print('Por Cuota  ',liq_cre.sal_cap_dia+liq_cre.sal_int_dia+liq_cre.int_mor_cau)
        #liq_cre.distri_pago_cuota(2200000)
        #liq_cre.distri_pago_abo(3000000) 
        #liq_cre.tip_pag = 'ABOCU'
        #liq_cre.aplicar_pago(3000000)
        #imprime_liq(liq_cre)

        #   liq_cre.Exportar_mov()
        #   liq_cre.liq_por_cuotas(liq_cre.cuo_pag+2)
        #   liq_cre.distri_pago(2000000)
    
    ruta_excel = "c:/aaa/cart_justo.xlsx"
    df = pd.DataFrame(lista_creditos)
    #writer = pd.ExcelWriter(ruta_excel, engine='xlsxwriter')
    #workbook  = writer.book
    #worksheet = writer.sheets['Hoja1']  # Ajusta el nombre de la hoja según tu caso
    #workbook.close()

    with pd.ExcelWriter(ruta_excel, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Hoja1', index=False)
        workbook = writer.book

    print('Final   ',datetime.now())

init()