import math
import random
import datetime
import statistics
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
def valor_br(dinheiro):#converte para padrão BR
    return locale.currency(dinheiro, grouping=True)
def valor_cdi (taxa):
    taxa_nova=taxa/100
    Imensal=(1+taxa_nova)**(1/12)-1
    return Imensal
def regressiva_ir (prazo_investimento):
    dias=prazo_investimento*30
    if dias<=180:
        taxa=0.225
    elif dias<=360:
        taxa=0.2
    elif dias<=720:
        taxa=0.175
    else:
        taxa=0.15
    return taxa
def valor_cdb (cap_inicial,apo_mensal,prazo_investimento,cdi,perc_cdi_cdb):
    taxa_mensal_cdi=valor_cdi(cdi)
    taxa_total= taxa_mensal_cdi*(perc_cdi_cdb/100)
    valor_bruto=cap_inicial*(1 + taxa_total)**prazo_investimento + apo_mensal * (((1+taxa_total)**prazo_investimento-1)/taxa_total)
    total_investido=cap_inicial+(apo_mensal*prazo_investimento)
    lucro=valor_bruto-total_investido
    valor_final=valor_bruto-(lucro*regressiva_ir(prazo_investimento))
    return valor_final
def dados():
    cap_inicial=float(input('Capital inicial: '))
    apo_mensal=float(input('qual aporte mensal: '))
    prazo_investimento=float(input('qual o prazo do investimento(em meses): '))
    cdi=float(input('CDI anual(%): '))
    perc_cdi_cdb=float(input('Percentual do CDI aplicado ao CDB (%): '))
    perc_cdi_lci=float(input('Percentual do CDI aplicado à LCI/LCA (%): '))
    renta_mensa=float(input('Rentabilidade mensal esperada do FII (%): '))
    meta=float(input('Meta financeira desejada: '))
    return cap_inicial, apo_mensal, prazo_investimento, cdi, perc_cdi_cdb, perc_cdi_lci, renta_mensa, meta
def main():
    cap_inicial, apo_mensal, prazo_investimento, cdi, perc_cdi_cdb, perc_cdi_lci, renta_mensa, meta=dados()
main()
