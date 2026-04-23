soma_notas=0
quantidade_notas=0
nota= float(input('Digite a sua nota: '))
while nota != -1:
    quantidade_notas+=1
    soma_notas+=nota
    nota= float(input('Digite uma nova nota: '))
def calcular_media(soma_notas,quantidade_notas):
    return soma_notas/quantidade_notas
print(f'A media deu {calcular_media(soma_notas,quantidade_notas)}')