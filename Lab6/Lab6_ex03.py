numero = input("Digite um número: ")
soma = 0
pares = 0
impares = 0
for digito in numero:
    d = int(digito)
    soma += d
    if d % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Soma dos dígitos: {soma}")
print(f"Dígitos pares: {pares}")
print(f"Dígitos ímpares: {impares}")