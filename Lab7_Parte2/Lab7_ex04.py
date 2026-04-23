

def calcular_fatorial():
    n = int(input('Digite um número inteiro positivo: '))
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    print(f'{n}! = {resultado}')

def gerar_fibonacci():
    n = int(input('Quantos termos da sequência de Fibonacci? '))
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

def inverter_digitos():
    numero = int(input('Digite um número inteiro: '))
    original = numero
    invertido = 0
    while numero > 0:
        ultimo_digito = numero % 10
        invertido = invertido * 10 + ultimo_digito
        numero //= 10
    print(f'Número invertido: {invertido}')

def progressao_geometrica():
    a1 = float(input('Digite o primeiro termo (a1): '))
    r  = float(input('Digite a razão (r): '))
    n  = int(input('Quantos termos? '))
    termo = a1
    for i in range(n):
        print(f'Termo {i+1}: {termo:.2f}')
        termo *= r

def verificar_palindromo():
    numero = int(input('Digite um número inteiro: '))
    original = numero
    invertido = 0
    while numero > 0:
        invertido = invertido * 10 + numero % 10
        numero //= 10
    if original == invertido:
        print(f'{original} É um palíndromo!')
    else:
        print(f'{original} NÃO é um palíndromo.')

def soma_digitos():
    numero = int(input('Digite um número inteiro: '))
    soma = 0
    n = abs(numero)
    while n > 0:
        soma += n % 10
        n //= 10
    print(f'Soma dos dígitos de {numero}: {soma}')

while True:
    print('\n===== CALCULADORA =====')
    print('1. Calcular Fatorial')
    print('2. Gerar Sequência de Fibonacci')
    print('3. Inverter Dígitos')
    print('4. Progressão Geométrica (PG)')
    print('5. Verificar Palíndromo Numérico')
    print('6. Soma de Dígitos')
    print('7. Sair do Programa')
    print('================================')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        calcular_fatorial()
    elif opcao == '2':
        gerar_fibonacci()
    elif opcao == '3':
        inverter_digitos()
    elif opcao == '4':
        progressao_geometrica()
    elif opcao == '5':
        verificar_palindromo()
    elif opcao == '6':
        soma_digitos()
    elif opcao == '7':
        print('Encerrando o programa.')
        break
    else:
        print('Opção inválida! Digite um número de 1 a 7.')