videos=float(input('quantos vídeos?'))
InsG=videos//100
restoG=videos%100
InsM=restoG//10
InsP=restoG%10
total=InsG*150+InsM*20+InsP*5
print(InsG,'Instancias G',InsM,'Instâncias M',InsP,'Instâncias P. Custo:',total )
