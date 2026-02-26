M=float(input('quantos MM'))
km=M//1000000
restokm=M%1000000
me=restokm//1000
restome=M%1000
cm=restome//10
restocm=M%10

print(km,'km',me,'m',cm,'cm.(Sobram',restocm,'mm)')
