def ver_triangulo(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            print('Equilátero')
        elif a!=b and b!=c and a!=c:
            print('Escaleno')
        else:
            print('Isósceles')
    else:
        print('Não é um triângulo')
def dados_triangulo():
    a = float(input('Lado A: '))
    b = float(input('Lado B: '))
    c = float(input('Lado C: '))
    return a,b,c
def principal():
    a,b,c = dados_triangulo()
    ver_triangulo(a,b,c)


principal()