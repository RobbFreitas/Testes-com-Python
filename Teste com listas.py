lista = []  
#Condição para formação da lista
while True:
  num = int(input('Informe números para a lista (digite 0 para finalizar a lista): '))
  if num == 0:
    break
  lista.append(num)
  #Variável para identificação do número caso esteja na lista ou não
num2 = int(input('Procure por tal número:  '))
if num2 in lista:
  print('Número encontrado: {}'.format(num2))
else:
    print('Não encontrado')
print('A lista é: ', lista)
