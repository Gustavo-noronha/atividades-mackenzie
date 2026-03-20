def calcular_conta_luz (l_atual,l_anterior,bandeira):
    consumo=l_atual-l_anterior
    if bandeira == "VERDE":
        valor=consumo*0.5
    elif bandeira == "AMARELA":
        valor=consumo*0.52
    else:
        valor=consumo*0.55
    if consumo>=300:
        valor*=1.1
    return valor
print(f'Valor={calcular_conta_luz(1100,1000,'VERDE')}')
print(f'Valor={calcular_conta_luz(1100,1000,'AMARELA')}')
print(f'Valor={calcular_conta_luz(1500,1000,'VERMELHA')}')