V=float(input('qual a  velocidade inicial do trem em M/S ?'))
T=float(input('qual foi o tempo de frenagem em segundos?'))
A=-V/T
S=V*T+A*T**2/2
print('a distancia que a trem percorreu ate parar foi de :',S,'metros')
