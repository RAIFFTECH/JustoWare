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


def es_ultimo_dia_del_mes(fecha):
    siguiente_dia = fecha + timedelta(days=1)
    return siguiente_dia.month != fecha.month

def ultimo_dia_mes_anterior(fecha):
    primer_dia_mes_actual = fecha.replace(day=1)
    ultimo_dia_mes_anterior = primer_dia_mes_actual - timedelta(days=1)
    return ultimo_dia_mes_anterior

class ahorros():
    Oficina = None
    num_cta = None
    fecha_liq = None
    saldo_fecha = 0.0

    def __init__(self,iOficina,iFecha):
        self.Oficina = iOficina
        self.fecha_liq = iFecha
  
    def saldo_cta(self,inum_cta,ifecha = None):
        if ifecha == None:
            ifecha = self.fecha_liq  
        self.num_cta = inum_cta
        self.saldo_fecha = 0
        fecha_minima = datetime.strptime('1900-01-01', '%Y-%m-%d').date()
        RegFec = justo.DETALLE_PROD.objects.filter(oficina = self.Oficina,producto='AH',subcuenta=inum_cta,hecho_econo__anulado='N',
            detalle_econo__item_concepto='SalIni',detalle_econo__detalle_prod=F('id'),
            hecho_econo__fecha__lte = self.fecha_liq).values('subcuenta').annotate(fecha_min=Coalesce(Max('hecho_econo__fecha'), fecha_minima)).order_by('-fecha_min').first()
        if RegFec == None:
            xFecIni = fecha_minima
        else:
            xFecIni = RegFec['fecha_min']
        SalAho = justo.DETALLE_PROD.objects.filter(oficina = self.Oficina,producto='AH',subcuenta=inum_cta,hecho_econo__anulado='N',
            detalle_econo__detalle_prod=F('id'),hecho_econo__fecha__gte = xFecIni,hecho_econo__fecha__lte = self.fecha_liq
            ).aggregate(saldo=Sum(F('detalle_econo__debito') - F('detalle_econo__credito')))
        if SalAho == None or SalAho['saldo'] == None :
            self.saldo_fecha = 0
        else:
            self.saldo_fecha = SalAho['saldo']
        return
    
    def interes_diario(self):
        print('Inicio Saldos Ahorro  ',datetime.now())
        Ctas = justo.CTAS_AHORRO.objects.filter(oficina=self.Oficina, est_cta='A').filter(Q(num_cta__startswith='03') | Q(num_cta__startswith='05'))
        Doc = justo.DOCTO_CONTA.objects.filter(oficina = self.Oficina,per_con = self.fecha_liq.year,codigo = 131).first()
        HecEco = justo.HECHO_ECONO.objects.filter(docto_conta = Doc,numero = self.fecha_liq.timetuple().tm_yday).first()
        if HecEco == None:
            HecEco = justo.HECHO_ECONO.objects.create(docto_conta = Doc,numero = self.fecha_liq.timetuple().tm_yday)
            HecEco.fecha = self.fecha_liq
            HecEco.descripcion = 'Intereses y retencion de Ctas de Ahorros y Cdat '
            HecEco.anulado = 'N'
            HecEco.protegido = 'S'
            HecEco.canal = 'OFI'
            HecEco.save()
        saldo = 0
        for Cta in Ctas:
            self.saldo_cta(Cta.num_cta)
            saldo = saldo - self.saldo_fecha
            if Cta.num_cta[0:2] != '04':
                LinAho = justo.LINEAS_AHORRO.objects.filter(cliente = self.Oficina.cliente,cod_lin_aho = Cta.num_cta[0:2]).first()
                TasLin = justo.TAS_LIN_AHO.objects.filter(lin_aho=LinAho,fecha_inicial__lte=self.fecha_liq, fecha_final__gte=self.fecha_liq).first()
                TasRF = justo.RET_FUE_AHO.objects.filter(lin_aho = LinAho,fecha_inicial__lte=self.fecha_liq, fecha_final__gte=self.fecha_liq).first()
                xTasIntDia = TasLin.tiae / 100
                xTasNomDia = round(((1 + xTasIntDia) ** (1 / 365)) - 1,6)
                xIntDia = round(self.saldo_fecha*xTasNomDia,0) 
                if xIntDia < 0:
                    xDesRF = round(-xIntDia*TasRF.tas_liq_rf,0)  if TasRF.bas_liq_int <= -xIntDia else 0
                    DiaInt = justo.INT_DIA_AHO.objects.filter(oficina = self.Oficina,cta_aho = Cta,num_cta = Cta.num_cta,dia_mes = self.fecha_liq.day).first()
                    if DiaInt == None:
                        DiaInt = justo.INT_DIA_AHO.objects.create(oficina = self.Oficina,cta_aho = Cta,num_cta = Cta.num_cta,dia_mes = self.fecha_liq.day)
                    DiaInt.fecha = self.fecha_liq
                    DiaInt.int_dia = xIntDia
                    DiaInt.ret_fue = xDesRF
                    DiaInt.aplicado = 'N'
                    DiaInt.save()
        LinAho = justo.LINEAS_AHORRO.objects.filter(cliente = self.Oficina.cliente,cod_lin_aho = '04').first()
        TasRF = justo.RET_FUE_AHO.objects.filter(lin_aho = LinAho,fecha_inicial__lte=self.fecha_liq, fecha_final__gte=self.fecha_liq).first()
        CdatFecs = justo.CTA_CDAT_AMP.objects.filter(fecha = self.fecha_liq)
        for CdatFec in CdatFecs:
            if CdatFec.cta_aho.oficina != self.Oficina:
                continue
            Cdat = justo.CTA_CDAT.objects.filter(cta_aho = CdatFec.cta_aho).first()
            xPlaMes = Cdat.plazo_mes
            xPer = Cdat.Periodicidad
            xInt = xRetFueNue = xInt = xRetFue = 0
            MovCdas = justo.CTA_CDAT_LIQ.objects.filter(cta_amp = CdatFec.id)
            for MovCda in MovCdas:
                xInt = xInt + MovCda.Val_int
                xRetFue = xRetFue + MovCda.Val_ret + MovCda.Val_ret_nue
                xRefFueNue = xRetFueNue + MovCda.Val_ret_nue
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
            justo.CTA_CDAT_LIQ.objects.filter(cta_amp = CdatFec,fecha__gte = self.fecha_liq).delete()
            MovCdaLiq = justo.CTA_CDAT_LIQ.objects.filter(cta_aho = CdatFec.cta_aho,cta_amp = CdatFec,fecha = self.fecha_liq,tip_liq = 'C').first()
            if MovCdaLiq == None:
                MovCdaLiq = justo.CTA_CDAT_LIQ.objects.create(cta_aho = CdatFec.cta_aho,cta_amp = CdatFec,fecha = self.fecha_liq,tip_liq = 'C')
            MovCdaLiq.fecha = self.fecha_liq
            MovCdaLiq.Val_int = xIntPorApl
            MovCdaLiq.Val_ret = xRetFuePorApl if xUltRetFue > 0 else 0
            MovCdaLiq.Val_ret_nue = 0
            MovCdaLiq.save()
            MovCdaLiq1 = justo.CTA_CDAT_LIQ.objects.filter(cta_aho = CdatFec.cta_aho,cta_amp = CdatFec,fecha = self.fecha_liq,tip_liq = 'P').first()
            if MovCdaLiq1 == None:
                MovCdaLiq1 = justo.CTA_CDAT_LIQ.objects.create(cta_aho = CdatFec.cta_aho,cta_amp = CdatFec,fecha = self.fecha_liq,tip_liq = 'P')
            MovCdaLiq1.fecha = self.fecha_liq
            MovCdaLiq1.Val_int = CdatFec.valor
            MovCdaLiq1.Val_ret = -(xRetFue + xRetFuePorApl)
            MovCdaLiq1.Val_ret_nue = 0
            MovCdaLiq1.save()
            xCtaPXCda = LinAho.cta_por_pas
            CtaAho = justo.CTAS_AHORRO.objects.filter(oficina = self.Oficina,id = Cdat.cta_aho_id).first()
            ImpCon = justo.IMP_CON_LIN_AHO.objects.filter(linea_ahorro = LinAho,cod_imp = CtaAho.cod_imp ).first()
            xCtaAhoDes = ImpCon.ctaafeact if CtaAho.est_cta == 'A' else ImpCon.ctaafeint
            xCtaInt = ImpCon.ctaafeint
            xCtaRetFue = ImpCon.ctaretfue
            if xIntPorApl > 0:
                PlaCtaInt = justo.PLAN_CTAS.objects.filter(cliente = self.Oficina.cliente, per_con = self.fecha_liq.year,cod_cta = xCtaInt).first()
                DetEcoInt = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaInt,tercero = CtaAho.asociado.tercero).first()
                if DetEcoInt == None:
                    DetEcoInt = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaInt,tercero = CtaAho.asociado.tercero)
                DetEcoInt.detalle = 'Gasto Causado Cta_aho '+CtaAho.num_cta
                DetEcoInt.debito = xIntPorApl
                DetEcoInt.credito = 0
                DetEcoInt.valor_1 = 0
                DetEcoInt.valor_2 = 0
                DetEcoInt.save()
                PlaCtaPag = justo.PLAN_CTAS.objects.filter(cliente = self.Oficina.cliente, per_con = self.fecha_liq.year,cod_cta = xCtaPXCda).first()
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
                PlaCtaPag = justo.PLAN_CTAS.objects.filter(cliente = self.Oficina.cliente, per_con = self.fecha_liq.year,cod_cta = xCtaPXCda).first()
                DetEcoPag = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaPag,tercero = CtaAho.asociado.tercero).first()
                if DetEcoInt == None:
                    DetEcoPag = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaPag,tercero = CtaAho.asociado.tercero)
                DetEcoPag.detalle = 'Ctas Por Pag Cta_aho '+CtaAho.num_cta
                DetEcoPag.debito = xIntPorApl+xInt-xRetFue-xRetFuePorApl
                DetEcoPag.credito = 0
                DetEcoPag.valor_1 = 0
                DetEcoPag.valor_2 = 0
                DetEcoPag.save()
                PlaCtaAho = justo.PLAN_CTAS.objects.filter(cliente = self.Oficina.cliente, per_con = self.fecha_liq.year,cod_cta = xCtaAhoDes).first()
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
        return
    
    def interes_mensual(self):
        if not es_ultimo_dia_del_mes(self.fecha_liq):
            print('No se Puede liquidar el Interes Mensual si la fecha no es el ultimo dia del mes ')
            return
        Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
        Doc = justo.DOCTO_CONTA.objects.filter(oficina = self.Oficina,per_con = self.fecha_liq.year,codigo = 131).first()
        HecEco = justo.HECHO_ECONO.objects.filter(docto_conta = Doc,numero = self.fecha_liq.timetuple().tm_yday).first()
        if HecEco == None:
            print('No se ha Realizado la Luiquidacion der Innteres diario a la fecha')
            return
        xUltDiaFec = ultimo_dia_mes_anterior(self.fecha_liq)
        print('Inicio Saldos Ahorro Mensual ',datetime.now())
        # Ctas = justo.CTAS_AHORRO.objects.filter(oficina = self.Oficina,est_cta = 'A').exclude(Q(num_cta__startswith='04'))
        Ctas = justo.CTAS_AHORRO.objects.filter(oficina=self.Oficina, est_cta='A').filter(Q(num_cta__startswith='01') | Q(num_cta__startswith='02') | Q(num_cta__startswith='06') | Q(num_cta__startswith='07') )
        saldo = 0
        conta = 0
        for Cta in Ctas:
            self.saldo_cta(Cta.num_cta,xUltDiaFec)
            xSalIni = self.saldo_fecha
            MovPers = justo.DETALLE_ECONO.objects.filter(detalle_prod__producto='AH',detalle_prod__subcuenta=Cta.num_cta, hecho_econo__fecha__gt=xUltDiaFec,
                hecho_econo__fecha__lte=self.fecha_liq, hecho_econo__docto_conta__oficina=Oficina).exclude(item_concepto='IntCor').order_by('hecho_econo__fecha')
            xFecAnt = xUltDiaFec
            xNueSal = xSalIni
            xSalPro = 0
            for MovPer in MovPers:
                xSalPro = xSalPro + xNueSal*(MovPer.hecho_econo.fecha - xFecAnt).days
                xFecAnt = MovPer.hecho_econo.fecha
                xNueSal = xNueSal + MovPer.debito - MovPer.credito
            LinAho = justo.LINEAS_AHORRO.objects.filter(cliente = self.Oficina.cliente,cod_lin_aho = Cta.num_cta[0:2]).first()
            TasLin = justo.TAS_LIN_AHO.objects.filter(lin_aho=LinAho,fecha_inicial__lte=self.fecha_liq, fecha_final__gte=self.fecha_liq).first()
            TasRF = justo.RET_FUE_AHO.objects.filter(lin_aho = LinAho,fecha_inicial__lte=self.fecha_liq, fecha_final__gte=self.fecha_liq).first()
            xTasAnuEfe = TasLin.tiae / 100
            xTasIntMes = ((1+xTasAnuEfe/12)**(1/12)-1)*12
            xDiaMes = self.fecha_liq.day
            xSalPro = xSalPro + xNueSal*((self.fecha_liq - xFecAnt).days+1)
            xSalPro = round(xSalPro/xDiaMes,0)
            xIntMes = round(xSalPro*xTasIntMes,0) 
            if xIntMes < 0:
                DetPro = justo.DETALLE_PROD.objects.filter(hecho_econo = HecEco,producto = 'AH',concepto = 'AHO',subcuenta = Cta.num_cta).first()
                if DetPro == None:
                    DetPro = justo.DETALLE_PROD.objects.create(hecho_econo = HecEco,producto = 'AH',concepto = 'AHO',subcuenta = Cta.num_cta)
                DetPro.save()
                ImpCon = justo.IMP_CON_LIN_AHO.objects.filter(linea_ahorro = LinAho,cod_imp = Cta.cod_imp).first()
                PlaCtaCta = justo.PLAN_CTAS.objects.filter(cliente = self.Oficina.cliente, per_con = self.fecha_liq.year,cod_cta = ImpCon.ctaafeact).first()
                DetEcoMov = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaCta,tercero = Cta.asociado.tercero).first()
                if DetEcoMov == None:
                    DetEcoMov = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaCta,tercero = Cta.asociado.tercero)
                DetEcoMov.detalle_prod = DetPro
                DetEcoMov.item_concepto = 'IntCor'
                DetEcoMov.detalle = 'IntCor del Mes.  Cta '+Cta.num_cta
                DetEcoMov.debito = 0
                DetEcoMov.credito = -xIntMes
                DetEcoMov.valor_1 = 0
                DetEcoMov.valor_2 = 0
                DetEcoMov.save()
                if -xIntMes > TasRF.bas_liq_int * xDiaMes:
                    xDesRet = round(-xIntMes * TasRF.tas_liq_rf/100,0)
                    PlaCtaCta = justo.PLAN_CTAS.objects.filter(cliente = self.Oficina.cliente, per_con = self.fecha_liq.year,cod_cta = ImpCon.ctaretfue).first()
                    DetEcoMovRet = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaCta,tercero = Cta.asociado.tercero).first()
                    if DetEcoMovRet == None:
                        DetEcoMovRet = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaCta,tercero = Cta.asociado.tercero)
                    DetEcoMov.detalle_prod = DetPro
                    DetEcoMov.item_concepto = 'IntCor'
                    DetEcoMov.detalle = 'Ret Fte del Mes.  Cta '+Cta.num_cta
                    DetEcoMov.debito = xDesRet
                    DetEcoMov.credito = 0
                    DetEcoMov.valor_1 = 0
                    DetEcoMov.valor_2 = 0
                    DetEcoMov.save()
                    
        IntDias = justo.INT_DIA_AHO.objects.filter(aplicado='N', fecha__month=self.fecha_liq.month, oficina=Oficina).values('num_cta').annotate(total_int=Sum('int_dia'), total_ret_fue=Sum('ret_fue'))
        for IntDia in IntDias:
            if IntDia['total_int'] >= 0:
                continue
            CtaAho = justo.CTAS_AHORRO.objects.filter(oficina = self.Oficina,num_cta = IntDia['num_cta']).first()
            LinAho = justo.LINEAS_AHORRO.objects.filter(cliente = self.Oficina.cliente,cod_lin_aho = CtaAho.num_cta[0:2]).first()
            DetPro = justo.DETALLE_PROD.objects.filter(hecho_econo = HecEco,producto = 'AH',concepto = 'AHO',subcuenta = IntDia['num_cta']).first()
            if DetPro == None:
                DetPro = justo.DETALLE_PROD.objects.create(hecho_econo = HecEco,producto = 'AH',concepto = 'AHO',subcuenta = IntDia['num_cta'])
            DetPro.save()
            ImpCon = justo.IMP_CON_LIN_AHO.objects.filter(linea_ahorro = LinAho,cod_imp = CtaAho.cod_imp).first()
            PlaCtaCta = justo.PLAN_CTAS.objects.filter(cliente = self.Oficina.cliente, per_con = self.fecha_liq.year,cod_cta = ImpCon.ctaafeact).first()
            DetEcoMov = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaCta,tercero = Cta.asociado.tercero).first()
            if DetEcoMov == None:
                DetEcoMov = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaCta,tercero = CtaAho.asociado.tercero)
            DetEcoMov.detalle_prod = DetPro
            DetEcoMov.item_concepto = 'IntCor'
            DetEcoMov.detalle = 'IntCor Diario del Mes  Cta '+CtaAho.num_cta
            DetEcoMov.debito = 0
            DetEcoMov.credito = -IntDia['total_int']
            DetEcoMov.valor_1 = 0
            DetEcoMov.valor_2 = 0
            DetEcoMov.save()
            if IntDia['total_ret_fue'] > 0:
                PlaCtaCta = justo.PLAN_CTAS.objects.filter(cliente = self.Oficina.cliente, per_con = self.fecha_liq.year,cod_cta = ImpCon.ctaretfue).first()
                DetEcoMovRet = justo.DETALLE_ECONO.objects.filter(hecho_econo = HecEco,cuenta = PlaCtaCta,tercero = Cta.asociado.tercero).first()
                if DetEcoMovRet == None:
                    DetEcoMovRet = justo.DETALLE_ECONO.objects.create(hecho_econo = HecEco,cuenta = PlaCtaCta,tercero = Cta.asociado.tercero)
                DetEcoMov.detalle_prod = DetPro
                DetEcoMov.item_concepto = 'IntCor'
                DetEcoMov.detalle = 'Ret Fte diario del Mes.  Cta '+Cta.num_cta
                DetEcoMov.debito = IntDia['total_ret_fue']
                DetEcoMov.credito = 0
                DetEcoMov.valor_1 = 0
                DetEcoMov.valor_2 = 0
                DetEcoMov.save()


        print('Saldo MensuaL ',saldo,'  Cuentas',conta)
        print('Final Saldos Ahorro  Mensual ',datetime.now())
        return

def init():
    print('Saldo Total    ',datetime.now())     
    fecha_liq = date(2023,12,31)
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    MiAho = ahorros(Oficina,fecha_liq)
    MiAho.interes_mensual()
    print('Fin Saldos Ahorro     ',datetime.now())
    return

init()
