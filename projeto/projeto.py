import math
import random
import datetime
import statistics
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
def valor_br(dinheiro):#converte para padrão BR
    return locale.currency(dinheiro, grouping=True)
cap_inicial=float(input('Capital inicial: '))
apo_mensal=float(input('qual aporte mensal'))
prazo_investimento=float(input('qual o prazo do investimento(em meses): '))
cdi=float(input('CDI anual(%)'))
perc_cdi_cdb=float(input('Percentual do CDI aplicado ao CDB (%): '))
perc_cdi_lci=float(input('Percentual do CDI aplicado à LCI/LCA (%)'))
renta_mensa=float(input('Rentabilidade mensal esperada do FII (%): '))
meta=float(input('Meta financeira desejada: '))
def valor_cdi (taxa):
    Imensal=(1+taxa)**(1/12)-1
    return Imensal
