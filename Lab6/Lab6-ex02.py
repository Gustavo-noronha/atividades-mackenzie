intervalos = int(input("Quantos intervalos de tempo? "))
leituras = []

for i in range(1, intervalos + 1):
    uso = float(input(f"Intervalo {i} - Uso do recurso (%): "))
    leituras.append(uso)

media = sum(leituras) / len(leituras)
pico = max(leituras)
acima_limite = sum(1 for x in leituras if x > 80)

print(f"\nUso medio: {media}%")
print(f"Pico de uso: {pico}%")
print(f"Vezes acima de 80%: {acima_limite}")