n = int(input("Quantos valores? "))
for _ in range(n):
    x = int(input("Digite um número: "))
    fat = 1
    for i in range(1, x + 1):
        fat *= i
    print(f"{x}! = {fat}")
