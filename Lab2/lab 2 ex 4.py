R=float(input("qual sua renda mensal "))
E=float(input("qual o valor do emprestimo"))
N=float(input("qual o numero de parcelas"))
if E>10*R:
    taxa=0.05
else:
    taxa=0.02
juros=E*taxa*N
total=E+juros
parcelas=total/N
if parcelas>0.32000*R:
    print("'Reprovado. Parcela excede 30% da renda.')
elif taxa==0.05 :
    print('Aprovado (Risco Alto). Parcela: RS',parcelas,'(Juros de 5% aplicado)')
else:
    print('Aprovado. Parcela: RS', parcelas)
