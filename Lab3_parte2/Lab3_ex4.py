ladoa=float(input('qual o valor do lado A?'))
ladob=float(input('qual o valor do lado B?'))
ladoc=float(input('qual o valor do lado C?'))
if (ladoa+ladob)<ladoc or (ladoa+ladoc)<ladob or(ladob+ladoc)<ladoa:
    print('nao existe esse triangulo')
elif ladoa==ladob==ladoc:
    print('triangulo equilatero')
elif ladoa==ladob or ladoa==ladoc or ladob==ladoc:
    print('triangulo isosceles')
else:
    print('triangulo escaleno')
