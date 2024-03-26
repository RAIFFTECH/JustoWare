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
from django.db.models import Max



class ahorros():
    Oficina = None
    num_cta = None
    saldo_fecha = 0.0
    def __init__(self,iOficina):
        self.Oficina = iOficina
  
    def saldo_cta(self,inum_cta,ifecha = datetime.now().date()):   
        self.num_cta = inum_cta
        self.saldo_fecha = 0
        fecha_minima = datetime.strptime('1900-01-01', '%Y-%m-%d').date()
        RegFec = justo.DETALLE_PROD.objects.filter(oficina = self.Oficina,producto='AH',subcuenta=inum_cta,hecho_econo__anulado='N',
            detalle_econo__item_concepto='SalIni',detalle_econo__detalle_prod=F('id'),
            hecho_econo__fecha__lte = ifecha).values('subcuenta').annotate(fecha_min=Coalesce(Max('hecho_econo__fecha'), fecha_minima)).order_by('-fecha_min').first()
        if RegFec == None:
            xFecIni = fecha_minima
        else:
            xFecIni = RegFec['fecha_min']
        SalAho = justo.DETALLE_PROD.objects.filter(oficina = self.Oficina,producto='AH',subcuenta=inum_cta,hecho_econo__anulado='N',
            detalle_econo__detalle_prod=F('id'),hecho_econo__fecha__gte = xFecIni,hecho_econo__fecha__lte = ifecha
            ).aggregate(saldo=Sum(F('detalle_econo__debito') - F('detalle_econo__credito')))
        if SalAho == None or SalAho['saldo'] == None :
            self.saldo_fecha = 0
        else:
            self.saldo_fecha = SalAho['saldo']
        return

