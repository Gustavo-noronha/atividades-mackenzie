kilos=int(input('quantos kilos de peixe?'))
if kilos<=50:
          print('Dentro do regulamento')
else:
    excedente=kilos-50
    multa=excedente*4
    print(f'fora do regulamento com {excedente} kilos excedentes e tera que pagar uma multa de {multa} reais')
