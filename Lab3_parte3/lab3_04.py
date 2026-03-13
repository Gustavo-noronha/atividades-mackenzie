valor_do_produto=int(input("qual o valor do produto?"))
nota100=valor_do_produto//100
resto100=valor_do_produto%100
nota50=resto100//50
resto50=resto100%50
nota20=resto50//20
resto20=resto50%20
nota10=resto20//10
resto10=resto20%10
nota5=resto10//5
resto5=resto10%5
nota2=resto10%5
nota1=resto5%2
print(f'sera usadas ({nota100}) notas de 100 ,({nota50}) notas de 50,({nota20}) notas de 20,({nota10}) notas de 10,({nota5}) notas de 5,({nota2}) notas de 2 e ({nota1}) notas de 1')