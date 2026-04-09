total_compra = float(input("Valor total da compra: "))
total_recebido = 0

while total_recebido < total_compra:
    cedula = float(input(f"Insira o valor: "))
    total_recebido += cedula
    print(f"Falta pagar: R$ {total_compra - total_recebido}")

print("Pagamento concluido")
print(f"Troco:  {total_recebido - total_compra}")