cidades = []

for i in range(10):
    print(f"\nCidade {i + 1}:")
    nome = input("  Nome da cidade: ")
    temp = float(input("  Temperatura (°C): "))
    cidades.append([nome, temp])

maior = max(cidades, key=lambda c: c[1])
menor = min(cidades, key=lambda c: c[1])
media = sum(c[1] for c in cidades) / len(cidades)

print("\n======= RESULTADO =======")
print(f"Maior temperatura: {maior[0]} com {maior[1]}°C")
print(f"Menor temperatura: {menor[0]} com {menor[1]}°C")
print(f"Média geral: {media:.1f}°C")
