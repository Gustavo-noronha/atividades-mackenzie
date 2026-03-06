valor_produto=float(input('qual o valor do produto?'))
if valor_produto<=20:
    total=valor_produto*1.45
    print(f'Teve um lucro de 45% e o valor ficou{total}reais')
else:
    total2=valor_produto*1.30
    print(f'Teve um lucro de 30% e o valor ficou{total2}reais')
