for i in range(0,10,2):#de 0 a 10 de 2 em 2 , i= item , e o 10 nao aparece
    print(i)
"""
Uma lista que por exemplo tem 7 elementos e numerada de 0 ate 6 pois começa no 0
"""
notas= [8.0 , 9.1 ,7.0]# tem que usar []
for n in notas:
    print(n)

nota= []#lista vazia
for i in range (1,100):
    nota.append(i)
print(len(nota))#len fala o tamanho das listas

print(nota)#print tudo um do lado do outro
for n in nota:#print tudo separado por linha
    print(n)
for letra in 'teste':
    print(letra)#fala letra por letra
cont = 0 
for vogal in 'amarelo':
    if vogal=='a' or vogal=='e' or vogal=='i' or vogal =='o' or vogal =='u':
        print(vogal)
        cont +=1


print('total de vogais ', cont)

