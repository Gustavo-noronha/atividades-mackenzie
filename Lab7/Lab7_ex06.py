qtd = int(input("Quantidade de empregados: "))
count_10 = 0
soma_salarios = 0
for _ in range(qtd):
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    if salario >= 3000:
        novo = salario * 1.08
    elif salario >= 2000:
        novo = salario * 1.10
        count_10 += 1
    else:
        novo = salario * 1.12
    soma_salarios += novo
    print(f"{nome} - Salário reajustado: R$ {novo:.2f}")
print(f"Empregados com reajuste de 10%: {count_10}")
print(f"Salário médio: R$ {soma_salarios / qtd:.2f}")
