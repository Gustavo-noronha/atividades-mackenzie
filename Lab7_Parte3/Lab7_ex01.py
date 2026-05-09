def divisores(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    return contador

numero= int(input('Numero: '))


def primo (numero):
    if divisores(numero)== 2:
        return True
    else:
        return False
print(divisores(numero),primo(numero))
