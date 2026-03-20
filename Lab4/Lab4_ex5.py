def simular_rendimento (capital_inicial,tempo_meses,tipo_investimento):
    if tipo_investimento=="CDB":
        taxa=0.01
        lucro=capital_inicial*tempo_meses*taxa
        valor_com_imposto=(lucro+capital_inicial)*0.85
        print(f'CDB ,lucro Bruto: {lucro} e o valor total com imposto: {valor_com_imposto}')
    elif tipo_investimento=="POUPANCA":
        taxa = 0.005
        lucro = capital_inicial * tempo_meses * taxa
        valor_final =capital_inicial+lucro
        print(f'POUPANCA,(sem imposto) lucro Bruto: {lucro} e o valor total: {valor_final}')
    else:
        taxa = 0.008
        lucro = capital_inicial * tempo_meses * taxa
        valor_com_imposto = (lucro + capital_inicial) * 0.85
        print(f'TESOURO ,lucro Bruto: {lucro} e o valor total com imposto: {valor_com_imposto}')

def dados():
    capital_inicial=float(input("Insira o capital inicial: "))
    tempo_meses=int(input("Insira a temperatura em meses: "))
    investimento=input("Qual seu investimento?(CDB,POUPANCA,TESOURA): ")
    return capital_inicial,tempo_meses,investimento
def principal():
    capital_inicial,tempo_meses,investimento=dados()
    simular_rendimento(capital_inicial,tempo_meses,investimento)
principal()