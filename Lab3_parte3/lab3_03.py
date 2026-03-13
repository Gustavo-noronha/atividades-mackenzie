peso=int(input('quantos kg de peixe?'))
if peso<=50:
    print('dentro de regulamento')
else:
    execesso=peso-50
    multa=execesso*4
    print(f'fora do regulamento com {execesso}kg de execesso de peixe com multa de {multa} reais')