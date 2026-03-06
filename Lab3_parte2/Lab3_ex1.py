salario_bruto=float(input('Qual o valor do salário bruto?'))
parcela_pretendida=float(input('Qual o valor da parcela pretendida'))
tempo_serviço=int(input('Qual o tempo?'))
pontuacao=int(input('qual sua pontuaçao?'))
if (tempo_serviço< 12) and (pontuacao>=800)and (parcela_pretendida<= (0.3*salario_bruto)):
    print('emprestimo aprovado 2 caso')
elif (parcela_pretendida<= (0.3*salario_bruto)) and (tempo_serviço>=12):
    print('emprestimo aprovado 1caso')
else:
    print('reprovado')