def init():
    print('Inicio Saldos Ahorro  ',datetime.now())
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    fecha_liq = date(2023,12,30)
    miliq = ahorros(Oficina)
    Ctas = justo.CTAS_AHORRO.objects.filter(oficina = Oficina,est_cta = 'P').exclude(Q(num_cta__startswith='04'))
    saldo = 0
    for Cta in Ctas:
        miliq.saldo_cta(Cta.num_cta,fecha_liq)
        saldo = saldo - miliq.saldo_fecha
        if Cta.num_cta[0:2] != '04':
            LinAho = justo.LINEAS_AHORRO.objects.filter(cliente = Oficina.cliente,cod_lin_aho = Cta.num_cta[0:2]).first()
            TasLin = justo.TAS_LIN_AHO.objects.filter(lin_aho=LinAho,fecha_inicial__lte=fecha_liq, fecha_final__gte=fecha_liq).first()
            TasRF = justo.RET_FUE_AHO.objects.filter(lin_aho = LinAho,fecha_inicial__lte=fecha_liq, fecha_final__gte=fecha_liq).first()
            xTasIntDia = TasLin.tiae / 100
            xTasNomDia = round(((1 + xTasIntDia) ** (1 / 365)) - 1,6)
            xIntDia = round(miliq.saldo_fecha*xTasNomDia,0) 
            if xIntDia < 0:
                xDesRF = round(-xIntDia*TasRF.tas_liq_rf,0)  if TasRF.bas_liq_int <= -xIntDia else 0
                DiaInt = justo.INT_DIA_AHO.objects.filter(oficina = Oficina,cta_aho = Cta,num_cta = Cta.num_cta,dia_mes = fecha_liq.day).first()
                if DiaInt == None:
                    DiaInt = justo.INT_DIA_AHO.objects.create(oficina = Oficina,cta_aho = Cta,num_cta = Cta.num_cta,dia_mes = fecha_liq.day)
                DiaInt.fecha = fecha_liq
                DiaInt.int_dia = xIntDia
                DiaInt.ret_fue = xDesRF
                DiaInt.aplicado = 'N'
                DiaInt.save()

    LinAho = justo.LINEAS_AHORRO.objects.filter(cliente = Oficina.cliente,cod_lin_aho = '04').first()
    TasRF = justo.RET_FUE_AHO.objects.filter(lin_aho = LinAho,fecha_inicial__lte=fecha_liq, fecha_final__gte=fecha_liq).first()
    xHayCda = False
    CdatFecs = justo.CTA_CDAT_AMP.objects.filter(fecha = fecha_liq)
    for CdatFec in CdatFecs:
        if CdatFec.cta_aho.oficina != Oficina:
            continue
        if xHayCda == False:
            Doc = justo.DOCTO_CONTA.objects.filter(oficina = Oficina,per_con = fecha_liq.year,codigo = 131).first()
            HecEco = justo.HECHO_ECONO.objects.filter(docto_conta = Doc,numero = fecha_liq.timetuple().tm_yday).first()
            if HecEco == None:
                HecEco = justo.HECHO_ECONO.objects.create(docto_conta = Doc,numero = fecha_liq.timetuple().tm_yday)
            HecEco.fecha = fecha_liq
            HecEco.descripcion = 'Intereses y retencion de Ctas de Ahorros y Cdat '
            HecEco.anulado = 'N'
            HecEco.protegido = 'S'
            HecEco.canal = 'OFI'
            HecEco.save()
            xHayCda = True
        Cdat = justo.CTA_CDAT.objects.filter(cta_aho = CdatFec.cta_aho).first()
        xPlaMes = Cdat.plazo_mes
        xFecIni = Cdat.fecha
        xPer = Cdat.Periodicidad
        xInt = xRetFueNue = xInt = xRetFue = 0
        MovCdas = justo.CTA_CDAT_LIQ.objects.filter(cta_amp = CdatFec.id)
        for MovCda in MovCdas:
            xInt = xInt + MovCda.Val_int
            xRetFue = xRetFue + MovCda.Val_ret + MovCda.Val_ret_nue
            xRefFueNue = xRetFueNue + MovCda.Val_ret_nue
            xFecIni = MovCda.fecha
        xIntPorApl = CdatFec.valor - xInt
        xRetFuePorApl = 0
        xUltRetFue = xRetFueNue 
        xTotRetFue = 0
        if CdatFec.valor > TasRF.bas_liq_int*30*xPlaMes/xPer or xRefFueNue > 0:
            xTotRetFue = xTotRetFue + xRetFue + xRetFuePorApl
        DetPro = justo.DETALLE_PROD.objects.filter(hecho_econo = HecEco,producto = 'AH',concepto = 'AHO',subcuenta = Cdat.cta_int_ret).first()
        if DetPro == None:
            DetPro = justo.DETALLE_PROD.objects.create(hecho_econo = HecEco,producto = 'AH',concepto = 'AHO',subcuenta = Cdat.cta_int_ret)
        DetPro.valor = xIntPorApl + xInt - xRetFue - xRetFuePorApl
        DetPro.save()
        justo.CTA_CDAT_LIQ.objects.filter(cta_amp = CdatFec,fecha__gte = fecha_liq).delete()
        MovCdaLiq = justo.CTA_CDAT_LIQ.objects.filter(cta_aho = CdatFec.cta_aho,cta_amp = CdatFec,fecha = fecha_liq,tip_liq = 'C').first()
        if MovCdaLiq == None:
            MovCdaLiq = justo.CTA_CDAT_LIQ.objects.create(cta_aho = CdatFec.cta_aho,cta_amp = CdatFec,fecha = fecha_liq,tip_liq = 'C')
        MovCdaLiq.fecha = fecha_liq
        MovCdaLiq.Val_int = xIntPorApl
        MovCdaLiq.Val_ret = xRetFuePorApl if xUltRetFue > 0 else 0
        MovCdaLiq.Val_ret_nue = 0
        MovCdaLiq.save()
        MovCdaLiq1 = justo.CTA_CDAT_LIQ.objects.filter(cta_aho = CdatFec.cta_aho,cta_amp = CdatFec,fecha = fecha_liq,tip_liq = 'P').first()
        if MovCdaLiq1 == None:
            MovCdaLiq1 = justo.CTA_CDAT_LIQ.objects.create(cta_aho = CdatFec.cta_aho,cta_amp = CdatFec,fecha = fecha_liq,tip_liq = 'P')
        MovCdaLiq1.fecha = fecha_liq
        MovCdaLiq1.Val_int = CdatFec.valor
        MovCdaLiq1.Val_ret = -(xRetFue + xRetFuePorApl)
        MovCdaLiq1.Val_ret_nue = 0
        MovCdaLiq1.save()
        xCtaPXCda = LinAho.cta_por_pas
        CtaAho = justo.CTAS_AHORRO.objects.filter(oficina = Oficina,id = Cdat.cta_aho_id).first()
        ImpCon = justo.IMP_CON_LIN_AHO.objects.filter(linea_ahorro = LinAho,cod_imp = CtaAho.cod_imp ).first()
        xCtaAhoDes = ImpCon.ctaafeact if CtaAho.est_cta == 'A' else ImpCon.ctaafeint
        xCtaInt = ImpCon.ctaafeint
        xCtaRetFue = ImpCon.ctaretfue
        if xIntPorApl > 0:
            PlaCtaInt = justo.PLAN_CTAS.objects.filter(cliente = Oficina.cliente, per_con = fecha_liq.year,cod_cta = xCtaInt).first()
            DetEcoInt = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaInt,tercero = CtaAho.asociado.tercero).first()
            if DetEcoInt == None:
                DetEcoInt = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaInt,tercero = CtaAho.asociado.tercero)
            DetEcoInt.detalle = 'Gasto Causado Cta_aho '+CtaAho.num_cta
            DetEcoInt.debito = xIntPorApl
            DetEcoInt.credito = 0
            DetEcoInt.valor_1 = 0
            DetEcoInt.valor_2 = 0
            DetEcoInt.save()
            PlaCtaPag = justo.PLAN_CTAS.objects.filter(cliente = Oficina.cliente, per_con = fecha_liq.year,cod_cta = xCtaPXCda).first()
            DetEcoPag = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaPag,tercero = CtaAho.asociado.tercero).first()
            if DetEcoPag == None:
                DetEcoPag = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaPag,tercero = CtaAho.asociado.tercero)
            DetEcoPag.detalle = 'Ctas por Pagar Interes Cta_aho '+CtaAho.num_cta
            DetEcoPag.debito = 0
            DetEcoPag.credito = xIntPorApl
            DetEcoPag.valor_1 = 0
            DetEcoPag.valor_2 = 0
            DetEcoPag.save()
        if xIntPorApl + xInt - xRetFue - xRetFuePorApl - xUltRetFue != 0:
            PlaCtaPag = justo.PLAN_CTAS.objects.filter(cliente = Oficina.cliente, per_con = fecha_liq.year,cod_cta = xCtaPXCda).first()
            DetEcoPag = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaPag,tercero = CtaAho.asociado.tercero).first()
            if DetEcoInt == None:
                DetEcoPag = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaPag,tercero = CtaAho.asociado.tercero)
            DetEcoPag.detalle = 'Ctas Por Pag Cta_aho '+CtaAho.num_cta
            DetEcoPag.debito = xIntPorApl+xInt-xRetFue-xRetFuePorApl
            DetEcoPag.credito = 0
            DetEcoPag.valor_1 = 0
            DetEcoPag.valor_2 = 0
            DetEcoPag.save()
            PlaCtaAho = justo.PLAN_CTAS.objects.filter(cliente = Oficina.cliente, per_con = fecha_liq.year,cod_cta = xCtaAhoDes).first()
            DetEcoAho = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaAho,tercero = CtaAho.asociado.tercero).first()
            if DetEcoAho == None:
                DetEcoAho = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaAho,tercero = CtaAho.asociado.tercero)
            DetEcoAho.detalle_prod = DetPro
            DetEcoAho.item_concepto = 'IntCda'
            DetEcoAho.detalle = 'Interes y/0 Reten fuente Cuenta Cta_aho '+CtaAho.num_cta
            DetEcoAho.debito = 0
            DetEcoAho.credito = xIntPorApl+xInt-xRetFue-xRetFuePorApl
            DetEcoAho.valor_1 = 0
            DetEcoAho.valor_2 = 0
            DetEcoAho.save()

    print('Saldo Total    ',saldo)     
    print('Fin Saldos Ahorro     ',datetime.now())
    return

init()
