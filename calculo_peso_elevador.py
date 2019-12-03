peso_max = 500
peso_total = 0
x = 0
while peso_total <= peso_max:
    peso_pessoa = float(input('Digite peso do passageiro {0}: '.format(x + 1)))
    peso_total += peso_pessoa
    x += 1
    if peso_total == peso_max:
        print('Máximo valor atingido')
        break
    elif peso_total > 500:
        print('Valor máximo ultrapassado')
print('Comportado {} passageiros'.format(x))
