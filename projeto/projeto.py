import math
import random
import datetime
import statistics
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')#o meu computador ficava puxando o padrão americano ai tive que forçar para br

def valor_br(dinheiro):#converte para padrão BR
    return locale.currency(dinheiro, grouping=True)

def converter_taxa_cdi (taxa):#cdi anual para mensal
    taxa_nova=taxa/100 #divir para sair de % e ir para decimal
    Imensal=math.pow(1+taxa_nova, 1/12)-1
    return Imensal

def regressiva_ir (prazo_investimento):#imposto cdb
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

def calcular_cdb (cap_inicial,apo_mensal,prazo_investimento,cdi,perc_cdi_cdb):#calcula o valor final do cdb
    taxa_mensal_cdi=converter_taxa_cdi(cdi)#chamando a função cdi
    taxa_total= taxa_mensal_cdi*(perc_cdi_cdb/100)#taxa
    valor_bruto=cap_inicial* math.pow(1 + taxa_total,prazo_investimento)+ apo_mensal*((math.pow(1+taxa_total, prazo_investimento)-1)/taxa_total)#valor bruto
    total_investido=cap_inicial+(apo_mensal*prazo_investimento)#total investido
    lucro=valor_bruto-total_investido#lucro
    valor_final=valor_bruto-(lucro*regressiva_ir(prazo_investimento))#valor final
    return valor_final

def calcular_fii (cap_inicial, apo_mensal, prazo_investimento, renta_mensa):
    taxa_convertida=renta_mensa/100#% para decimal 
    valor_principal=cap_inicial*math.pow(1+taxa_convertida, prazo_investimento) + apo_mensal * ((math.pow(1+taxa_convertida, prazo_investimento)-1)/taxa_convertida)
    calculo1=valor_principal*(1 + random.uniform(-0.03, 0.03))#gera os 5 testes aleatorios
    calculo2=valor_principal*(1 + random.uniform(-0.03, 0.03))
    calculo3=valor_principal*(1 + random.uniform(-0.03, 0.03))
    calculo4=valor_principal*(1 + random.uniform(-0.03, 0.03))
    calculo5=valor_principal*(1 + random.uniform(-0.03, 0.03))
    calculos=[calculo1, calculo2, calculo3, calculo4, calculo5]#cria uma lista para statistics conseguir ler
    media=statistics.mean(calculos)#gera media
    mediana = statistics.median(calculos)#gera mediana
    desvio = statistics.stdev(calculos)#gera desvio padrao
    return media,mediana,desvio
def graficos (cdb_1,media_fii):#gera a quantidade de blocos a serem usadas
    maior=max(cdb_1,media_fii)#pega o maior valor presente
    barra_cdb=int((cdb_1/maior)*50)
    barra_fii=int((media_fii/maior)*50)
    return barra_cdb,barra_fii

def dados():#valores a serem enseridos
    cap_inicial=float(input('Capital inicial: '))
    apo_mensal=float(input('Qual aporte mensal: '))
    prazo_investimento=float(input('Qual o prazo do investimento(em meses): '))
    cdi=float(input('CDI anual(%): '))
    perc_cdi_cdb=float(input('Percentual do CDI aplicado ao CDB (%): '))
    perc_cdi_lci=float(input('Percentual do CDI aplicado à LCI/LCA (%): '))
    renta_mensa=float(input('Rentabilidade mensal esperada do FII (%): '))
    meta=float(input('Meta financeira desejada: '))
    return cap_inicial, apo_mensal, prazo_investimento, cdi, perc_cdi_cdb, perc_cdi_lci, renta_mensa, meta

def data_e_total (prazo_investimento,cap_inicial,apo_mensal):#define dia e resgate , valor final e ainda separa visualmente os blocos
    hoje=datetime.datetime.now()#dia da simulação
    resgate=hoje+datetime.timedelta(days=prazo_investimento*30)#dia do resgate
    total_investido=cap_inicial+(apo_mensal*prazo_investimento)#total investido
    print('')
    print('=====================================================')#enfeite
    print(f'PyInvest - Simulador {hoje.strftime('%d/%m/%Y')}')#data da simulação
    print(f'Data estimada de resgate {resgate.strftime('%d/%m/%Y')} ')#data resgate
    print(f'Total investido: {valor_br(total_investido)}')#total investido
    print('_____________________________________________________')#enfeite

def validação (cap_inicial,apo_mensal,prazo_investimento):#verifica se os valores são positivos ou negativos
    if cap_inicial<=0 or apo_mensal<=0 or prazo_investimento<=0:
        print('Erro,a Capital inicial o Aporte mensal e o Prazo precisam ser positivos.')
        exit()#finaliza a função

def principal ():#função principal para reunir os prints
    print('===== PyInvest - Simulador ===========================')#enfeite
    cap_inicial, apo_mensal, prazo_investimento, cdi, perc_cdi_cdb, perc_cdi_lci, renta_mensa, meta=dados()#chama os input e guarda eles 
    media_fii, mediana_fii, desvio_fii = calcular_fii(cap_inicial, apo_mensal, prazo_investimento, renta_mensa)#cria variaveis para eu conseguir escolher qual informacao do retunr eu quero
    cdb_1= calcular_cdb(cap_inicial, apo_mensal, prazo_investimento, cdi, perc_cdi_cdb)#transforma a função em um variavel
    barra_cdb,barra_fii=graficos(cdb_1,media_fii)#cria variaveis para eu conseguir escolher qual informacao do retunr eu quero
    validação(cap_inicial,apo_mensal,prazo_investimento)#chama a validação para ela testar 
    data_e_total(prazo_investimento,cap_inicial,apo_mensal)#mostra a hora e o prazo
    print(f'CDB         : {valor_br(calcular_cdb(cap_inicial,apo_mensal,prazo_investimento,cdi,perc_cdi_cdb))}')#valor cdb
    print(f'Grafico     : {'█'*barra_cdb}')#gera o grafico 
    print(f'FII (Media) : {valor_br(media_fii)}')#valor FII
    print(f'Grafico     : {'█'*barra_fii}')#gera o grafico 
    print(f'A mediana de FII foi de {valor_br(mediana_fii)}')#gera a mediana 
    print(f'O desvio padrão de FII foi de {valor_br(desvio_fii)}') #gera o desvio
principal()#inicial a função principal para colocar os dados
