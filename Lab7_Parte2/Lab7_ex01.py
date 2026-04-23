senha=int(float(input('Digite a sua senha: ')))
correta = 1234
while senha != correta:
    print('Senha incorreta')
    senha=int(input('Digite a sua senha: '))
print('Acesso Permitido! Bem-vindo(a)')

