valor=int(input('Digite um valor entre 1 á 3: '))
import random
dado_jogador=random.randint(-10,10)
dado_maquina=random.randint(-10,10)
dano=abs(dado_jogador-dado_maquina)*valor
if dado_jogador>dado_maquina:
    print(f'Voce ganhou! com dado de {dado_jogador} e a maquina com {dado_maquina} gerando um dano de {dano}')
elif dado_jogador<dado_maquina:
    print(f'Voce perdeu! com dado do jogador de {dado_jogador} e a maquina com {dado_maquina} tomando um dano de {dano}')
else:
    print(f'Empate com o dado do jogador de {dado_jogador} e a maquina com {dado_maquina} ')
