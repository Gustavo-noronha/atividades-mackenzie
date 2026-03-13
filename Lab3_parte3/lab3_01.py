salario=float(input('digite seu salario: '))
tempo_de_trabalho=int(input('digite o tempo de trabalho(em anos): '))
if tempo_de_trabalho>=5:
    sn=salario*1.2
    bonus=salario*0.2
    print(f'seu bonus foi de 20% ({bonus}) com seu novo salario de {sn} reais')
else:
    sn2=salario*1.1
    bonus2=salario*0.1
    print(f'seu bonus foi de 10% ({bonus2}) com seu novo salario de {sn2} reais')