nota1=float(input('digite o primeira nota'))
nota2=float(input('digite o segunda nota'))
nota3=float(input('digite o terceira nota'))
media=((nota1*2)+(nota2*3)+(nota3*5))/10
if media >=6:
    print(f'Aprovado!.Sua media foi {media:.2f}')
else:
    print(f'Reprovado!.Sua media foi {media:.2f}')