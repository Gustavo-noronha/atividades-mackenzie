funcionarios = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

turno_a = []
turno_b = []

print("DISTRIBUIÇÃO DE TURNOS ")
for func in funcionarios:
    while True:
        turno = input(f"{func} -> Turno A ou B? ").strip().upper()
        if turno in ("A", "B"):
            break
        print("  Digite apenas A ou B.")
    
    if turno == "A":
        turno_a.append(func)
    else:
        turno_b.append(func)

print("TROCA DE TURNOS")
print(f"Turno A: {turno_a}")
print(f"Turno B: {turno_b}")

while True:
    saindo_a = input("\nNome do funcionário do Turno A para trocar: ").strip()
    if saindo_a in turno_a:
        break
    print("  Funcionário não encontrado no Turno A.")

while True:
    saindo_b = input("Nome do funcionário do Turno B para trocar: ").strip()
    if saindo_b in turno_b:
        break
    print("  Funcionário não encontrado no Turno B.")

turno_a.remove(saindo_a)
turno_b.remove(saindo_b)
turno_a.append(saindo_b)
turno_b.append(saindo_a)

print("ESTADO FINAL")
print(f"Turno A: {turno_a}")
print(f"Turno B: {turno_b}")
