numero=int(input('Digite um numero inteiro: '))
numero_inicial=numero
invertido = 0
while numero > 0:
    ultimo_digito = numero % 10
    invertido = invertido * 10 + ultimo_digito
    numero = numero // 10
if numero_inicial == invertido:
    print(f'{numero_inicial} é um palíndromo!')
else:
    print(f'{numero_inicial} não é um palíndromo.')