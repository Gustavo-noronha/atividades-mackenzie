documentos_pendentes = ['relatorio.pdf','foto.pdf','audio.pdf','documento.pdf','trabalho.pdf','texto.pdf','word.pdf','exel.pdf','powerpoint.pdf','opera.pdf']
print('----Menu----')
print('A Simule erro')
print('B organizar por nome')
escolha = input("Qual voce quer?").upper()
if escolha == 'A':
  print(documentos_pendentes)
  print('Erro na primeira linha')
  for i in range(2):
    item = documentos_pendentes.pop(0)
    documentos_pendentes.append(item)
  print(documentos_pendentes)
  
elif escolha == 'B':
    print('Por ordem')
    documentos_pendentes.sort()
    print(documentos_pendentes)
else:
    print('Invalido')
    






